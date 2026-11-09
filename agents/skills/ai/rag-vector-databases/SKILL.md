---
name: rag-vector-databases
description: Implementar arquitecturas de Generación Aumentada por Recuperación (RAG) con bases de datos vectoriales (pgvector, Pinecone, Qdrant, Chroma) y modelos de embeddings.
---

# RAG & Vector Databases Skill

## Propósito
Permitir que los modelos de Inteligencia Artificial respondan preguntas utilizando la base de conocimiento privada y documentación de la empresa.

## Guía de Implementación

### 1. Extracción y Generación de Embeddings
- Fragmentar documentos largos en trozos (*chunks*) de tamaño adecuado (ej. 500-1000 caracteres con solapamiento).
- Convertir texto a vectores usando modelos de embedding (OpenAI `text-embedding-3-small`, Cohere u Ollama Nomic).

### 2. Búsqueda Vectorial
- Almacenar embeddings en **PostgreSQL con pgvector** o en **Pinecone / Qdrant**.
- Ejecutar búsquedas de similitud de coseno para recuperar los trozos más relevantes e inyectarlos en el prompt del LLM.
