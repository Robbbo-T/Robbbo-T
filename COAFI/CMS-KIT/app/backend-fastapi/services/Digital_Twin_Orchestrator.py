"""
Digital Thread Orchestrator (Versión Mejorada)

Este módulo implementa el componente central que conecta todas las capas
de la arquitectura GAIA AIR, con mejoras en eficiencia, seguridad y manejo de errores.
"""

import asyncio
import json
import logging
import time
import uuid
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import opentelemetry.trace as trace
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from redis.asyncio import Redis
from redis.exceptions import RedisError

# Configuración de logging y telemetría
logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)

# Constantes
MAX_RETRY_ATTEMPTS = 3
EVENT_RETENTION_DAYS = 365  # Retención de eventos por 1 año
CONSUMER_GROUP = "digital_thread_processors"
CONSUMER_NAME = "processor-{hostname}"  # Se reemplazará con el hostname real

class LayerType(str, Enum):
    """Tipos de capas en la arquitectura GAIA AIR."""
    DESIGN = "design"
    PRODUCTION = "production"
    OPERATIONS = "operations"

class EventType(str, Enum):
    """Tipos de eventos en el Digital Thread."""
    DESIGN_CHANGE = "design_change"
    SIMULATION_RESULT = "simulation_result"
    PRODUCTION_START = "production_start"
    QUALITY_CHECK = "quality_check"
    MAINTENANCE_ALERT = "maintenance_alert"
    SUPPLY_CHAIN_UPDATE = "supply_chain_update"
    SUSTAINABILITY_METRIC = "sustainability_metric"
    LIFECYCLE_UPDATE = "lifecycle_update"

class EventStatus(str, Enum):
    """Estados posibles de un evento."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class ThreadEvent(BaseModel):
    """Modelo para eventos en el Digital Thread."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    event_type: EventType
    source_layer: LayerType
    target_layer: Optional[LayerType] = None
    component_id: str
    version_hash: str
    payload: Dict[str, Any]
    metadata: Dict[str, Any] = Field(default_factory=dict)
    parent_event_id: Optional[str] = None
    status: EventStatus = EventStatus.PENDING
    retry_count: int = 0
    
    @validator('payload')
    def validate_payload(cls, v, values):
        """Valida que el payload contenga los campos requeridos según el tipo de evento."""
        event_type = values.get('event_type')
        if event_type == EventType.DESIGN_CHANGE and 'changes' not in v:
            raise ValueError("El payload de DESIGN_CHANGE debe incluir 'changes'")
        elif event_type == EventType.QUALITY_CHECK and 'results' not in v:
            raise ValueError("El payload de QUALITY_CHECK debe incluir 'results'")
        return v

class ProcessingError(BaseModel):
    """Modelo para errores de procesamiento."""
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    error_type: str
    error_message: str
    stack_trace: Optional[str] = None

class DigitalThreadOrchestrator:
    """
    Orquestador del Digital Thread que conecta todas las capas de GAIA AIR.
    
    Responsabilidades:
    - Registro y coordinación de eventos entre sistemas
    - Trazabilidad completa de cambios y decisiones
    - Mantenimiento del linaje de datos a través de todas las fases
    """
    
    def __init__(self, redis_client: Redis):
        """Inicializa el orquestador con las dependencias necesarias."""
        self.redis = redis_client
        self.event_stream = "gaia:digital_thread:events"
        self.event_store = "gaia:digital_thread:store"
        self.event_index = "gaia:digital_thread:index"  # Índice para búsquedas eficientes
        self.lineage_graph = "gaia:digital_thread:lineage"
        self.failed_events = "gaia:digital_thread:failed"
        self.component_timeline = "gaia:digital_thread:component"  # Sorted set por componente
        self.hostname = self._get_hostname()
        
    def _get_hostname(self) -> str:
        """Obtiene el hostname para identificar al consumidor."""
        import socket
        return socket.gethostname()
        
    async def initialize(self):
        """
        Inicializa las estructuras de datos necesarias y crea el grupo de consumidores.
        Debe llamarse al iniciar la aplicación.
        """
        with tracer.start_as_current_span("initialize_orchestrator"):
            try:
                # Crear el stream si no existe
                try:
                    # Intentar crear el grupo de consumidores
                    await self.redis.xgroup_create(
                        self.event_stream, 
                        CONSUMER_GROUP, 
                        id="0", 
                        mkstream=True
                    )
                    logger.info(f"Grupo de consumidores {CONSUMER_GROUP} creado")
                except RedisError:
                    # El grupo ya existe, lo que está bien
                    logger.info(f"Grupo de consumidores {CONSUMER_GROUP} ya existe")
                
                # Configurar índices (en una implementación real usaríamos RediSearch)
                # Aquí simulamos índices con estructuras de Redis
                
                logger.info("Digital Thread Orchestrator inicializado correctamente")
                return True
            except Exception as e:
                logger.error(f"Error inicializando el orquestrador: {e}")
                raise
        
    async def publish_event(self, event: ThreadEvent) -> str:
        """
        Publica un evento en el Digital Thread.
        
        Args:
            event: El evento a publicar
            
        Returns:
            El ID del evento publicado
        """
        with tracer.start_as_current_span("publish_event") as span:
            span.set_attribute("event.id", event.id)
            span.set_attribute("event.type", event.event_type)
            
            try:
                # Almacenar el evento en Redis con TTL
                event_data = event.model_dump_json()
                expiry = int(timedelta(days=EVENT_RETENTION_DAYS).total_seconds())
                
                # Transacción para garantizar consistencia
                tr = self.redis.pipeline()
                
                # Almacenar el evento
                tr.hset(self.event_store, event.id, event_data)
                tr.expire(self.event_store, expiry)
                
                # Publicar en el stream para procesamiento asíncrono
                tr.xadd(self.event_stream, {"event_id": event.id})
                
                # Índice por componente (sorted set ordenado por timestamp)
                score = int(event.timestamp.timestamp() * 1000)  # Milisegundos para precisión
                tr.zadd(f"{self.component_timeline}:{event.component_id}", {event.id: score})
                
                # Si tiene un evento padre, actualizar el grafo de linaje
                if event.parent_event_id:
                    tr.sadd(f"{self.lineage_graph}:children:{event.parent_event_id}", event.id)
                    tr.sadd(f"{self.lineage_graph}:parents:{event.id}", event.parent_event_id)
                
                # Ejecutar la transacción
                await tr.execute()
                
                logger.info(f"Evento publicado: {event.id} - {event.event_type}")
                return event.id
                
            except Exception as e:
                logger.error(f"Error publicando evento {event.id}: {e}")
                span.record_exception(e)
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Error publicando evento: {str(e)}"
                )
    
    async def get_event(self, event_id: str) -> Optional[ThreadEvent]:
        """Recupera un evento por su ID."""
        with tracer.start_as_current_span("get_event") as span:
            span.set_attribute("event.id", event_id)
            
            try:
                event_data = await self.redis.hget(self.event_store, event_id)
                if not event_data:
                    return None
                return ThreadEvent.model_validate_json(event_data)
            except Exception as e:
                logger.error(f"Error recuperando evento {event_id}: {e}")
                span.record_exception(e)
                return None
    
    async def get_component_history(
        self, 
        component_id: str, 
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        limit: int = 100,
        offset: int = 0
    ) -> Tuple[List[ThreadEvent], int]:
        """
        Recupera el historial de un componente con paginación eficiente.
        
        Args:
            component_id: ID del componente
            start_time: Tiempo de inicio (opcional)
            end_time: Tiempo de fin (opcional)
            limit: Número máximo de eventos a retornar
            offset: Desplazamiento para paginación
            
        Returns:
            Tupla de (lista de eventos, conteo total)
        """
        with tracer.start_as_current_span("get_component_history") as span:
            span.set_attribute("component.id", component_id)
            
            try:
                # Convertir tiempos a scores para Redis Sorted Set
                min_score = "-inf"
                max_score = "+inf"
                
                if start_time:
                    min_score = int(start_time.timestamp() * 1000)
                if end_time:
                    max_score = int(end_time.timestamp() * 1000)
                
                # Obtener el conteo total para paginación
                total_count = await self.redis.zcount(
                    f"{self.component_timeline}:{component_id}",
                    min_score,
                    max_score
                )
                
                # Obtener IDs de eventos con paginación
                event_ids = await self.redis.zrevrangebyscore(
                    f"{self.component_timeline}:{component_id}",
                    max_score,
                    min_score,
                    start=offset,
                    num=limit
                )
                
                # Recuperar eventos en paralelo
                events = []
                if event_ids:
                    # Usar mget para eficiencia
                    event_data_list = await self.redis.hmget(
                        self.event_store, 
                        *event_ids
                    )
                    
                    for event_data in event_data_list:
                        if event_data:
                            events.append(ThreadEvent.model_validate_json(event_data))
                
                return events, total_count
                
            except Exception as e:
                logger.error(f"Error recuperando historial del componente {component_id}: {e}")
                span.record_exception(e)
                return [], 0
    
    async def get_event_lineage(self, event_id: str, max_depth: int = 10) -> Dict[str, List[Dict]]:
        """
        Recupera el linaje completo de un evento (ancestros y descendientes).
        
        Args:
            event_id: ID del evento
            max_depth: Profundidad máxima de búsqueda
            
        Returns:
            Dict con "ancestors" y "descendants", cada uno con detalles del evento
        """
        with tracer.start_as_current_span("get_event_lineage") as span:
            span.set_attribute("event.id", event_id)
            
            try:
                # Implementación mejorada usando conjuntos para ancestros y descendientes
                ancestors = await self._get_ancestors(event_id, max_depth)
                descendants = await self._get_descendants(event_id, max_depth)
                
                # Convertir IDs a detalles de eventos
                ancestor_details = await self._get_events_details(ancestors)
                descendant_details = await self._get_events_details(descendants)
                
                return {
                    "ancestors": ancestor_details,
                    "descendants": descendant_details
                }
                
            except Exception as e:
                logger.error(f"Error recuperando linaje del evento {event_id}: {e}")
                span.record_exception(e)
                return {"ancestors": [], "descendants": []}
    
    async def _get_ancestors(self, event_id: str, max_depth: int) -> Set[str]:
        """Recupera recursivamente todos los ancestros de un evento."""
        ancestors = set()
        to_process = {event_id}
        processed = set()
        depth = 0
        
        while to_process and depth < max_depth:
            current_id = to_process.pop()
            processed.add(current_id)
            
            # Obtener padres directos
            parents = await self.redis.smembers(f"{self.lineage_graph}:parents:{current_id}")
            
            for parent_id in parents:
                parent_id = parent_id.decode() if isinstance(parent_id, bytes) else parent_id
                ancestors.add(parent_id)
                if parent_id not in processed:
                    to_process.add(parent_id)
            
            depth += 1
            
        return ancestors
    
    async def _get_descendants(self, event_id: str, max_depth: int) -> Set[str]:
        """Recupera recursivamente todos los descendientes de un evento."""
        descendants = set()
        to_process = {event_id}
        processed = set()
        depth = 0
        
        while to_process and depth < max_depth:
            current_id = to_process.pop()
            processed.add(current_id)
            
            # Obtener hijos directos
            children = await self.redis.smembers(f"{self.lineage_graph}:children:{current_id}")
            
            for child_id in children:
                child_id = child_id.decode() if isinstance(child_id, bytes) else child_id
                descendants.add(child_id)
                if child_id not in processed:
                    to_process.add(child_id)
            
            depth += 1
            
        return descendants
    
    async def _get_events_details(self, event_ids: Set[str]) -> List[Dict]:
        """Convierte un conjunto de IDs de eventos en detalles completos."""
        if not event_ids:
            return []
            
        events = []
        for event_id in event_ids:
            event = await self.get_event(event_id)
            if event:
                events.append(event.model_dump())
        
        # Ordenar por timestamp
        events.sort(key=lambda e: e["timestamp"])
        return events
    
    async def update_event_status(self, event_id: str, status: EventStatus, error: Optional[ProcessingError] = None) -> bool:
        """
        Actualiza el estado de un evento y opcionalmente registra un error.
        
        Args:
            event_id: ID del evento
            status: Nuevo estado
            error: Información de error (opcional)
            
        Returns:
            True si se actualizó correctamente
        """
        with tracer.start_as_current_span("update_event_status") as span:
            span.set_attribute("event.id", event_id)
            span.set_attribute("event.status", status)
            
            try:
                event = await self.get_event(event_id)
                if not event:
                    logger.error(f"Evento no encontrado para actualizar estado: {event_id}")
                    return False
                
                # Actualizar estado
                event.status = status
                
                # Si hay error, añadirlo a los metadatos
                if error and status == EventStatus.FAILED:
                    if "errors" not in event.metadata:
                        event.metadata["errors"] = []
                    event.metadata["errors"].append(error.model_dump())
                    
                    # Añadir a la lista de eventos fallidos si alcanzó el máximo de reintentos
                    if event.retry_count >= MAX_RETRY_ATTEMPTS:
                        await self.redis.sadd(self.failed_events, event_id)
                
                # Guardar evento actualizado
                await self.redis.hset(
                    self.event_store, 
                    event_id, 
                    event.model_dump_json()
                )
                
                return True
                
            except Exception as e:
                logger.error(f"Error actualizando estado del evento {event_id}: {e}")
                span.record_exception(e)
                return False
    
    async def process_events_worker(self):
        """
        Worker que procesa eventos asíncronamente.
        Este método se ejecutaría en un proceso separado.
        """
        consumer_name = CONSUMER_NAME.format(hostname=self.hostname)
        logger.info(f"Iniciando worker de procesamiento de eventos: {consumer_name}")
        
        # Asegurar que el grupo de consumidores existe
        await self.initialize()
        
        while True:
            try:
                # Leer eventos pendientes del stream
                events = await self.redis.xreadgroup(
                    groupname=CONSUMER_GROUP,
                    consumername=consumer_name,
                    streams={self.event_stream: ">"},
                    count=10,
                    block=5000
                )
                
                if not events:
                    # No hay eventos nuevos, procesar eventos pendientes
                    pending_events = await self.redis.xpending_range(
                        name=self.event_stream,
                        groupname=CONSUMER_GROUP,
                        min="-",
                        max="+",
                        count=10
                    )
                    
                    for pe in pending_events:
                        # Reclamar eventos pendientes que llevan más de 30 segundos
                        message_id = pe["message_id"]
                        if time.time() - (int(message_id.split("-")[0]) / 1000) > 30:
                            claimed = await self.redis.xclaim(
                                name=self.event_stream,
                                groupname=CONSUMER_GROUP,
                                consumername=consumer_name,
                                min_idle_time=30000,
                                message_ids=[message_id]
                            )
                            
                            if claimed:
                                for stream_name, stream_events in claimed:
                                    await self._process_stream_events(stream_events)
                    
                    # Esperar un poco antes de verificar nuevamente
                    await asyncio.sleep(1)
                    continue
                
                # Procesar eventos nuevos
                for stream_name, stream_events in events:
                    await self._process_stream_events(stream_events)
            
            except Exception as e:
                logger.exception(f"Error en worker de procesamiento: {e}")
                await asyncio.sleep(5)
    
    async def _process_stream_events(self, stream_events):
        """Procesa una lista de eventos del stream."""
        for message_id, event_data in stream_events:
            event_obj_id = event_data[b"event_id"].decode()
            
            try:
                # Obtener el evento completo
                event_obj = await self.get_event(event_obj_id)
                
                if not event_obj:
                    logger.error(f"Evento no encontrado: {event_obj_id}")
                    # Confirmar procesamiento para evitar bloqueos
                    await self.redis.xack(self.event_stream, CONSUMER_GROUP, message_id)
                    continue
                
                # Actualizar estado a procesando
                await self.update_event_status(event_obj_id, EventStatus.PROCESSING)
                
                # Procesar según el tipo de evento
                success = await self._route_event(event_obj)
                
                if success:
                    # Actualizar estado a completado
                    await self.update_event_status(event_obj_id, EventStatus.COMPLETED)
                    # Confirmar procesamiento
                    await self.redis.xack(self.event_stream, CONSUMER_GROUP, message_id)
                else:
                    # Incrementar contador de reintentos
                    event_obj.retry_count += 1
                    await self.redis.hset(
                        self.event_store, 
                        event_obj_id, 
                        event_obj.model_dump_json()
                    )
                    
                    if event_obj.retry_count >= MAX_RETRY_ATTEMPTS:
                        # Máximo de reintentos alcanzado
                        error = ProcessingError(
                            error_type="max_retries_exceeded",
                            error_message=f"Alcanzado máximo de reintentos ({MAX_RETRY_ATTEMPTS})"
                        )
                        await self.update_event_status(
                            event_obj_id, 
                            EventStatus.FAILED,
                            error
                        )
                        # Confirmar procesamiento para evitar bloqueos
                        await self.redis.xack(self.event_stream, CONSUMER_GROUP, message_id)
                    else:
                        # No confirmar para que se reintente
                        logger.info(f"Reintentando evento {event_obj_id} (intento {event_obj.retry_count})")
            
            except Exception as e:
                logger.exception(f"Error procesando evento {event_obj_id}: {e}")
                # Registrar el error
                import traceback
                error = ProcessingError(
                    error_type=type(e).__name__,
                    error_message=str(e),
                    stack_trace=traceback.format_exc()
                )
                
                try:
                    # Obtener evento nuevamente por si cambió
                    event_obj = await self.get_event(event_obj_id)
                    if event_obj:
                        event_obj.retry_count += 1
                        await self.redis.hset(
                            self.event_store, 
                            event_obj_id, 
                            event_obj.model_dump_json()
                        )
                        
                        if event_obj.retry_count >= MAX_RETRY_ATTEMPTS:
                            await self.update_event_status(
                                event_obj_id, 
                                EventStatus.FAILED,
                                error
                            )
                            # Confirmar procesamiento
                            await self.redis.xack(self.event_stream, CONSUMER_GROUP, message_id)
                except Exception:
                    # Si falla incluso el manejo de errores, confirmar para evitar bloqueos
                    await self.redis.xack(self.event_stream, CONSUMER_GROUP, message_id)
    
    async def _route_event(self, event: ThreadEvent) -> bool:
        """
        Enruta un evento a los sistemas correspondientes según su tipo.
        
        Returns:
            True si el procesamiento fue exitoso
        """
        with tracer.start_as_current_span("route_event") as span:
            span.set_attribute("event.id", event.id)
            span.set_attribute("event.type", event.event_type)
            
            try:
                # Implementación de enrutamiento basado en el tipo de evento
                if event.event_type == EventType.DESIGN_CHANGE:
                    # Notificar a los gemelos digitales
                    logger.info(f"Notificando cambio de diseño a gemelos digitales: {event.id}")
                    return await self._notify_digital_twins(event)
                    
                elif event.event_type == EventType.PRODUCTION_START:
                    # Actualizar sistema MES
                    logger.info(f"Actualizando MES para inicio de producción: {event.id}")
                    return await self._update_mes(event)
                    
                elif event.event_type == EventType.MAINTENANCE_ALERT:
                    # Notificar al sistema de mantenimiento
                    logger.info(f"Enviando alerta de mantenimiento: {event.id}")
                    return await self._send_maintenance_alert(event)
                    
                elif event.event_type == EventType.SUSTAINABILITY_METRIC:
                    # Registrar métricas de sostenibilidad
                    logger.info(f"Registrando métricas de sostenibilidad: {event.id}")
                    return await self._record_sustainability_metrics(event)
                
                # Registrar métricas de sostenibilidad para todos los eventos si contienen datos
                if "sustainability" in event.metadata:
                    logger.info(f"Registrando métricas de sostenibilidad adicionales: {event.id}")
                    await self._record_sustainability_metrics(event)
                
                return True
                
            except Exception as e:
                logger.error(f"Error enrutando evento {event.id}: {e}")
                span.record_exception(e)
                return False
    
    async def _notify_digital_twins(self, event: ThreadEvent) -> bool:
        """Notifica cambios a los gemelos digitales."""
        try:
            # Simulación de integración con sistema de gemelos digitales
            logger.info(f"Enviando evento {event.id} al sistema de gemelos digitales")
            
            # En una implementación real, aquí habría una llamada a la API del sistema
            # de gemelos digitales o una publicación en un topic de mensajería
            
            # Simulamos un tiempo de procesamiento
            await asyncio.sleep(0.5)
            
            # Registrar en telemetría
            with tracer.start_as_current_span("digital_twin_notification") as span:
                span.set_attribute("event.id", event.id)
                span.set_attribute("component.id", event.component_id)
                
                # Simular éxito
                return True
                
        except Exception as e:
            logger.error(f"Error notificando a gemelos digitales: {e}")
            return False
    
    async def _update_mes(self, event: ThreadEvent) -> bool:
        """Actualiza el sistema MES con información de producción."""
        try:
            # Simulación de integración con sistema MES
            logger.info(f"Actualizando MES con evento {event.id}")
            
            # En una implementación real, aquí habría una llamada a la API del MES
            # o una actualización en una base de datos compartida
            
            # Simulamos un tiempo de procesamiento
            await asyncio.sleep(0.7)
            
            # Registrar en telemetría
            with tracer.start_as_current_span("mes_update") as span:
                span.set_attribute("event.id", event.id)
                span.set_attribute("component.id", event.component_id)
                
                # Simular éxito
                return True
                
        except Exception as e:
            logger.error(f"Error actualizando MES: {e}")
            return False
    
    async def _send_maintenance_alert(self, event: ThreadEvent) -> bool:
        """Envía alertas al sistema de mantenimiento."""
        try:
            # Simulación de integración con sistema de mantenimiento
            logger.info(f"Enviando alerta de mantenimiento para evento {event.id}")
            
            # En una implementación real, aquí habría una llamada a la API del sistema
            # de mantenimiento o el envío de una notificación
            
            # Simulamos un tiempo de procesamiento
            await asyncio.sleep(0.3)
            
            # Registrar en telemetría
            with tracer.start_as_current_span("maintenance_alert") as span:
                span.set_attribute("event.id", event.id)
                span.set_attribute("component.id", event.component_id)
                span.set_attribute("alert.severity", event.payload.get("severity", "unknown"))
                
                # Simular éxito
                return True
                
        except Exception as e:
            logger.error(f"Error enviando alerta de mantenimiento: {e}")
            return False
    
    async def _record_sustainability_metrics(self, event: ThreadEvent) -> bool:
        """Registra métricas de sostenibilidad."""
        try:
            # Simulación de registro de métricas
            logger.info(f"Registrando métricas de sostenibilidad para evento {event.id}")
            
            # Extraer métricas de sostenibilidad del evento
            sustainability_data = event.metadata.get("sustainability", {})
            if event.event_type == EventType.SUSTAINABILITY_METRIC:
                sustainability_data.update(event.payload)
            
            if not sustainability_data:
                logger.warning(f"No hay datos de sostenibilidad en el evento {event.id}")
                return True  # No es un error, simplemente no hay datos
            
            # En una implementación real, aquí registraríamos las métricas en un
            # sistema de análisis de sostenibilidad o una base de datos de series temporales
            
            # Simulamos un tiempo de procesamiento
            await asyncio.sleep(0.4)
            
            # Registrar en telemetría
            with tracer.start_as_current_span("sustainability_metrics") as span:
                span.set_attribute("event.id", event.id)
                span.set_attribute("component.id", event.component_id)
                
                # Registrar métricas específicas si están disponibles
                for metric, value in sustainability_data.items():
                    if isinstance(value, (int, float)):
                        span.set_attribute(f"sustainability.{metric}", value)
                
                # Simular éxito
                return True
                
        except Exception as e:
            logger.error(f"Error registrando métricas de sostenibilidad: {e}")
            return False

# Autenticación para API
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_redis_client() -> Redis:
    """Dependencia para obtener un cliente Redis."""
    # En una implementación real, usaríamos un pool de conexiones
    redis = Redis(host="localhost", port=6379, db=0)
    try:
        yield redis
    finally:
        await redis.close()

async def get_orchestrator(redis: Redis = Depends(get_redis_client)) -> DigitalThreadOrchestrator:
    """Dependencia para obtener una instancia del orquestrador."""
    orchestrator = DigitalThreadOrchestrator(redis)
    # Asegurar que está inicializado
    await orchestrator.initialize()
    return orchestrator

# Ejemplo de endpoint para publicar un evento con seguridad
async def publish_thread_event(
    event: ThreadEvent,
    orchestrator: DigitalThreadOrchestrator = Depends(get_orchestrator),
    token: str = Security(oauth2_scheme)
) -> Dict[str, str]:
    """
    Endpoint para publicar un evento en el Digital Thread.
    Requiere autenticación OAuth2.
    """
    # En una implementación real, aquí verificaríamos permisos basados en el token
    # y el tipo de evento que se está publicando
    
    event_id = await orchestrator.publish_event(event)
    return {"event_id": event_id, "status": "pending"}

# Ejemplo de endpoint para consultar el historial de un componente
async def get_component_history_endpoint(
    component_id: str,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    limit: int = 100,
    offset: int = 0,
    orchestrator: DigitalThreadOrchestrator = Depends(get_orchestrator),
    token: str = Security(oauth2_scheme)
) -> Dict[str, Any]:
    """
    Endpoint para consultar el historial de un componente.
    Incluye paginación y filtrado por tiempo.
    """
    events, total = await orchestrator.get_component_history(
        component_id, start_time, end_time, limit, offset
    )
    
    return {
        "component_id": component_id,
        "total_events": total,
        "limit": limit,
        "offset": offset,
        "events": [event.model_dump() for event in events]
    }
