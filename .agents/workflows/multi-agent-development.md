# Workflow: Desarrollo coordinado por el Director

## Activación
Funciones, refactorizaciones o correcciones que requieren varias disciplinas.

## Secuencia
1. Director inspecciona repositorio, Git, scripts, pruebas y capacidades del host.
2. Product Manager aclara requisitos si es necesario.
3. Architect define diseño, contratos y límites de archivos.
4. Director crea tareas con IDs, responsables, Skills, dependencias y criterios.
5. Delegar a subagentes reales solo si el host los soporta. En otro caso, ejecutar por etapas secuenciales.
6. Especialistas entregan handoffs con evidencia, cambios y pruebas.
7. Director integra, resuelve conflictos y revisa el diff completo.
8. Tester/QA ejecutan pruebas pertinentes; Security revisa cambios sensibles.
9. Director verifica criterios y entrega resultados y pendientes.

## Reglas de coordinación
No permitir escrituras paralelas sobre los mismos archivos sin estrategia explícita. No simular agentes, ejecuciones ni pruebas. Mantener cambios del usuario. Solicitar aprobación para acciones de alto riesgo.
