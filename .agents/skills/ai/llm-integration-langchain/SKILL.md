---
name: llm-integration-langchain
description: Integrar modelos de lenguaje grandes (OpenAI, Anthropic, Gemini, Ollama) en aplicaciones usando LangChain, Vercel AI SDK o llamadas directas a API con Function Calling.
---

# LLM Integration & LangChain Skill

## Propósito
Construir funcionalidades potenciadas por Inteligencia Artificial generativa con manejo de prompts, streaming de texto y llamadas a funciones estructuradas.

## Guía de Implementación

### 1. Vercel AI SDK / LangChain
- Usar Vercel AI SDK (`useChat`, `streamText`) para enviar respuestas en tiempo real al frontend.
- Definir esquemas de entrada/salida estricta con **Zod** para llamadas a funciones (*Function Calling / Structured Outputs*).

### 2. Manejo de Contexto y Token Cost
- Limitar el historial de chat enviado a la API para evitar exceder la ventana de contexto y optimizar costos.
