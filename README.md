# AI DEV TEAM

Framework de ingeniería asistida por IA con **18 agentes, 57 Skills únicas y 8 workflows** para proyectos web, móviles, desktop, backend, datos, IA, videojuegos, XR y e-commerce.

## Objetivo
El usuario trabaja con el asistente que ya utiliza en su IDE, editor, terminal o plataforma. Ese asistente asume el rol de **Director**, interpreta la solicitud, inspecciona el repositorio, selecciona especialistas y Skills, orquesta la ejecución y consolida resultados.

El framework no exige un motor ejecutable propio. La delegación paralela, memoria, ejecución de herramientas y aprobaciones dependen de las capacidades del asistente anfitrión. Si no existen subagentes reales, el Director coordina el trabajo secuencialmente y lo informa con transparencia.

## Estructura
- AGENTS.md: reglas globales y protocolo de orquestación.
- .agents/agents/: 18 perfiles especialistas.
- .agents/skills/: 57 Skills organizadas por dominio.
- .agents/workflows/: 8 procesos reutilizables.
- .agents/runtime/: especificación de arquitectura para un runtime opcional.
- adapters/: guía y prompt universal de integración.
- docs/IDE-COMPATIBILITY.md: estrategia y matriz de portabilidad.
- CLAUDE.md, GEMINI.md, .cursor/, .github/ y .junie/: adaptadores incluidos para hosts compatibles.
- templates/: solicitudes, handoffs, ADR y pull requests.
- scripts/: validaciones del framework.

## Inicio rápido
1. Copia AGENTS.md y la carpeta completa .agents/ a la raíz del proyecto.
2. Copia también el adaptador nativo del asistente que uses, si corresponde.
3. Abre el proyecto en el IDE o entorno.
4. Verifica que el asistente lea las instrucciones.
5. Activa el Director con el prompt de adapters/README.md.
6. Aprueba el plan antes de cambios amplios o destructivos.

## Portabilidad
El núcleo común es Markdown + rutas + convenciones. Hay adaptadores para Copilot, Codex, Cursor, Claude Code, Gemini CLI y Junie. Para otros entornos, consulta docs/IDE-COMPATIBILITY.md y configura el formato nativo correspondiente.

No existe un formato único que garantice que todos los IDEs carguen Skills, subagentes y herramientas de la misma manera. MCP facilita interoperabilidad de herramientas, no delegación universal.

## Validación
Ejecuta desde la raíz: python scripts/validate_framework.py

Comprueba estructura, inventario y referencias documentales. No ejecuta agentes ni prueba aplicaciones externas.

## Alcance honesto
Este repositorio proporciona perfiles, instrucciones, Skills, workflows y adaptadores. No incluye todavía un runtime autónomo propio. El Director orquesta usando las capacidades del asistente anfitrión.

## Seguridad y licencia
Nunca subas secretos. No asumas licencia de código abierto hasta que el repositorio incluya una licencia explícita.
