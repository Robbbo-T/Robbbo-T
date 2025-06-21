#!/usr/bin/env python3
"""
Enhanced Semantic Retrieval Bridge para COAFI Memory System
Versión extendida con soporte para pgvector/Pinecone, control de acceso,
caché de embeddings, métricas de trazabilidad y capacidades RAG.
"""

import os
import json
import time
import logging
import hashlib
import asyncio
from typing import Dict, List, Any, Optional, Union, Tuple
from datetime import datetime, timedelta
import numpy as np
from fastapi import APIRouter, Depends, HTTPException, Query, Header, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import httpx
from sqlalchemy import create_engine, Column, String, Float, JSON, ForeignKey, DateTime, Integer, Boolean, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import pinecone
from redis import Redis
from prometheus_client import Counter, Histogram, Gauge

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("semantic_bridge.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Modelos de datos
class SemanticQueryRequest(BaseModel):
    query: str
    folder_id: Optional[str] = None
    folder_path: Optional[str] = None
    conversation_id: Optional[str] = None
    mood_id: Optional[str] = None
    token_limit: int = 1000
    min_similarity: float = 0.7
    include_metadata: bool = True
    gaia_token: Optional[str] = None
    cache_strategy: str = "default"  # 'none', 'default', 'aggressive'
    
class RetrievalResult(BaseModel):
    id: str
    content: str
    similarity_score: float
    source_type: str  # 'message', 'conversation', 'summary', 'memory_layer'
    metadata: Dict[str, Any]
    token_count: int = 0

class SemanticQueryResponse(BaseModel):
    results: List[RetrievalResult]
    total_results: int
    token_count: int
    processing_time: float
    query_embedding_dimension: int = 1536
    cache_hit: bool = False
    trace_id: str = ""
    validationScore: Optional[float] = None

class RAGRequest(BaseModel):
    query: str
    context_results: List[RetrievalResult]
    mood_id: Optional[str] = None
    max_tokens: int = 500
    temperature: float = 0.7
    
class RAGResponse(BaseModel):
    generated_text: str
    sources: List[Dict[str, Any]]
    token_usage: Dict[str, int]
    processing_time: float
    trace_id: str
    validationScore: Optional[float] = None

class AccessControlPolicy(BaseModel):
    mood_id: Optional[str] = None
    conversation_id: Optional[str] = None
    folder_id: Optional[str] = None
    allowed_operations: List[str] = ["read"]
    expiration: Optional[datetime] = None

# Modelos SQLAlchemy para la base de datos
Base = declarative_base()

class VectorEmbedding(Base):
    __tablename__ = "vector_embeddings"
    
    id = Column(String, primary_key=True)
    text = Column(Text, nullable=False)
    vector = Column(ARRAY(Float), nullable=False)
    source_type = Column(String, nullable=False)
    conversation_id = Column(String, nullable=True)
    folder_id = Column(String, nullable=True)
    mood_id = Column(String, nullable=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class QueryLog(Base):
    __tablename__ = "query_logs"
    
    id = Column(String, primary_key=True)
    query_text = Column(Text, nullable=False)
    mood_id = Column(String, nullable=True)
    conversation_id = Column(String, nullable=True)
    folder_id = Column(String, nullable=True)
    token_count = Column(Integer, nullable=False)
    result_count = Column(Integer, nullable=False)
    processing_time = Column(Float, nullable=False)
    cache_hit = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(String, nullable=True)
    trace_id = Column(String, nullable=False)

# Métricas para Prometheus
QUERY_COUNTER = Counter('semantic_queries_total', 'Total number of semantic queries', ['mood_id', 'cache_hit'])
QUERY_LATENCY = Histogram('semantic_query_latency_seconds', 'Semantic query latency in seconds', ['mood_id', 'cache_hit'])
TOKEN_USAGE = Counter('semantic_token_usage_total', 'Total tokens used in semantic queries', ['mood_id'])
CACHE_SIZE = Gauge('semantic_cache_size', 'Number of items in the embedding cache')
VECTOR_DB_LATENCY = Histogram('vector_db_latency_seconds', 'Vector database query latency in seconds', ['db_type'])

# Clase para gestionar la caché de embeddings
class EmbeddingCache:
    def __init__(self, max_size: int = 1000, ttl: int = 3600):
        """
        Inicializa la caché de embeddings
        
        Args:
            max_size: Tamaño máximo de la caché
            ttl: Tiempo de vida en segundos para las entradas de la caché
        """
        self.redis_client = None
        self.local_cache = {}
        self.max_size = max_size
        self.ttl = ttl
        self.hits = 0
        self.misses = 0
        
        # Intentar conectar a Redis si está disponible
        redis_url = os.environ.get("REDIS_URL")
        if redis_url:
            try:
                self.redis_client = Redis.from_url(redis_url)
                logger.info(f"Connected to Redis cache at {redis_url}")
            except Exception as e:
                logger.warning(f"Failed to connect to Redis: {e}. Using local cache instead.")
    
    def _get_cache_key(self, text: str, mood_id: Optional[str] = None) -> str:
        """Genera una clave de caché única para el texto y mood_id"""
        key_parts = [text]
        if mood_id:
            key_parts.append(mood_id)
        
        key_string = ":".join(key_parts)
        return hashlib.md5(key_string.encode()).hexdigest()
    
    async def get(self, text: str, mood_id: Optional[str] = None) -> Optional[List[float]]:
        """Obtiene un embedding de la caché"""
        cache_key = self._get_cache_key(text, mood_id)
        
        # Intentar obtener de Redis primero
        if self.redis_client:
            try:
                cached_data = self.redis_client.get(cache_key)
                if cached_data:
                    self.hits += 1
                    CACHE_SIZE.set(self.redis_client.dbsize())
                    return json.loads(cached_data)
            except Exception as e:
                logger.warning(f"Redis cache get error: {e}")
        
        # Caer en la caché local si Redis falla o no está disponible
        if cache_key in self.local_cache:
            entry = self.local_cache[cache_key]
            if entry["expires_at"] > time.time():
                self.hits += 1
                return entry["embedding"]
            else:
                # Eliminar entrada expirada
                del self.local_cache[cache_key]
        
        self.misses += 1
        return None
    
    async def set(self, text: str, embedding: List[float], mood_id: Optional[str] = None) -> None:
        """Almacena un embedding en la caché"""
        cache_key = self._get_cache_key(text, mood_id)
        
        # Intentar almacenar en Redis primero
        if self.redis_client:
            try:
                self.redis_client.setex(
                    cache_key,
                    self.ttl,
                    json.dumps(embedding)
                )
                CACHE_SIZE.set(self.redis_client.dbsize())
                return
            except Exception as e:
                logger.warning(f"Redis cache set error: {e}")
        
        # Caer en la caché local si Redis falla o no está disponible
        # Limpiar caché si está llena
        if len(self.local_cache) >= self.max_size:
            # Eliminar la entrada más antigua
            oldest_key = min(self.local_cache.items(), key=lambda x: x[1]["expires_at"])[0]
            del self.local_cache[oldest_key]
        
        self.local_cache[cache_key] = {
            "embedding": embedding,
            "expires_at": time.time() + self.ttl
        }
    
    def get_stats(self) -> Dict[str, Any]:
        """Obtiene estadísticas de la caché"""
        total_requests = self.hits + self.misses
        hit_rate = self.hits / total_requests if total_requests > 0 else 0
        
        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": hit_rate,
            "size": len(self.local_cache) if not self.redis_client else "unknown",
            "using_redis": self.redis_client is not None
        }

# Clase para gestionar el control de acceso
class AccessControl:
    def __init__(self):
        """Inicializa el sistema de control de acceso"""
        self.policies = {}
        self.token_secret = os.environ.get("GAIA_TOKEN_SECRET", "default_secret_key")
        logger.info("Initialized access control system")
    
    def validate_token(self, token: str) -> Dict[str, Any]:
        """
        Valida un token GAIA y extrae sus claims
        
        En una implementación real, esto verificaría la firma JWT
        """
        if not token:
            raise ValueError("Token is required")
        
        # Simulación simple - en producción usar JWT real
        try:
            # Formato simulado: "mood_id:conversation_id:timestamp:signature"
            parts = token.split(":")
            if len(parts) < 3:
                raise ValueError("Invalid token format")
            
            mood_id = parts[0] if parts[0] != "null" else None
            conversation_id = parts[1] if parts[1] != "null" else None
            timestamp_str = parts[2]
            
            # Verificar expiración
            timestamp = int(timestamp_str)
            if timestamp < int(time.time()):
                raise ValueError("Token expired")
            
            return {
                "mood_id": mood_id,
                "conversation_id": conversation_id,
                "exp": timestamp
            }
        except Exception as e:
            logger.error(f"Token validation error: {e}")
            raise ValueError(f"Invalid token: {str(e)}")
    
    def check_access(
        self, 
        operation: str,
        mood_id: Optional[str] = None,
        conversation_id: Optional[str] = None,
        folder_id: Optional[str] = None,
        token: Optional[str] = None
    ) -> bool:
        """
        Verifica si se permite el acceso para la operación y recursos especificados
        
        Args:
            operation: Operación a realizar (read, write, delete)
            mood_id: ID del mood al que se accede
            conversation_id: ID de la conversación a la que se accede
            folder_id: ID de la carpeta a la que se accede
            token: Token GAIA opcional para autenticación
            
        Returns:
            bool: True si se permite el acceso, False en caso contrario
        """
        # Si no hay token, verificar políticas locales
        if not token:
            # Verificar si hay una política que coincida
            for policy_key, policy in self.policies.items():
                if self._policy_matches(policy, mood_id, conversation_id, folder_id):
                    if operation in policy.allowed_operations:
                        if not policy.expiration or policy.expiration > datetime.now():
                            return True
            return False
        
        # Validar token GAIA
        try:
            claims = self.validate_token(token)
            
            # Verificar si el token tiene acceso a los recursos solicitados
            token_mood_id = claims.get("mood_id")
            token_conversation_id = claims.get("conversation_id")
            
            # Si el token especifica un mood_id, debe coincidir con el solicitado
            if token_mood_id and mood_id and token_mood_id != mood_id:
                return False
                
            # Si el token especifica un conversation_id, debe coincidir con el solicitado
            if token_conversation_id and conversation_id and token_conversation_id != conversation_id:
                return False
                
            # Si llegamos aquí, el token es válido para los recursos solicitados
            return True
            
        except ValueError as e:
            logger.warning(f"Access denied: {e}")
            return False
    
    def _policy_matches(
        self, 
        policy: AccessControlPolicy,
        mood_id: Optional[str],
        conversation_id: Optional[str],
        folder_id: Optional[str]
    ) -> bool:
        """Verifica si una política coincide con los recursos solicitados"""
        if policy.mood_id and mood_id and policy.mood_id != mood_id:
            return False
            
        if policy.conversation_id and conversation_id and policy.conversation_id != conversation_id:
            return False
            
        if policy.folder_id and folder_id and policy.folder_id != folder_id:
            return False
            
        return True
    
    def add_policy(self, policy: AccessControlPolicy) -> str:
        """Añade una nueva política de control de acceso"""
        policy_id = f"policy_{len(self.policies) + 1}"
        self.policies[policy_id] = policy
        return policy_id
    
    def remove_policy(self, policy_id: str) -> bool:
        """Elimina una política de control de acceso"""
        if policy_id in self.policies:
            del self.policies[policy_id]
            return True
        return False

# Clase para gestionar las operaciones vectoriales
class VectorOperations:
    """Operaciones vectoriales para recuperación semántica y optimización"""
    
    def __init__(self, vector_dimension: int = 1536):
        self.vector_dimension = vector_dimension
        self.xai_api_key = os.environ.get("reciprocity_XAI_API_KEY", "")
        self.embedding_cache = EmbeddingCache()
        self.db_type = os.environ.get("VECTOR_DB_TYPE", "mock").lower()
        
        # Inicializar la base de datos vectorial según la configuración
        if self.db_type == "pinecone":
            self._init_pinecone()
        elif self.db_type == "pgvector":
            self._init_pgvector()
        else:
            logger.warning(f"Using mock vector database (type: {self.db_type})")
        
        if not self.xai_api_key:
            logger.warning("No XAI API key found. Using mock embeddings.")
    
    def _init_pinecone(self):
        """Inicializa la conexión a Pinecone"""
        try:
            api_key = os.environ.get("PINECONE_API_KEY")
            environment = os.environ.get("PINECONE_ENVIRONMENT")
            index_name = os.environ.get("PINECONE_INDEX", "coafi-memory")
            
            if not api_key or not environment:
                raise ValueError("Missing Pinecone credentials")
                
            pinecone.init(api_key=api_key, environment=environment)
            
            # Verificar si el índice existe, si no, crearlo
            if index_name not in pinecone.list_indexes():
                pinecone.create_index(
                    name=index_name,
                    dimension=self.vector_dimension,
                    metric="cosine"
                )
                
            self.pinecone_index = pinecone.Index(index_name)
            logger.info(f"Connected to Pinecone index: {index_name}")
        except Exception as e:
            logger.error(f"Failed to initialize Pinecone: {e}")
            self.db_type = "mock"
    
    def _init_pgvector(self):
        """Inicializa la conexión a PostgreSQL con pgvector"""
        try:
            db_url = os.environ.get("DATABASE_URL")
            if not db_url:
                raise ValueError("Missing DATABASE_URL for pgvector")
                
            self.db_engine = create_engine(db_url)
            Base.metadata.create_all(self.db_engine)
            self.db_session = sessionmaker(bind=self.db_engine)
            
            # Verificar que la extensión pgvector esté instalada
            with self.db_engine.connect() as conn:
                result = conn.execute("SELECT * FROM pg_extension WHERE extname = 'vector'").fetchone()
                if not result:
                    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
                    conn.commit()
            
            logger.info(f"Connected to PostgreSQL with pgvector extension")
        except Exception as e:
            logger.error(f"Failed to initialize pgvector: {e}")
            self.db_type = "mock"
    
    async def get_embedding(self, text: str, mood_id: Optional[str] = None, use_cache: bool = True) -> List[float]:
        """Obtiene el embedding para un texto usando Reciprocity XAI o fallback a mock"""
        # Verificar caché primero si está habilitada
        if use_cache:
            cached_embedding = await self.embedding_cache.get(text, mood_id)
            if cached_embedding:
                logger.debug(f"Cache hit for text: {text[:30]}...")
                return cached_embedding
        
        if self.xai_api_key:
            try:
                # Usar API de embedding real con clave XAI
                async with httpx.AsyncClient() as client:
                    start_time = time.time()
                    response = await client.post(
                        "https://api.reciprocity-xai.com/v1/embeddings",
                        headers={"Authorization": f"Bearer {self.xai_api_key}"},
                        json={"text": text}
                    )
                    
                    if response.status_code != 200:
                        raise Exception(f"API error: {response.status_code} - {response.text}")
                    
                    embedding = response.json()["embedding"]
                    
                    # Guardar en caché si está habilitada
                    if use_cache:
                        await self.embedding_cache.set(text, embedding, mood_id)
                    
                    return embedding
            except Exception as e:
                logger.error(f"Error getting embedding: {e}")
                embedding = self._get_mock_embedding()
                
                # Guardar en caché incluso el mock para consistencia
                if use_cache:
                    await self.embedding_cache.set(text, embedding, mood_id)
                
                return embedding
        else:
            embedding = self._get_mock_embedding()
            
            # Guardar en caché si está habilitada
            if use_cache:
                await self.embedding_cache.set(text, embedding, mood_id)
            
            return embedding
    
    def _get_mock_embedding(self) -> List[float]:
        """Genera un embedding simulado para pruebas sin acceso a API"""
        return list(np.random.uniform(-1, 1, self.vector_dimension))
    
    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calcula la similitud del coseno entre dos vectores"""
        if len(vec1) != len(vec2):
            raise ValueError(f"Las dimensiones de los vectores no coinciden: {len(vec1)} vs {len(vec2)}")
        
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = sum(a * a for a in vec1) ** 0.5
        magnitude2 = sum(b * b for b in vec2) ** 0.5
        
        if magnitude1 * magnitude2 == 0:
            return 0
            
        return dot_product / (magnitude1 * magnitude2)
    
    async def store_vector(
        self,
        text: str,
        vector: List[float],
        source_type: str,
        conversation_id: Optional[str] = None,
        folder_id: Optional[str] = None,
        mood_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Almacena un vector en la base de datos vectorial
        
        Args:
            text: Texto original
            vector: Vector de embedding
            source_type: Tipo de fuente (message, conversation, summary, memory_layer)
            conversation_id: ID de la conversación (opcional)
            folder_id: ID de la carpeta (opcional)
            mood_id: ID del mood (opcional)
            metadata: Metadatos adicionales (opcional)
            
        Returns:
            str: ID del vector almacenado
        """
        vector_id = f"vec_{int(time.time())}_{hashlib.md5(text[:50].encode()).hexdigest()[:8]}"
        
        if self.db_type == "pinecone":
            try:
                start_time = time.time()
                
                self.pinecone_index.upsert(
                    vectors=[
                        {
                            "id": vector_id,
                            "values": vector,
                            "metadata": {
                                "text": text[:1000],  # Limitar longitud para metadatos
                                "source_type": source_type,
                                "conversation_id": conversation_id,
                                "folder_id": folder_id,
                                "mood_id": mood_id,
                                **(metadata or {})
                            }
                        }
                    ]
                )
                
                VECTOR_DB_LATENCY.labels(db_type="pinecone").observe(time.time() - start_time)
                logger.debug(f"Stored vector in Pinecone: {vector_id}")
            except Exception as e:
                logger.error(f"Error storing vector in Pinecone: {e}")
                raise
                
        elif self.db_type == "pgvector":
            try:
                start_time = time.time()
                
                session = self.db_session()
                embedding = VectorEmbedding(
                    id=vector_id,
                    text=text,
                    vector=vector,
                    source_type=source_type,
                    conversation_id=conversation_id,
                    folder_id=folder_id,
                    mood_id=mood_id,
                    metadata=metadata or {}
                )
                session.add(embedding)
                session.commit()
                session.close()
                
                VECTOR_DB_LATENCY.labels(db_type="pgvector").observe(time.time() - start_time)
                logger.debug(f"Stored vector in pgvector: {vector_id}")
            except Exception as e:
                logger.error(f"Error storing vector in pgvector: {e}")
                raise
        else:
            # Modo simulado - no hace nada pero registra
            logger.debug(f"Mock storage of vector: {vector_id}")
        
        return vector_id
    
    async def retrieve_similar_vectors(
        self, 
        query_embedding: List[float],
        folder_id: Optional[str] = None,
        conversation_id: Optional[str] = None,
        mood_id: Optional[str] = None,
        min_similarity: float = 0.7,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Recupera vectores similares al embedding de consulta
        
        En producción, esto consultaría una base de datos vectorial como Pinecone, Milvus o pgvector
        """
        start_time = time.time()
        
        if self.db_type == "pinecone":
            try:
                # Construir filtro para Pinecone
                filter_dict = {}
                if folder_id:
                    filter_dict["folder_id"] = {"$eq": folder_id}
                if conversation_id:
                    filter_dict["conversation_id"] = {"$eq": conversation_id}
                if mood_id:
                    filter_dict["mood_id"] = {"$eq": mood_id}
                
                # Realizar consulta a Pinecone
                query_response = self.pinecone_index.query(
                    vector=query_embedding,
                    top_k=limit,
                    include_metadata=True,
                    filter=filter_dict if filter_dict else None
                )
                
                VECTOR_DB_LATENCY.labels(db_type="pinecone").observe(time.time() - start_time)
                
                # Formatear resultados
                results = []
                for match in query_response.matches:
                    if match.score >= min_similarity:
                        results.append({
                            "id": match.id,
                            "similarity": match.score,
                            "content": match.metadata.get("text", ""),
                            "metadata": {
                                "source_type": match.metadata.get("source_type", "unknown"),
                                "conversation_id": match.metadata.get("conversation_id"),
                                "folder_id": match.metadata.get("folder_id"),
                                "mood_id": match.metadata.get("mood_id"),
                                "timestamp": match.metadata.get("timestamp", datetime.now().isoformat())
                            }
                        })
                
                return results
                
            except Exception as e:
                logger.error(f"Error querying Pinecone: {e}")
                # Caer en implementación simulada si falla
        
        elif self.db_type == "pgvector":
            try:
                session = self.db_session()
                
                # Construir consulta SQL con pgvector
                query = session.query(VectorEmbedding)
                
                # Aplicar filtros
                if folder_id:
                    query = query.filter(VectorEmbedding.folder_id == folder_id)
                if conversation_id:
                    query = query.filter(VectorEmbedding.conversation_id == conversation_id)
                if mood_id:
                    query = query.filter(VectorEmbedding.mood_id == mood_id)
                
                # Ordenar por similitud de coseno (usando la función <=> de pgvector)
                # Nota: En SQL real sería: ORDER BY embedding <=> $1 LIMIT $2
                # Aquí usamos una aproximación simplificada
                results_raw = query.all()
                
                # Calcular similitudes manualmente
                results_with_sim = []
                for embedding in results_raw:
                    sim = self.cosine_similarity(query_embedding, embedding.vector)
                    if sim >= min_similarity:
                        results_with_sim.append((embedding, sim))
                
                # Ordenar por similitud (mayor primero) y limitar resultados
                results_with_sim.sort(key=lambda x: x[1], reverse=True)
                results_with_sim = results_with_sim[:limit]
                
                VECTOR_DB_LATENCY.labels(db_type="pgvector").observe(time.time() - start_time)
                
                # Formatear resultados
                results = []
                for embedding, sim in results_with_sim:
                    results.append({
                        "id": embedding.id,
                        "similarity": sim,
                        "content": embedding.text,
                        "metadata": {
                            "source_type": embedding.source_type,
                            "conversation_id": embedding.conversation_id,
                            "folder_id": embedding.folder_id,
                            "mood_id": embedding.mood_id,
                            "timestamp": embedding.created_at.isoformat(),
                            **(embedding.metadata or {})
                        }
                    })
                
                session.close()
                return results
                
            except Exception as e:
                logger.error(f"Error querying pgvector: {e}")
                # Caer en implementación simulada si falla
        
        # Implementación simulada con resultados simulados
        logger.debug("Using mock vector retrieval")
        results = []
        
        # Simular 10 resultados con puntuaciones de similitud variables
        for i in range(limit):
            mock_vector = self._get_mock_embedding()
            sim_score = self.cosine_similarity(query_embedding, mock_vector)
            
            # Solo incluir resultados por encima del umbral mínimo de similitud
            if sim_score >= min_similarity:
                results.append({
                    "id": f"vector_{i}",
                    "similarity": sim_score,
                    "content": f"Este es un contenido de memoria simulado para el resultado {i}.",
                    "metadata": {
                        "source_type": "memory_layer" if i % 3 == 0 else "message",
                        "timestamp": datetime.now().isoformat(),
                        "folder_id": folder_id or "default_folder",
                        "conversation_id": conversation_id,
                        "mood_id": mood_id,
                        "tags": ["aerospace", "documentation", "technical"] 
                    }
                })
        
        # Ordenar por puntuación de similitud (mayor primero)
        results.sort(key=lambda x: x["similarity"], reverse=True)
        return results

# Clase para la generación aumentada por recuperación (RAG)
class RAGProcessor:
    def __init__(self):
        self.xai_api_key = os.environ.get("reciprocity_XAI_API_KEY", "")
        self.llm_model = os.environ.get("LLM_MODEL", "gpt-4o")
        self.openai_api_key = os.environ.get("OPENAI_API_KEY", "")
        logger.info(f"Initialized RAG processor with model: {self.llm_model}")
        
    async def generate_response(self, request: RAGRequest) -> RAGResponse:
        """
        Genera una respuesta utilizando RAG (Retrieval-Augmented Generation)
        
        Args:
            request: Solicitud RAG con consulta y resultados de contexto
            
        Returns:
            RAGResponse: Respuesta generada con fuentes y uso de tokens
        """
        start_time = time.time()
        trace_id = f"rag_{int(time.time())}_{hashlib.md5(request.query.encode()).hexdigest()[:8]}"
        
        # Preparar el contexto a partir de los resultados recuperados
        context_text = self._prepare_context(request.context_results)
        
        # Construir el prompt para el LLM
        prompt = f"""
        Consulta: {request.query}
        
        Contexto relevante:
        {context_text}
        
        Instrucciones: Responde a la consulta utilizando la información proporcionada en el contexto.
        Cita las fuentes cuando sea apropiado. Si la información en el contexto no es suficiente,
        indica qué información adicional sería necesaria.
        """
        
        # Generar respuesta utilizando el LLM
        try:
            if self.openai_api_key:
                # Usar OpenAI
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        "https://api.openai.com/v1/chat/completions",
                        headers={
                            "Authorization": f"Bearer {self.openai_api_key}",
                            "Content-Type": "application/json"
                        },
                        json={
                            "model": self.llm_model,
                            "messages": [
                                {"role": "system", "content": "Eres un asistente especializado en COAFI que proporciona respuestas precisas basadas en el contexto proporcionado."},
                                {"role": "user", "content": prompt}
                            ],
                            "temperature": request.temperature,
                            "max_tokens": request.max_tokens
                        },
                        timeout=30.0
                    )
                    
                    if response.status_code != 200:
                        raise Exception(f"Error de API OpenAI: {response.status_code} - {response.text}")
                    
                    result = response.json()
                    generated_text = result["choices"][0]["message"]["content"]
                    token_usage = result["usage"]
            else:
                # Respuesta simulada para pruebas
                generated_text = f"Respuesta simulada para: {request.query}\n\nBasado en el contexto proporcionado, puedo inferir que...\n\nFuentes: [1], [2]"
                token_usage = {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150}
                
            # Extraer fuentes utilizadas
            sources = self._extract_sources(request.context_results, generated_text)
            
            return RAGResponse(
                generated_text=generated_text,
                sources=sources,
                token_usage=token_usage,
                processing_time=time.time() - start_time,
                trace_id=trace_id,
                validationScore=self._calculate_validation_score(request.context_results)
            )
            
        except Exception as e:
            logger.error(f"Error en generación RAG: {e}")
            # Proporcionar respuesta de fallback
            return RAGResponse(
                generated_text=f"Lo siento, no pude generar una respuesta debido a un error: {str(e)}",
                sources=[],
                token_usage={"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
                processing_time=time.time() - start_time,
                trace_id=trace_id,
                validationScore=None
            )
    
    def _prepare_context(self, results: List[RetrievalResult]) -> str:
        """Prepara el texto de contexto a partir de los resultados recuperados"""
        context_parts = []
        
        for i, result in enumerate(results):
            # Formatear cada resultado como una sección numerada
            context_parts.append(f"[{i+1}] {result.content}")
        
        return "\n\n".join(context_parts)
    
    def _extract_sources(self, results: List[RetrievalResult], generated_text: str) -> List[Dict[str, Any]]:
        """Extrae las fuentes utilizadas en la respuesta generada"""
        sources = []
        
        # Buscar referencias a fuentes en el texto generado
        # Formato típico: [1], [2], etc.
        for i, result in enumerate(results):
            source_marker = f"[{i+1}]"
            if source_marker in generated_text:
                sources.append({
                    "id": result.id,
                    "content_snippet": result.content[:100] + "..." if len(result.content) > 100 else result.content,
                    "source_type": result.source_type,
                    "metadata": result.metadata
                })
        
        return sources

    def _calculate_validation_score(self, results: List[RetrievalResult]) -> float:
        """Calcula un puntaje de validación basado en los resultados recuperados"""
        if not results:
            return 0.0
        
        # Ejemplo simple: promedio de las puntuaciones de similitud
        total_score = sum(result.similarity_score for result in results)
        return total_score / len(results)

# Clase adaptadora para el sistema de memoria
class MemoryAdapter:
    """Adaptador para conectar con el sistema de gestión de memoria"""
    
    def __init__(self):
        self.vector_ops = VectorOperations()
        self.access_control = AccessControl()
        self.rag_processor = RAGProcessor()
        self.fastapi_url = os.environ.get("FASTAPI_URL", "http://localhost:8000")
        self.port = os.environ.get("PORT", "3000")
        logger.info(f"Initialized Memory Adapter with FastAPI URL: {self.fastapi_url}")
    
    async def query_semantic_memory(
        self, 
        request: SemanticQueryRequest,
        trace_id: str
    ) -> SemanticQueryResponse:
        """Consulta la memoria semántica con los parámetros dados"""
        start_time = time.time()
        cache_hit = False
        
        # Verificar acceso
        if not self.access_control.check_access(
            "read",
            mood_id=request.mood_id,
            conversation_id=request.conversation_id,
            folder_id=request.folder_id,
            token=request.gaia_token
        ):
            raise HTTPException(
                status_code=403,
                detail="Acceso denegado. No tienes permisos para acceder a estos recursos."
            )
        
        # Determinar estrategia de caché
        use_cache = request.cache_strategy != "none"
        
        # Obtener embedding para la consulta
        query_embedding = await self.vector_ops.get_embedding(
            request.query, 
            mood_id=request.mood_id,
            use_cache=use_cache
        )
        
        # Recuperar vectores similares
        similar_vectors = await self.vector_ops.retrieve_similar_vectors(
            query_embedding,
            folder_id=request.folder_id,
            conversation_id=request.conversation_id,
            mood_id=request.mood_id,
            min_similarity=request.min_similarity,
            limit=20  # Obtener más de los necesarios para filtrar y procesar
        )
        
        # Procesar y formatear resultados
        results = []
        token_count = 0
        
        for item in similar_vectors:
            # Estimar recuento de tokens (aproximación simple)
            item_tokens = len(item["content"].split()) * 1.3
            
            # Verificar si añadir esto excedería el límite de tokens
            if token_count + item_tokens > request.token_limit:
                break
                
            # Convertir a modelo RetrievalResult
            result = RetrievalResult(
                id=item["id"],
                content=item["content"],
                similarity_score=item["similarity"],
                source_type=item["metadata"]["source_type"],
                metadata=item["metadata"],
                token_count=int(item_tokens)
            )
            
            results.append(result)
            token_count += item_tokens
        
        # Calcular tiempo de procesamiento
        processing_time = time.time() - start_time
        
        # Registrar métricas
        QUERY_COUNTER.labels(
            mood_id=request.mood_id or "none",
            cache_hit=str(cache_hit)
        ).inc()
        
        QUERY_LATENCY.labels(
            mood_id=request.mood_id or "none",
            cache_hit=str(cache_hit)
        ).observe(processing_time)
        
        TOKEN_USAGE.labels(
            mood_id=request.mood_id or "none"
        ).inc(token_count)
        
        # Registrar la consulta en la base de datos
        self._log_query(
            query_text=request.query,
            mood_id=request.mood_id,
            conversation_id=request.conversation_id,
            folder_id=request.folder_id,
            token_count=token_count,
            result_count=len(results),
            processing_time=processing_time,
            cache_hit=cache_hit,
            trace_id=trace_id
        )
        
        return SemanticQueryResponse(
            results=results,
            total_results=len(results),
            token_count=int(token_count),
            processing_time=processing_time,
            query_embedding_dimension=self.vector_ops.vector_dimension,
            cache_hit=cache_hit,
            trace_id=trace_id,
            validationScore=self._calculate_validation_score(results)
        )
    
    async def generate_rag_response(self, request: RAGRequest) -> RAGResponse:
        """Genera una respuesta utilizando RAG"""
        return await self.rag_processor.generate_response(request)
    
    def _log_query(
        self,
        query_text: str,
        mood_id: Optional[str],
        conversation_id: Optional[str],
        folder_id: Optional[str],
        token_count: int,
        result_count: int,
        processing_time: float,
        cache_hit: bool,
        trace_id: str,
        user_id: Optional[str] = None
    ) -> None:
        """Registra una consulta en la base de datos para análisis"""
        try:
            # En una implementación real, esto guardaría en la base de datos
            # Aquí solo registramos en el log
            logger.info(
                f"Query log: trace_id={trace_id}, query='{query_text[:30]}...', "
                f"mood_id={mood_id}, tokens={token_count}, results={result_count}, "
                f"time={processing_time:.3f}s, cache_hit={cache_hit}"
            )
        except Exception as e:
            logger.error(f"Error logging query: {e}")

    async def generate_documentation(self, metadata: Dict[str, Any]) -> str:
        """
        Genera documentación a partir de metadatos (e.g., @program, @version)
        
        Args:
            metadata: Diccionario de metadatos
            
        Returns:
            str: Documentación generada
        """
        # Placeholder implementation
        # In a real implementation, this would generate documentation based on metadata
        return "Generated documentation based on metadata."

    async def commit_changes(self, files: List[str], message: str) -> str:
        """
        Commit changes to IDX, CHANGELOG.md, or README.md
        
        Args:
            files: List of files to commit
            message: Commit message
            
        Returns:
            Status message indicating the result of the commit
        """
        # Placeholder implementation
        # In a real implementation, this would commit changes to the specified files
        return f"Changes committed to {', '.join(files)} with message: {message}"

    async def trigger_semantic_audits(self) -> str:
        """
        Trigger semantic audits or PET-CORE scoring pipelines after push events
        
        Returns:
            Status message indicating the result of the trigger
        """
        # Placeholder implementation
        # In a real implementation, this would trigger semantic audits or PET-CORE scoring pipelines
        return "Semantic audits and PET-CORE scoring pipelines triggered."

    async def execute_phi_mode(self, request: dict) -> dict:
        """
        Execute ϕ-mode logic
        
        Args:
            request: Request data for ϕ-mode execution
            
        Returns:
            Response data indicating the result of the ϕ-mode execution
        """
        # Placeholder implementation for ϕ-mode execution logic
        return {
            "request": request,
            "status": "ϕ-mode executed"
        }

    async def execute_ethical_promptimization(self, request: dict) -> dict:
        """
        Execute promptimización ético-paramétrica logic
        
        Args:
            request: Request data for promptimización ético-paramétrica
            
        Returns:
            Response data indicating the result of the promptimización ético-paramétrica
        """
        # Placeholder implementation for promptimización ético-paramétrica
        return {
            "request": request,
            "status": "promptimización ético-paramétrica executed"
        }

# Middleware para generar trace_id
async def add_trace_id(request: Request, call_next):
    """Middleware para añadir trace_id a cada solicitud"""
    trace_id = f"trace_{int(time.time())}_{hashlib.md5(str(request.url).encode()).hexdigest()[:8]}"
    request.state.trace_id = trace_id
    
    # Añadir trace_id a los headers de respuesta
    response = await call_next(request)
    response.headers["X-Trace-ID"] = trace_id
    
    return response

# Middleware para verificar token GAIA
async def verify_gaia_token(request: Request, call_next):
    """Middleware para verificar token GAIA en solicitudes protegidas"""
    # Rutas que requieren autenticación
    protected_routes = [
        "/semantic-query/protected",
        "/rag/protected"
    ]
    
    # Verificar si la ruta actual está protegida
    path = request.url.path
    if any(path.startswith(route) for route in protected_routes):
        # Obtener token del header
        token = request.headers.get("X-GAIA-Token")
        if not token:
            return JSONResponse(
                status_code=401,
                content={"detail": "Se requiere token GAIA para acceder a esta ruta"}
            )
        
        # Verificar token
        access_control = AccessControl()
        try:
            access_control.validate_token(token)
        except ValueError as e:
            return JSONResponse(
                status_code=403,
                content={"detail": str(e)}
            )
    
    return await call_next(request)

# Crear router
memory_router = APIRouter(prefix="/semantic-query", tags=["memory"])
rag_router = APIRouter(prefix="/rag", tags=["rag"])

# Instancia singleton
memory_adapter = MemoryAdapter()

@memory_router.post("/", response_model=SemanticQueryResponse)
async def semantic_query(request: SemanticQueryRequest, trace_id: str = None):
    """
    Consulta la memoria semántica basada en similitud de texto
    
    Este endpoint recupera contenido semánticamente similar del sistema de memoria
    basado en la consulta y parámetros proporcionados.
    """
    if not trace_id:
        trace_id = f"query_{int(time.time())}_{hashlib.md5(request.query.encode()).hexdigest()[:8]}"
        
    try:
        return await memory_adapter.query_semantic_memory(request, trace_id)
    except Exception as e:
        logger.error(f"Error en consulta semántica: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@memory_router.post("/protected", response_model=SemanticQueryResponse)
async def protected_semantic_query(
    request: SemanticQueryRequest,
    x_gaia_token: str = Header(None, alias="X-GAIA-Token")
):
    """Endpoint protegido que requiere token GAIA"""
    # El token ya fue verificado por el middleware
    request.gaia_token = x_gaia_token
    trace_id = f"protected_{int(time.time())}_{hashlib.md5(request.query.encode()).hexdigest()[:8]}"
    
    try:
        return await memory_adapter.query_semantic_memory(request, trace_id)
    except Exception as e:
        logger.error(f"Error en consulta semántica protegida: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@rag_router.post("/", response_model=RAGResponse)
async def generate_rag(request: RAGRequest):
    """
    Genera una respuesta utilizando RAG (Retrieval-Augmented Generation)
    
    Este endpoint utiliza los resultados de contexto recuperados para generar
    una respuesta coherente a la consulta del usuario.
    """
    try:
        return await memory_adapter.generate_rag_response(request)
    except Exception as e:
        logger.error(f"Error en generación RAG: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@memory_router.get("/stats", tags=["monitoring"])
async def get_memory_stats():
    """Obtiene estadísticas del sistema de memoria"""
    cache_stats = memory_adapter.vector_ops.embedding_cache.get_stats()
    
    return {
        "cache": cache_stats,
        "vector_db": {
            "type": memory_adapter.vector_ops.db_type,
            "dimension": memory_adapter.vector_ops.vector_dimension
        },
        "metrics": {
            "queries_total": sum(v for k, v in QUERY_COUNTER._metrics.items()),
            "token_usage_total": sum(v for k, v in TOKEN_USAGE._metrics.items()),
            "avg_latency": sum(v for k, v in QUERY_LATENCY._metrics.items()) / max(1, len(QUERY_LATENCY._metrics))
        }
    }

# Interfaz de línea de comandos para pruebas
if __name__ == "__main__":
    import asyncio
    import argparse
    
    parser = argparse.ArgumentParser(description="Probar semantic retrieval bridge")
    parser.add_argument("--query", type=str, required=True, help="Texto de consulta a buscar")
    parser.add_argument("--folder", type=str, help="ID de carpeta opcional para buscar dentro")
    parser.add_argument("--mood", type=str, help="ID de mood opcional para contextualizar la búsqueda")
    parser.add_argument("--limit", type=int, default=1000, help="Límite de tokens para resultados")
    parser.add_argument("--rag", action="store_true", help="Generar respuesta RAG con los resultados")
    args = parser.parse_args()
    
    async def run_test():
        adapter = MemoryAdapter()
        trace_id = f"cli_{int(time.time())}"
        
        request = SemanticQueryRequest(
            query=args.query,
            folder_id=args.folder,
            mood_id=args.mood,
            token_limit=args.limit
        )
        
        print(f"Consultando: '{args.query}'")
        response = await adapter.query_semantic_memory(request, trace_id)
        print(f"Encontrados {response.total_results} resultados ({response.token_count} tokens) en {response.processing_time:.3f}s")
        
        for i, result in enumerate(response.results):
            print(f"\n--- Resultado {i+1} (similitud: {result.similarity_score:.3f}) ---")
            print(f"Tipo: {result.source_type}")
            print(f"Contenido: {result.content[:200]}...")
        
        if args.rag && response.results:
            print("\n=== Generando respuesta RAG ===")
            rag_request = RAGRequest(
                query=args.query,
                context_results=response.results,
                mood_id=args.mood
            )
            
            rag_response = await adapter.generate_rag_response(rag_request)
            print(f"\nRespuesta generada ({rag_response.token_usage.get('total_tokens', 0)} tokens):")
            print(rag_response.generated_text)
            
            if rag_response.sources:
                print("\nFuentes utilizadas:")
                for source in rag_response.sources:
                    print(f"- {source['content_snippet']}")
    
    asyncio.run(run_test())
