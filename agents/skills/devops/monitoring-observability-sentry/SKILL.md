---
name: monitoring-observability-sentry
description: Configurar monitoreo de errores en tiempo real, rastreo de rendimiento (tracing), métricas y alertas con Sentry, Datadog o LogRocket en aplicaciones frontend, móviles y backend.
---

# Monitoring & Observability Skill

## Propósito
Detectar, diagnosticar y resolver excepciones, errores de servidor y problemas de latencia antes de que afecten masivamente a los usuarios.

## Guía de Implementación

### 1. Monitoreo de Excepciones con Sentry
- Inicializar el SDK de Sentry en el punto de entrada de la aplicación.
- Capturar excepciones no controladas con contexto del usuario autenticado (ID de usuario, rol, plataforma).
- Excluir explícitamente contraseñas o tokens de los logs de Sentry.

### 2. Tracing de Rendimiento
- Rastrear tiempos de respuesta de consultas SQL y peticiones de red.
