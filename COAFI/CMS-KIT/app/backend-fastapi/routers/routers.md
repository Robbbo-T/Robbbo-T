
# 📡 Routers - CMS-KIT Backend (FastAPI)

Este módulo contiene los routers de la API REST para el sistema de gestión de contenidos (**CMS-KIT**) del proyecto 
**COAFI**.

Cada router encapsula la lógica de enrutamiento para un dominio funcional, siguiendo principios de modularidad y 
separación de responsabilidades. Esto permite una integración limpia y segura con **sistemas federados o 
descentralizados**, como nodos **GAIA-AIR**, identidades distribuidas (**SSI/DID**), y flujos auditables con 
**gaia-token**.

---

## 📁 Estructura actual

```
routers/
├── users.py              # Gestión de identidades
├── memory.py             # Operaciones de memoria (deprecated o en transición)
├── semantic-bridge.py    # Búsqueda semántica, RAG y estadísticas
```

---

## 🔐 `users.py` – Gestión de Identidades

Router que implementa la interfaz REST para el manejo de usuarios. Compatible con:

- OAuth2 con JWT
- Identidades federadas (SSO-ready)
- Tokens descentralizados (soporte planificado para `gaia-token`)

**Endpoints disponibles:**

| Método | Ruta             | Descripción                          | Seguridad         |
|--------|------------------|--------------------------------------|-------------------|
| POST   | `/users/`        | Crear un nuevo usuario               | Público           |
| GET    | `/users/`        | Listar usuarios                      | Requiere token    |
| GET    | `/users/me`      | Usuario autenticado actual           | Requiere token    |
| GET    | `/users/{id}`    | Obtener usuario por ID               | Requiere token    |
| DELETE | `/users/{id}`    | Eliminar un usuario                  | Requiere token    |

**Dependencias clave:** `get_db`, `get_current_active_user`

---

## 🧠 `semantic-bridge.py` – Memoria Semántica y RAG

Router central para operaciones de búsqueda semántica, generación de embeddings, memoria dinámica y generación aument
por recuperación (**RAG**).

**Endpoints disponibles:**

| Método | Ruta                         | Descripción                                               | Seguridad      
|--------|------------------------------|-----------------------------------------------------------|----------------
| POST   | `/semantic-query/`           | Consulta semántica sobre la memoria                       | Público / Token
| POST   | `/semantic-query/rag`        | Generación RAG (Retrieval-Augmented Generation)           | Requiere token 
| POST   | `/semantic-query/memory`     | Agregar contenido a la memoria semántica                  | Requiere token 
| POST   | `/semantic-query/memory/cleanup` | Ejecutar limpieza de memoria (deduplicación, compresión) | Requiere 
token    |
| GET    | `/semantic-query/stats`      | Métricas del sistema de memoria                           | Requiere token 
| GET    | `/semantic-query/trend`      | Tendencia de uso de memoria (MB por día)                  | Requiere token 
| GET    | `/semantic-query/logs`       | Historial de queries semánticas                           | Requiere token 

**Destacado:** Este módulo utiliza `memory_service`, con soporte para `pgvector`, `Pinecone`, cacheo en Redis, y 
embeddings con `OpenAI` o `XAI`.

---

## 🎯 Objetivo General

> Desacoplar y escalar funcionalidades del backend para permitir:

- Orquestación modular
- Federación de identidades
- Auditoría distribuida y transparente
- Recuperación semántica contextual
- Autenticación unificada y portable (SSO/SSI-ready)

---

## 🧭 Roadmap Pendiente

- ✅ Integración con `pgvector` y `Pinecone`
- 🔜 Autenticación federada con `gaia-token`
- 🔜 Firma de tokens con claves asimétricas (ECDSA)
- 🔜 Soporte para `Self-Sovereign Identity` (SSI / DID)
- 🔜 Control granular de roles y permisos por recurso

---

## 📎 Requisitos Técnicos

- Python `3.10+`
- FastAPI
- SQLAlchemy
- Authlib / PyJWT
- PostgreSQL / SQLite
- Redis (opcional, para cache)

---

## 🤖 Autoría

Desarrollado como parte de la arquitectura distribuida y cuántica de **GAIA AIR**, este backend forma la base del sis
COAFI (**Content Management System as Container and Orchestrator for Aerospace Fixed Index**), asegurando trazabilida
eficiencia y ética en entornos de misión crítica aeroespacial.

> _Designed for AI-driven federated infrastructures. Verified for ethical alignment and quantum-compatibility._
