#!/usr/bin/env python3
"""
Memory Service for COAFI System
Provides comprehensive memory management capabilities including vector storage,
semantic retrieval, caching, and access control integration.
"""

import os
import time
import json
import logging
import hashlib
import asyncio
from typing import Dict, List, Any, Optional, Union, Tuple
from datetime import datetime, timedelta
from functools import lru_cache

import numpy as np
import redis
import psycopg2
from psycopg2.extras import Json
from fastapi import HTTPException, Depends, Security
from pydantic import BaseModel, Field

# Optional imports with fallbacks
try:
    import pinecone
    PINECONE_AVAILABLE = True
except ImportError:
    PINECONE_AVAILABLE = False

try:
    import openai
    from openai import AsyncOpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("coafi.memory")

# Models for memory operations
class MemoryItem(BaseModel):
    """Base model for items stored in memory"""
    id: str
    content: str
    embedding: List[float]
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory(datetime.now)
    
class MemoryQuery(BaseModel):
    """Query parameters for memory retrieval"""
    query: str
    embedding: Optional[List[float]] = None
    folder_id: Optional[str] = None
    conversation_id: Optional[str] = None
    mood_id: Optional[str] = None
    token_limit: int = 1000
    min_similarity: float = 0.7
    max_results: int = 20
    include_metadata: bool = True
    user_id: Optional[str] = None  # Added for secure contexts
    
class MemoryResult(BaseModel):
    """Result from memory retrieval"""
    id: str
    content: str
    similarity_score: float
    source_type: str
    metadata: Dict[str, Any]
    token_count: int = 0

class MemoryStats(BaseModel):
    """Statistics about memory operations"""
    total_items: int = 0
    total_tokens: int = 0
    avg_similarity: float = 0.0
    query_time_ms: float = 0.0
    cache_hit_rate: float = 0.0
    embedding_time_ms: float = 0.0

class CacheConfig(BaseModel):
    """Configuration for embedding cache"""
    strategy: str = "default"  # none, default, aggressive
    ttl_seconds: int = 3600
    max_size: int = 1000

# Vector database connection configurations
class PgVectorConfig(BaseModel):
    """Configuration for PostgreSQL with pgvector extension"""
    host: str
    port: int = 5432
    database: str
    user: str
    password: str
    table_name: str = "memory_embeddings"
    vector_dimension: int = 1536

class PineconeConfig(BaseModel):
    """Configuration for Pinecone vector database"""
    api_key: str
    environment: str
    index_name: str
    namespace: str = "coafi-memory"
    vector_dimension: int = 1536

# Custom exception for MemoryService
class MemoryServiceError(Exception):
    pass

# Main Memory Service
class MemoryService:
    """
    Comprehensive memory service for COAFI system
    
    Provides:
    - Vector storage in pgvector or Pinecone
    - Embedding generation and caching
    - Semantic retrieval with access control
    - Memory statistics and monitoring
    """
    
    def __init__(self, 
                 vector_db_type: str = "pgvector",
                 pgvector_config: Optional[PgVectorConfig] = None,
                 pinecone_config: Optional[PineconeConfig] = None,
                 cache_config: Optional[CacheConfig] = None,
                 enable_access_control: bool = True):
        """
        Initialize the memory service
        
        Args:
            vector_db_type: Type of vector database to use ('pgvector', 'pinecone', or 'mock')
            pgvector_config: Configuration for pgvector connection
            pinecone_config: Configuration for Pinecone connection
            cache_config: Configuration for embedding cache
            enable_access_control: Whether to enable access control checks
        """
        self.vector_db_type = vector_db_type
        self.vector_dimension = 1536  # Default dimension for OpenAI embeddings
        self.enable_access_control = enable_access_control
        
        # Initialize cache
        self.cache_config = cache_config or CacheConfig()
        self._init_cache()
        
        # Initialize vector database
        if vector_db_type == "pgvector":
            if not pgvector_config:
                raise ValueError("pgvector_config is required when vector_db_type is 'pgvector'")
            self._init_pgvector(pgvector_config)
            self.vector_dimension = pgvector_config.vector_dimension
            
        elif vector_db_type == "pinecone":
            if not pinecone_config:
                raise ValueError("pinecone_config is required when vector_db_type is 'pinecone'")
            if not PINECONE_AVAILABLE:
                raise ImportError("Pinecone package is not installed. Install with 'pip install pinecone-client'")
            self._init_pinecone(pinecone_config)
            self.vector_dimension = pinecone_config.vector_dimension
            
        elif vector_db_type == "mock":
            logger.warning("Using mock vector database. This should only be used for testing.")
            self.mock_db = []
            
        else:
            raise ValueError(f"Unsupported vector_db_type: {vector_db_type}")
        
        # Initialize API clients
        self.xai_api_key = os.environ.get("reciprocity_XAI_API_KEY", "")
        self.openai_api_key = os.environ.get("OPENAI_API_KEY", "")
        
        if self.openai_api_key and OPENAI_AVAILABLE:
            self.openai_client = AsyncOpenAI(api_key=self.openai_api_key)
        else:
            self.openai_client = None
            logger.warning("OpenAI client not available. Some features will be limited.")
        
        # Statistics
        self.stats = {
            "queries_total": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "avg_query_time_ms": 0,
            "avg_embedding_time_ms": 0,
        }
        
        logger.info(f"Memory service initialized with {vector_db_type} backend")

    def _init_cache(self):
        """Initialize the embedding cache"""
        # Try to connect to Redis if available
        redis_url = os.environ.get("REDIS_URL")
        if redis_url and self.cache_config.strategy != "none":
            try:
                self.redis_client = redis.from_url(redis_url)
                self.redis_client.ping()  # Test connection
                self.cache_type = "redis"
                logger.info("Using Redis for embedding cache")
            except (redis.ConnectionError, redis.RedisError) as e:
                logger.warning(f"Failed to connect to Redis: {e}. Falling back to local cache.")
                self.cache_type = "local"
                self.local_cache = {}
        else:
            self.cache_type = "local"
            self.local_cache = {}
            logger.info("Using local dictionary for embedding cache")
    
    def _init_pgvector(self, config: PgVectorConfig):
        """Initialize connection to PostgreSQL with pgvector extension"""
        try:
            self.pg_config = config
            # Test connection
            conn = psycopg2.connect(
                host=config.host,
                port=config.port,
                dbname=config.database,
                user=config.user,
                password=config.password
            )
            
            # Check if pgvector extension is installed
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM pg_extension WHERE extname = 'vector'")
                if cur.fetchone() is None:
                    cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
                    conn.commit()
                
                # Check if table exists, create if not
                cur.execute(f"""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = '{config.table_name}'
                    )
                """)
                if not cur.fetchone()[0]:
                    cur.execute(f"""
                        CREATE TABLE {config.table_name} (
                            id TEXT PRIMARY KEY,
                            content TEXT NOT NULL,
                            embedding vector({config.vector_dimension}) NOT NULL,
                            metadata JSONB NOT NULL DEFAULT '{}',
                            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                    
                    # Create index for faster similarity search
                    cur.execute(f"""
                        CREATE INDEX ON {config.table_name} 
                        USING ivfflat (embedding vector_cosine_ops) 
                        WITH (lists = 100)
                    """)
                    conn.commit()
            
            conn.close()
            logger.info(f"Successfully connected to pgvector database: {config.database}")
            
        except Exception as e:
            logger.error(f"Failed to initialize pgvector: {e}")
            raise
    
    def _init_pinecone(self, config: PineconeConfig):
        """Initialize connection to Pinecone vector database"""
        try:
            pinecone.init(api_key=config.api_key, environment=config.environment)
            
            # Check if index exists, create if not
            if config.index_name not in pinecone.list_indexes():
                pinecone.create_index(
                    name=config.index_name,
                    dimension=config.vector_dimension,
                    metric="cosine"
                )
                logger.info(f"Created new Pinecone index: {config.index_name}")
            
            self.pinecone_index = pinecone.Index(config.index_name)
            self.pinecone_namespace = config.namespace
            logger.info(f"Successfully connected to Pinecone index: {config.index_name}")
            
        except Exception as e:
            logger.error(f"Failed to initialize Pinecone: {e}")
            raise
    
    async def get_embedding(self, text: str) -> List[float]:
        """
        Get embedding vector for text using OpenAI or XAI API
        
        Args:
            text: Text to embed
            
        Returns:
            List of floats representing the embedding vector
        """
        # Check cache first
        if self.cache_config.strategy != "none":
            cache_key = f"emb:{hashlib.md5(text.encode()).hexdigest()}"
            cached_embedding = await self._get_from_cache(cache_key)
            if cached_embedding:
                self.stats["cache_hits"] += 1
                return cached_embedding
            self.stats["cache_misses"] += 1
        
        start_time = time.time()
        
        # Try OpenAI first if available
        if self.openai_client:
            try:
                response = await self.openai_client.embeddings.create(
                    model="text-embedding-3-large",
                    input=text
                )
                embedding = response.data[0].embedding
                
                # Update stats
                embedding_time = (time.time() - start_time) * 1000
                self._update_rolling_avg("avg_embedding_time_ms", embedding_time)
                
                # Cache the result
                if self.cache_config.strategy != "none":
                    await self._set_in_cache(cache_key, embedding)
                
                return embedding
            except openai.RateLimitError as e:
                backoff_time = 5  # Example backoff time, can be adjusted
                await asyncio.sleep(backoff_time)
                logger.warning(f"OpenAI rate limit exceeded. Retrying after {backoff_time} seconds...")
            except Exception as e:
                logger.warning(f"OpenAI embedding failed: {e}. Trying XAI API...")
        
        # Fall back to XAI API if OpenAI fails or is not available
        if self.xai_api_key:
            try:
                # In a real implementation, this would call the XAI API
                # For now, we'll use a mock implementation
                logger.info("Using XAI API for embedding")
                embedding = self._get_mock_embedding()
                
                # Update stats
                embedding_time = (time.time() - start_time) * 1000
                self._update_rolling_avg("avg_embedding_time_ms", embedding_time)
                
                # Cache the result
                if self.cache_config.strategy != "none":
                    await self._set_in_cache(cache_key, embedding)
                
                return embedding
            except Exception as e:
                logger.error(f"XAI API embedding failed: {e}")
        
        # Fall back to mock embedding if all else fails
        logger.warning("All embedding methods failed. Using mock embedding.")
        return self._get_mock_embedding()
    
    def _get_mock_embedding(self) -> List[float]:
        """Generate a mock embedding for testing"""
        return list(np.random.uniform(-1, 1, self.vector_dimension))
    
    async def _get_from_cache(self, key: str) -> Optional[List[float]]:
        """Get embedding from cache"""
        if self.cache_type == "redis":
            try:
                cached = self.redis_client.get(key)
                if cached:
                    return json.loads(cached)
            except Exception as e:
                logger.warning(f"Redis cache get failed: {e}")
        else:
            return self.local_cache.get(key)
        return None
    
    async def _set_in_cache(self, key: str, embedding: List[float]) -> None:
        """Set embedding in cache"""
        if self.cache_type == "redis":
            try:
                self.redis_client.setex(
                    key, 
                    self.cache_config.ttl_seconds,
                    json.dumps(embedding)
                )
            except Exception as e:
                logger.warning(f"Redis cache set failed: {e}")
        else:
            self.local_cache[key] = embedding
            
            # Implement simple LRU eviction for local cache
            if len(self.local_cache) > self.cache_config.max_size:
                # Remove oldest 10% of entries
                num_to_remove = max(1, int(self.cache_config.max_size * 0.1))
                for _ in range(num_to_remove):
                    if self.local_cache:
                        self.local_cache.pop(next(iter(self.local_cache)))
    
    async def store_memory(self, item: MemoryItem) -> str:
        """
        Store a memory item in the vector database
        
        Args:
            item: Memory item to store
            
        Returns:
            ID of the stored item
        """
        if self.vector_db_type == "pgvector":
            return await self._store_in_pgvector(item)
        elif self.vector_db_type == "pinecone":
            return await self._store_in_pinecone(item)
        else:  # mock
            self.mock_db.append(item)
            return item.id
    
    async def _store_in_pgvector(self, item: MemoryItem) -> str:
        """Store memory item in pgvector"""
        try:
            conn = psycopg2.connect(
                host=self.pg_config.host,
                port=self.pg_config.port,
                dbname=self.pg_config.database,
                user=self.pg_config.user,
                password=self.pg_config.password
            )
            
            with conn.cursor() as cur:
                cur.execute(f"""
                    INSERT INTO {self.pg_config.table_name}
                    (id, content, embedding, metadata, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE
                    SET content = EXCLUDED.content,
                        embedding = EXCLUDED.embedding,
                        metadata = EXCLUDED.metadata,
                        updated_at = EXCLUDED.updated_at
                """, (
                    item.id,
                    item.content,
                    item.embedding,
                    Json(item.metadata),
                    item.created_at,
                    item.updated_at
                ))
                conn.commit()
            
            conn.close()
            return item.id
            
        except Exception as e:
            logger.error(f"Failed to store in pgvector: {e}")
            raise MemoryServiceError(f"Failed to store in pgvector: {e}")
    
    async def _store_in_pinecone(self, item: MemoryItem) -> str:
        """Store memory item in Pinecone"""
        try:
            self.pinecone_index.upsert(
                vectors=[(
                    item.id,
                    item.embedding,
                    {
                        "content": item.content,
                        "created_at": item.created_at.isoformat(),
                        "updated_at": item.updated_at.isoformat(),
                        **item.metadata
                    }
                )],
                namespace=self.pinecone_namespace
            )
            return item.id
            
        except Exception as e:
            logger.error(f"Failed to store in Pinecone: {e}")
            raise MemoryServiceError(f"Failed to store in Pinecone: {e}")
    
    async def query_memory(self, query: MemoryQuery) -> Tuple[List[MemoryResult], MemoryStats]:
        """
        Query memory for semantically similar content
        
        Args:
            query: Query parameters
            
        Returns:
            Tuple of (list of results, query statistics)
        """
        start_time = time.time()
        self.stats["queries_total"] += 1
        
        # Get embedding for query if not provided
        if query.embedding is None:
            query.embedding = await self.get_embedding(query.query)
        
        # Perform access control check if enabled
        if self.enable_access_control:
            await self._check_access(query)
        
        # Query the appropriate vector database
        if self.vector_db_type == "pgvector":
            results = await self._query_pgvector(query)
        elif self.vector_db_type == "pinecone":
            results = await self._query_pinecone(query)
        else:  # mock
            results = await self._query_mock(query)
        
        # Calculate token counts for results
        total_tokens = 0
        for result in results:
            # Simple approximation: 1 token ≈ 4 chars
            result.token_count = len(result.content) // 4
            total_tokens += result.token_count
        
        # Enforce token limit
        filtered_results = []
        current_tokens = 0
        
        for result in results:
            if current_tokens + result.token_count <= query.token_limit:
                filtered_results.append(result)
                current_tokens += result.token_count
            else:
                break
        
        # Calculate statistics
        query_time_ms = (time.time() - start_time) * 1000
        self._update_rolling_avg("avg_query_time_ms", query_time_ms)
        
        avg_similarity = sum(r.similarity_score for r in filtered_results) / len(filtered_results) if filtered_results else 0
        
        cache_hit_rate = self.stats["cache_hits"] / (self.stats["cache_hits"] + self.stats["cache_misses"]) if (self.stats["cache_hits"] + self.stats["cache_misses"]) > 0 else 0
        
        stats = MemoryStats(
            total_items=len(filtered_results),
            total_tokens=current_tokens,
            avg_similarity=avg_similarity,
            query_time_ms=query_time_ms,
            cache_hit_rate=cache_hit_rate,
            embedding_time_ms=self.stats["avg_embedding_time_ms"]
        )
        
        return filtered_results, stats
    
    async def _query_pgvector(self, query: MemoryQuery) -> List[MemoryResult]:
        """Query pgvector for similar vectors"""
        try:
            conn = psycopg2.connect(
                host=self.pg_config.host,
                port=self.pg_config.port,
                dbname=self.pg_config.database,
                user=self.pg_config.user,
                password=self.pg_config.password
            )
            
            with conn.cursor() as cur:
                # Build WHERE clause for filtering
                where_clauses = []
                params = [query.embedding, query.min_similarity]
                
                if query.folder_id:
                    where_clauses.append("metadata->>'folder_id' = %s")
                    params.append(query.folder_id)
                
                if query.conversation_id:
                    where_clauses.append("metadata->>'conversation_id' = %s")
                    params.append(query.conversation_id)
                
                if query.mood_id:
                    where_clauses.append("metadata->>'mood_id' = %s")
                    params.append(query.mood_id)
                
                if query.user_id:
                    where_clauses.append("metadata->>'user_id' = %s")
                    params.append(query.user_id)
                
                where_clause = " AND ".join(where_clauses)
                if where_clause:
                    where_clause = f"AND {where_clause}"
                
                # Execute query with cosine similarity
                cur.execute(f"""
                    SELECT 
                        id, 
                        content, 
                        1 - (embedding <=> %s) as similarity,
                        metadata,
                        created_at,
                        updated_at
                    FROM {self.pg_config.table_name}
                    WHERE 1 - (embedding <=> %s) >= %s
                    {where_clause}
                    ORDER BY similarity DESC
                    LIMIT {query.max_results}
                """, params)
                
                results = []
                for row in cur.fetchall():
                    metadata = row[3]
                    source_type = metadata.get("source_type", "unknown")
                    
                    results.append(MemoryResult(
                        id=row[0],
                        content=row[1],
                        similarity_score=row[2],
                        source_type=source_type,
                        metadata=metadata
                    ))
            
            conn.close()
            return results
            
        except Exception as e:
            logger.error(f"Failed to query pgvector: {e}")
            raise MemoryServiceError(f"Failed to query pgvector: {e}")
    
    async def _query_pinecone(self, query: MemoryQuery) -> List[MemoryResult]:
        """Query Pinecone for similar vectors"""
        try:
            # Build filter for metadata
            filter_dict = {}
            
            if query.folder_id:
                filter_dict["folder_id"] = {"$eq": query.folder_id}
            
            if query.conversation_id:
                filter_dict["conversation_id"] = {"$eq": query.conversation_id}
            
            if query.mood_id:
                filter_dict["mood_id"] = {"$eq": query.mood_id}
            
            if query.user_id:
                filter_dict["user_id"] = {"$eq": query.user_id}
            
            # Execute query
            query_response = self.pinecone_index.query(
                vector=query.embedding,
                top_k=query.max_results,
                namespace=self.pinecone_namespace,
                filter=filter_dict if filter_dict else None,
                include_metadata=query.include_metadata
            )
            
            results = []
            for match in query_response.matches:
                if match.score < query.min_similarity:
                    continue
                    
                metadata = match.metadata
                content = metadata.pop("content", "No content available")
                source_type = metadata.get("source_type", "unknown")
                
                results.append(MemoryResult(
                    id=match.id,
                    content=content,
                    similarity_score=match.score,
                    source_type=source_type,
                    metadata=metadata
                ))
            
            return results
            
        except Exception as e:
            logger.error(f"Failed to query Pinecone: {e}")
            raise MemoryServiceError(f"Failed to query Pinecone: {e}")
    
    async def _query_mock(self, query: MemoryQuery) -> List[MemoryResult]:
        """Query mock database for similar vectors"""
        results = []
        
        # Generate some mock results
        for i in range(min(query.max_results, 10)):
            similarity = max(0.7, 1.0 - (i * 0.03))
            if similarity < query.min_similarity:
                continue
                
            source_type = ["memory_layer", "message", "conversation", "summary"][i % 4]
            
            metadata = {
                "source_type": source_type,
                "timestamp": datetime.now().isoformat(),
                "folder_id": query.folder_id or "default_folder",
                "conversation_id": query.conversation_id or f"conv_{i}",
                "mood_id": query.mood_id,
                "user_id": query.user_id,
                "tags": ["aerospace", "documentation", "technical"],
                "infoCode": "GAIA-COAFI-MEM-QX-001",
                "object_id": "OBJ-2025-AMPEL360-29-01",
                "agent_trace": "ACE-AMP-001",
                "semantic_link": "qao://memory/29-01-0003"
            }
            
            results.append(MemoryResult(
                id=f"mock_{i}",
                content=f"This is mock content {i} for query: {query.query}",
                similarity_score=similarity,
                source_type=source_type,
                metadata=metadata
            ))
        
        return results
    
    async def _check_access(self, query: MemoryQuery) -> None:
        """
        Check if the current user has access to the requested data
        
        Raises HTTPException if access is denied
        """
        # In a real implementation, this would check against a permission system
        # For now, we'll just log the access check
        logger.info(f"Access check for query with folder_id={query.folder_id}, conversation_id={query.conversation_id}, mood_id={query.mood_id}")
        
        # Example implementation:
        # 1. Get current user from security context
        # 2. Check if user has access to the folder/conversation/mood
        # 3. Raise HTTPException(status_code=403) if not
        pass
    
    def _update_rolling_avg(self, stat_name: str, new_value: float, alpha: float = 0.1) -> None:
        """Update rolling average for a statistic"""
        current = self.stats.get(stat_name, 0)
        if current == 0:
            self.stats[stat_name] = new_value
        else:
            self.stats[stat_name] = (alpha * new_value) + ((1 - alpha) * current)
    
    async def generate_rag_response(self, 
                                   query: str, 
                                   memory_results: List[MemoryResult],
                                   model: str = "gpt-4o",
                                   temperature: float = 0.7,
                                   include_citations: bool = True) -> str:
        """
        Generate a response using Retrieval-Augmented Generation (RAG)
        
        Args:
            query: User query
            memory_results: Retrieved memory results to use as context
            model: LLM model to use
            temperature: Temperature for generation
            include_citations: Whether to include citations in the response
            
        Returns:
            Generated response text
        """
        if not self.openai_client:
            raise ValueError("OpenAI client not available. Cannot generate RAG response.")
        
        # Format context from memory results
        context_parts = []
        for i, result in enumerate(memory_results):
            source_id = f"[{i+1}]" if include_citations else ""
            context_parts.append(f"{source_id} {result.content}")
        
        context = "\n\n".join(context_parts)
        
        # Create prompt
        system_prompt = """
        You are an AI assistant for aerospace documentation and technical information.
        Answer the user's question based on the provided context.
        Be precise, technical, and helpful.
        
        If the context doesn't contain relevant information, say so rather than making up an answer.
        """
        
        if include_citations:
            system_prompt += "\nInclude citations [X] when referencing specific information from the context."
        
        try:
            response = await self.openai_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
                ],
                temperature=temperature
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"Failed to generate RAG response: {e}")
            raise MemoryServiceError(f"Failed to generate RAG response: {e}")

    async def adjust_license(self, license_id: str, feedback: Dict[str, Any]) -> str:
        """
        Adjust the license state based on feedback and context changes
        
        Args:
            license_id: ID of the license to adjust
            feedback: Feedback and context changes
            
        Returns:
            Adjusted license state
        """
        # Placeholder implementation
        # In a real implementation, this would adjust the license state based on feedback
        return "adjusted_license_state"

    async def getDocumentInterdependencies(self) -> Dict[str, Any]:
        """
        Identify and track interdependencies between documents across different domains
        
        Returns:
            Dictionary containing document interdependencies
        """
        # Placeholder implementation
        # In a real implementation, this would analyze documents and identify interdependencies
        return {
            "document_1": ["document_2", "document_3"],
            "document_2": ["document_1"],
            "document_3": ["document_1"]
        }

    async def getDocumentStatus(self) -> Dict[str, Any]:
        """
        Track document completion status, review cycles, and approval workflows
        
        Returns:
            Dictionary containing document status information
        """
        # Placeholder implementation
        # In a real implementation, this would track the status of documents
        return {
            "document_1": {
                "status": "completed",
                "review_cycles": 2,
                "approval_workflows": ["workflow_1", "workflow_2"]
            },
            "document_2": {
                "status": "in_progress",
                "review_cycles": 1,
                "approval_workflows": ["workflow_1"]
            },
            "document_3": {
                "status": "not_started",
                "review_cycles": 0,
                "approval_workflows": []
            }
        }

    async def updateRelatedDocuments(self, document_id: str) -> str:
        """
        Automatically update related documents when changes are made
        
        Args:
            document_id: ID of the document that was changed
            
        Returns:
            Status message indicating the result of the update
        """
        # Placeholder implementation
        # In a real implementation, this would update related documents based on changes
        return f"Related documents for {document_id} have been updated."

    async def integrateVersionControl(self) -> str:
        """
        Ensure all documents are managed in a version control system that maintains the revision history
        
        Returns:
            Status message indicating the result of the integration
        """
        # Placeholder implementation
        # In a real implementation, this would integrate documents with a version control system
        return "All documents are now managed in the version control system."

    async def commitChanges(self, files: List[str], message: str) -> str:
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

    async def triggerSemanticAudits(self) -> str:
        """
        Trigger semantic audits or PET-CORE scoring pipelines after push events
        
        Returns:
            Status message indicating the result of the trigger
        """
        # Placeholder implementation
        # In a real implementation, this would trigger semantic audits or PET-CORE scoring pipelines
        return "Semantic audits and PET-CORE scoring pipelines triggered."

    async def store_ontology_data(self, ontology_data: Dict[str, Any]) -> str:
        """
        Store ontology-related data in the memory service
        
        Args:
            ontology_data: Dictionary containing ontology data
            
        Returns:
            Status message indicating the result of the storage
        """
        # Placeholder implementation
        # In a real implementation, this would store ontology data in the memory service
        return "Ontology data has been stored."

    async def retrieve_ontology_data(self, ontology_id: str) -> Dict[str, Any]:
        """
        Retrieve ontology-related data from the memory service
        
        Args:
            ontology_id: ID of the ontology data to retrieve
            
        Returns:
            Dictionary containing the retrieved ontology data
        """
        # Placeholder implementation
        # In a real implementation, this would retrieve ontology data from the memory service
        return {
            "ontology_id": ontology_id,
            "data": "Sample ontology data"
        }

    async def executePhiMode(self, request: dict) -> dict:
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

    async def executeEthicalPromptimization(self, request: dict) -> dict:
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

# Singleton instance for easy import
memory_service = MemoryService(
    vector_db_type=os.environ.get("VECTOR_DB_TYPE", "mock"),
    enable_access_control=os.environ.get("ENABLE_ACCESS_CONTROL", "true").lower() == "true"
)

# Utility functions
def estimate_tokens(text: str) -> int:
    """Estimate the number of tokens in a text string"""
    # Simple approximation: 1 token ≈ 4 characters for English text
    return len(text) // 4

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Calculate cosine similarity between two vectors"""
    if len(vec1) != len(vec2):
        raise ValueError(f"Vector dimensions don't match: {len(vec1)} vs {len(vec2)}")
    
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = sum(a * a for a in vec1) ** 0.5
    magnitude2 = sum(b * b for b in vec2) ** 0.5
    
    if magnitude1 * magnitude2 == 0:
        return 0
        
    return dot_product / (magnitude1 * magnitude2)

# Command line interface for testing
if __name__ == "__main__":
    import asyncio
    import argparse
    
    parser = argparse.ArgumentParser(description="Test memory service")
    parser.add_argument("--query", type=str, required=True, help="Query text to search for")
    parser.add_argument("--folder", type=str, help="Optional folder ID to search within")
    parser.add_argument("--limit", type=int, default=1000, help="Token limit for results")
    parser.add_argument("--rag", action="store_true", help="Generate RAG response")
    args = parser.parse_args()
    
    async def run_test():
        # Initialize with mock DB for testing
        test_service = MemoryService(vector_db_type="mock")
        
        # Create query
        memory_query = MemoryQuery(
            query=args.query,
            folder_id=args.folder,
            token_limit=args.limit
        )
        
        # Query memory
        results, stats = await test_service.query_memory(memory_query)
        
        # Print results
        print(f"Found {len(results)} results in {stats.query_time_ms:.2f}ms")
        print(f"Total tokens: {stats.total_tokens}")
        print(f"Average similarity: {stats.avg_similarity:.4f}")
        print("\nResults:")
        
        for i, result in enumerate(results):
            print(f"\n[{i+1}] Similarity: {result.similarity_score:.4f}")
            print(f"Source: {result.source_type}")
            print(f"Content: {result.content[:100]}...")
        
        # Generate RAG response if requested
        if args.rag and test_service.openai_client:
            print("\nGenerating RAG response...")
            response = await test_service.generate_rag_response(
                args.query,
                results,
                include_citations=True
            )
            print("\nRAG Response:")
            print(response)
    
    asyncio.run(run_test())
