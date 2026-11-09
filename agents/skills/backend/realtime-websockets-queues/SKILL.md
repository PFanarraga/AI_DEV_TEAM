---
name: realtime-websockets-queues
description: Diseñar e implementar comunicación en tiempo real con WebSockets, Server-Sent Events (SSE), colas de procesamiento en segundo plano (Redis, RabbitMQ) y mensajería en vivo.
---

# Realtime & Message Queues Skill

## Propósito
Garantizar actualización instantánea de la interfaz e independizar tareas pesadas mediante arquitecturas orientadas a eventos y colas asíncronas.

## Guía de Implementación

### 1. Comunicación en Tiempo Real
- **WebSockets / Socket.io / Supabase Realtime**: Utilizar canales pub/sub para notificaciones instantáneas, chats y cambios en vivo.
- **Server-Sent Events (SSE)**: Preferir SSE para flujos unidireccionales de servidor a cliente (ej: streaming de respuestas de IA, estados de procesamiento).

### 2. Procesamiento Asíncrono en Segundo Plano
- **Colas (BullMQ, Redis, RabbitMQ)**: Desplazar tareas intensivas (envío de emails, generación de PDFs, procesamiento de videos) fuera del hilo principal de la API HTTP.
- **Idempotencia en Consumidores**: Garantizar que procesar el mismo mensaje dos veces produzca el mismo resultado sin duplicar operaciones financieras o envíos.
