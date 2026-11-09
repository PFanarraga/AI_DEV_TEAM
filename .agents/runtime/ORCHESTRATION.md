# Arquitectura objetivo de orquestación

> Estado: especificación de diseño, no runtime ejecutable. Los perfiles Markdown no crean procesos independientes ni ejecutan herramientas por sí solos.

## Componentes
1. Request Gateway: solicitud, identidad, repositorio, permisos y restricciones.
2. Project Inspector: árbol, stack, scripts, pruebas, estado Git y documentación.
3. Director/Planner: tareas, criterios de aceptación, dependencias y riesgos.
4. Task Orchestrator: asignación, estados, límites, reintentos y cancelación.
5. Agent Workers: perfiles especialistas con contexto mínimo y herramientas autorizadas.
6. Shared Task Store: estado, artefactos, decisiones y handoffs; nunca secretos.
7. Tool Gateway: operaciones de lectura/escritura con permisos y confirmaciones.
8. Review & Verification: diff, pruebas autorizadas y criterios.
9. Delivery Reporter: cambios, pruebas reales, limitaciones y riesgos residuales.

## Ciclo de vida
RECEIVED → INSPECTING → PLANNING → AWAITING_APPROVAL → EXECUTING → REVIEWING → VERIFYING → DELIVERED

Estados alternativos: BLOCKED, FAILED, CANCELLED y NEEDS_INPUT. No ejecutar si falta aprobación. Pedir información ante datos críticos ausentes. Reintentar con límites e idempotencia. Cancelar sin dejar operaciones en estados inseguros.

## Contrato de tarea
Cada tarea contiene task_id, request_id, parent_task_id, agent_role, Skills, objetivo, alcance, exclusiones, criterios de aceptación, archivos autorizados, dependencias, prioridad, herramientas permitidas, nivel de riesgo, estado, intentos, timeout, resultado y artefactos.

Los resultados distinguen hechos, inferencias, propuestas y acciones ejecutadas.

## Handoff
Incluir objetivo, contexto, archivos inspeccionados, evidencia, decisiones, cambios, pruebas ejecutadas, resultados, riesgos y pendientes. No incluir credenciales.

## Concurrencia
Paralelizar solo tareas independientes con límites de archivos claros. Serializar cambios sobre los mismos archivos. El Director resuelve conflictos y revisa la integración. Si el entorno no ofrece subagentes reales, informar que la ejecución es secuencial o asistida.

## Permisos
- Read-only: inspección y análisis.
- Workspace-write: cambios de archivos.
- External-write: commits, PR y servicios externos.
- Production: despliegues, migraciones y operaciones productivas.

Denegar permisos no concedidos. Registrar aprobaciones y acciones. No permitir borrar datos, cambiar permisos o desplegar sin autorización explícita.

## Verificación
Cerrar como verificado solo con evidencia de criterios, pruebas realmente ejecutadas, diff revisado, secretos protegidos y limitaciones documentadas.

## Fases
1. MVP documental (estado actual).
2. Runtime local: cola, adaptador de modelos, gateway de herramientas y aprobaciones.
3. Persistencia: estado, artefactos, memoria de proyecto y auditoría.
4. Multiagente: workers, dependencias, concurrencia limitada y cancelación.
5. Verificación: tests aislados, análisis estático y revisión.
6. Hardening: permisos granulares, sandbox, límites de costo y pruebas de seguridad.

No anunciar el sistema como autónomo hasta implementar y probar runtime, delegación, permisos y verificación.
