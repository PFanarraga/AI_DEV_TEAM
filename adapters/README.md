# Adaptadores de AI DEV TEAM

## Propósito
Conectar la fuente canónica de AI DEV TEAM con distintos IDEs, editores, asistentes y terminales. No se requiere motor propio: el asistente anfitrión actúa como Director.

## Núcleo
Copia a la raíz del proyecto:
- AGENTS.md
- .agents/

Conserva la jerarquía y no renombres .agents/.

## Adaptadores incluidos y documentados
Este repositorio incluye archivos nativos para:
- GitHub Copilot: .github/copilot-instructions.md
- OpenAI Codex y hosts compatibles con AGENTS.md: AGENTS.md
- Cursor: .cursor/rules/ai-dev-team.mdc y AGENTS.md
- Claude Code: CLAUDE.md
- Gemini CLI: GEMINI.md
- Junie: .junie/AGENTS.md

Los archivos son adaptadores ligeros. En proyectos existentes, copia o combina solo el adaptador del host que realmente uses. No sobrescribas reglas locales existentes.

## Prompt universal de activación
Cuando el host no detecte automáticamente sus instrucciones, pega este prompt:

> Lee AGENTS.md y actúa como Director de AI DEV TEAM. Inspecciona el repositorio, estado de Git, stack, instrucciones del host y herramientas disponibles. Consulta .agents/agents/director.md. Clasifica mi solicitud, selecciona solo especialistas y Skills pertinentes y presenta objetivo, alcance, tareas, dependencias, riesgos y criterios de aceptación antes de modificar. Si tienes subagentes reales, delega tareas independientes y reporta qué delegaste. Si no, coordina secuencialmente sin simular procesos paralelos. No inventes herramientas ni resultados. Conserva mis cambios y pide aprobación para operaciones destructivas, externas o productivas. Revisa el diff, ejecuta pruebas disponibles y reporta comandos y resultados reales.

## Otros IDEs, editores y plataformas
Para Visual Studio, JetBrains IDEs sin Junie/Copilot, Android Studio sin Junie/Copilot, Eclipse, NetBeans, Xcode, Windsurf, Zed, Cline, Roo Code, Continue, Aider, otros agentes CLI y entornos cloud:
1. Consulta docs/IDE-COMPATIBILITY.md.
2. Verifica la documentación oficial y versión del host.
3. Configura el archivo de instrucciones nativo del host para cargar AGENTS.md y activar al Director.
4. Si el host no carga AGENTS.md, usa el prompt universal o un adaptador específico revisado.
5. Verifica carga de Skills, herramientas y delegación real.

La lista de productos no significa que todos tengan un adaptador implementado. No existe una configuración única que active automáticamente todos los IDEs.

## Niveles de funcionamiento
- Instrucciones cargadas: el host leyó el contexto.
- Skills accesibles: el Director puede consultar Skills pertinentes.
- Herramientas disponibles: el host puede ejecutar acciones autorizadas.
- Delegación real: el host creó subagentes independientes y recibió resultados.
- Orquestación avanzada: el sistema conserva estado, permisos, cancelación y auditoría.

MCP conecta herramientas en clientes compatibles; no sustituye el soporte de subagentes ni un runtime.

## Seguridad
Nunca guardes claves o tokens en archivos de instrucciones. No otorgues acceso irrestricto al filesystem o shell. Revisa permisos y comandos antes de aprobar.
