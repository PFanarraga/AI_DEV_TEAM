---
name: performance-load-testing
description: Measure latency, throughput, saturation and resilience under representative load and failure conditions.
---
# Performance & Load Testing

## Procedimiento
1. Definir hipótesis, journeys, perfil de carga, concurrencia y duración.
2. Acordar SLO y umbrales con evidencia.
3. Crear datos sintéticos y proteger servicios compartidos.
4. Establecer baseline y controlar entorno y configuración.
5. Ejecutar carga gradual, pico, estrés y soak cuando corresponda.
6. Medir p50/p95/p99, throughput, errores, CPU, memoria, IO, DB y colas.
7. Identificar saturación y cuello de botella.
8. Probar límites, timeouts, backpressure y recuperación.
9. Comparar con baseline y documentar incertidumbre.

## Seguridad
No ejecutar pruebas agresivas en producción o terceros sin autorización y ventana aprobada. No confundir carga sintética con tráfico real.
