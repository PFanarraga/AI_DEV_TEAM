# AI DEV TEAM

Framework de ingeniería asistida por IA con **18 agentes, 57 Skills únicas y 8 workflows** para proyectos web, móviles, desktop, backend, datos, IA, videojuegos, XR y e-commerce.

## Objetivo
El usuario trabaja con el asistente que ya utiliza en su IDE, editor, terminal o plataforma. Ese asistente asume el rol de **Director**, interpreta la solicitud, inspecciona el repositorio, selecciona especialistas y Skills, orquesta la ejecución y consolida resultados.

El framework no exige un motor ejecutable propio. La delegación paralela, memoria, ejecución de herramientas y aprobaciones dependen de las capacidades del asistente anfitrión. Si no existen subagentes reales, el Director coordina el trabajo secuencialmente y lo informa con transparencia.

## Estructura
- AGENTS.md: reglas globales, protocolo de orquestación e inventario.
- .agents/agents/: 18 perfiles especialistas.
- .agents/skills/: 57 Skills organizadas por dominio.
- .agents/workflows/: 8 procesos reutilizables.
- .agents/runtime/: especificación de arquitectura para un runtime opcional.
- adapters/: guía para integrar distintos IDEs y asistentes.
- docs/IDE-COMPATIBILITY.md: estrategia de portabilidad.
- templates/: solicitudes, handoffs, ADR y pull requests.
- scripts/: validaciones del framework.
- .github/workflows/: validación automática.

## Inicio rápido
1. Copia AGENTS.md y la carpeta completa .agents/ a la raíz del proyecto.
2. Abre el proyecto en tu IDE, editor o entorno de desarrollo.
3. Configura el asistente para que lea AGENTS.md. Si admite archivos de instrucciones nativos, usa el adaptador correspondiente.
4. Envía el prompt de activación que aparece en adapters/README.md.
5. El Director inspeccionará el proyecto y propondrá especialistas, Skills, plan y criterios.
6. Aprueba el plan antes de cambios amplios o destructivos.

## Portabilidad
El núcleo común es Markdown + rutas + convenciones. Consulta docs/IDE-COMPATIBILITY.md. No existe un formato único que garantice que todos los IDEs carguen Skills, subagentes y herramientas de la misma manera. Los adaptadores deben verificar las capacidades reales de cada host y nunca sobrescribir configuración existente.

MCP puede conectar herramientas en clientes compatibles; no sustituye el soporte de subagentes, permisos o ejecución del host.

## Validación
Ejecuta desde la raíz: python scripts/validate_framework.py

La validación automática comprueba estructura, inventario y referencias documentales. No ejecuta agentes ni prueba aplicaciones construidas con el framework.

## Alcance honesto
Este repositorio proporciona perfiles, instrucciones, Skills, workflows y guías de integración. No incluye todavía un runtime autónomo propio. El objetivo es que el Director orqueste usando las capacidades disponibles del asistente anfitrión, sin atarse a un IDE o proveedor concreto.

## Seguridad y licencia
Nunca subas secretos. No asumas licencia de código abierto hasta que el repositorio incluya una licencia explícita.
