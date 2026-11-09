---
name: api-integration-testing
description: Verify API behavior, contracts, authorization, persistence and integrations across service boundaries.
---
# API & Integration Testing

## Procedimiento
1. Derivar escenarios de contratos y criterios de aceptación.
2. Levantar dependencias reproducibles o dobles controlados.
3. Probar autenticación, autorización por rol/tenant y acceso denegado.
4. Probar validación, tipos, paginación, filtros y límites.
5. Probar persistencia, transacciones, idempotencia y concurrencia.
6. Probar timeouts, fallos parciales, respuestas inválidas y rate limits.
7. Verificar códigos, esquemas, errores estables y ausencia de datos internos.
8. Aislar y limpiar fixtures; evitar datos reales.
9. Ejecutar en CI con reportes reproducibles.

## Gates
Cubrir escenarios positivos, negativos y de permisos. No depender de servicios externos inestables. No desactivar seguridad para hacer pasar pruebas.
