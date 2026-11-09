---
name: agentic-workflows-mcp
description: Construir agentes de IA autónomos con herramientas, memoria conversacional, protocolos de contexto (MCP - Model Context Protocol) y flujos multiagente.
---

# Agentic Workflows & MCP Skill

## Propósito
Crear agentes autónomos capaces de razonar, planificar y ejecutar herramientas externas para resolver tareas complejas.

## Guía de Implementación

### 1. Arquitectura de Agente Autónomo
- **Ciclo ReAct (Reasoning + Acting)**: El agente analiza el estado, decide qué herramienta usar, lee la respuesta de la herramienta y repite el proceso hasta cumplir la meta.
- **Model Context Protocol (MCP)**: Conectar agentes con servidores MCP estandarizados para acceder a repositorios Git, bases de datos y herramientas del sistema.
