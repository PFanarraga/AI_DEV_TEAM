# AI DEV TEAM

Framework documental de ingeniería asistida por IA con **12 agentes, 41 Skills únicas y 5 workflows** para proyectos web, móviles, desktop, backend, datos, IA, videojuegos, XR y e-commerce.

> **Alcance actual:** contiene perfiles Markdown, Skills, workflows, plantillas y una especificación de orquestación. Todavía no incluye un runtime ejecutable que lance agentes autónomos o concurrentes. La ejecución depende del IDE o plataforma que lea estos archivos.

## Estructura
- AGENTS.md: reglas globales e inventario.
- .agents/agents/: 12 perfiles especialistas.
- .agents/skills/: 41 Skills únicas organizadas por dominio.
- .agents/workflows/: 5 flujos de trabajo.
- .agents/runtime/: arquitectura objetivo de orquestación.
- templates/: solicitud, handoff, ADR y pull request.
- scripts/: validaciones del framework.
- .github/workflows/: validación automática.

## Inicio rápido
1. Copia AGENTS.md y la carpeta .agents/ a la raíz del proyecto.
2. Abre el proyecto en tu IDE o asistente.
3. Pide al asistente que lea AGENTS.md y .agents/agents/director.md.
4. Solicita inspección, plan y criterios de aceptación.
5. Aprueba el plan antes de cambios amplios o destructivos.
6. Invoca especialistas y exige evidencias de pruebas.

Prompt: Lee AGENTS.md y .agents/agents/director.md. Actúa como Director de AI DEV TEAM. Inspecciona el repositorio, selecciona especialistas y Skills, presenta un plan con riesgos y criterios de aceptación y espera mi aprobación. No afirmes que delegaste tareas ni ejecutaste herramientas si el entorno no dispone realmente de esas capacidades.

## Catálogo
12 agentes, 41 Skills en 10 dominios, 5 workflows y 4 plantillas. Consulta AGENTS.md y TUTORIAL_MAESTRO_AI_DEV_TEAM.md.

## Validación
Ejecuta: python scripts/validate_framework.py
GitHub Actions ejecuta esta validación en cada push y pull request. Comprueba estructura y referencias documentales, no compila aplicaciones externas.

## Seguridad y licencia
Nunca subas secretos. Este repositorio no declara una licencia de código abierto; no asumas permisos de reutilización o redistribución hasta que se añada una licencia explícita.
