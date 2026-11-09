---
name: integration-testing
description: Test interactions between modules, persistence, queues and external boundaries with controlled dependencies.
---
# Integration Testing

## Estrategia
1. Identificar contratos y límites entre componentes.
2. Usar dependencias efímeras reales cuando aporten fidelidad y dobles controlados cuando convenga.
3. Aislar datos por prueba y garantizar cleanup.
4. Verificar transacciones, consistencia, eventos, reintentos e idempotencia.
5. Simular timeout, caída, duplicados, orden incorrecto y recuperación.
6. Evitar dependencia de orden, hora, red pública o estado compartido.
7. Ejecutar suite crítica en CI y suites costosas en pipeline apropiado.

## Evidencia
Reportar entorno, versiones, comando, pruebas, resultado y fallos. No llamar integración real a una prueba que solo usa mocks.
