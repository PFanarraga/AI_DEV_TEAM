# AI DEV TEAM

Framework de ingeniería asistida por IA con **18 agentes, 57 Skills únicas y 8 workflows** para proyectos web, móviles, desktop, backend, datos, IA, videojuegos, XR y e-commerce.

## Objetivo
El usuario trabaja con el asistente que prefiera. Ese asistente asume el rol de **Director**, inspecciona el proyecto, selecciona especialistas y Skills, coordina la implementación y verifica resultados.

## Integración con asistentes e IDEs
La guía principal está en **[docs/integrations/README.md](docs/integrations/README.md)**. Incluye instrucciones actualizadas y un prompt base por asistente para:
- VS Code + GitHub Copilot.
- Visual Studio + GitHub Copilot.
- OpenAI Codex.
- Claude Code.
- Cursor.
- Gemini CLI.
- JetBrains Junie, incluido Android Studio.
- Windsurf / Devin Local.
- Cline.
- Roo Code.
- Continue.
- Aider.
- Zed.
- Otros IDEs sin adaptador nativo.

Cada guía describe rutas de configuración, cómo activar al Director, capacidades nativas, limitaciones y prompt para iniciar un proyecto.

## Estructura
- AGENTS.md: reglas globales y protocolo de orquestación.
- .agents/agents/: 18 perfiles especialistas.
- .agents/skills/: 57 Skills organizadas por dominio.
- .agents/workflows/: 8 procesos reutilizables.
- .agents/runtime/: especificación de arquitectura para un runtime opcional.
- docs/integrations/: guías y prompts por asistente.
- adapters/: prompt universal y guía de adaptación.
- templates/: solicitudes, handoffs, ADR y pull requests.
- scripts/: validaciones del framework.

## Inicio rápido
1. Copia AGENTS.md y .agents/ a la raíz de tu proyecto.
2. Abre docs/integrations/README.md.
3. Sigue la guía del asistente que vas a utilizar.
4. Combina las instrucciones con cualquier configuración existente, sin sobrescribirla.
5. Pega el prompt base de esa guía y describe qué quieres crear.

## Alcance honesto
Los perfiles Markdown son instrucciones y contratos de rol. La delegación paralela depende de que el asistente anfitrión soporte subagentes reales. Si no los soporta, el Director coordina secuencialmente. El framework no incluye un runtime autónomo propio.

## Validación
Ejecuta desde la raíz: `python scripts/validate_framework.py`. La validación comprueba estructura e inventario documental, no certifica compatibilidad funcional con cada asistente.

## Seguridad
Nunca subas secretos. No habilites permisos irrestrictos. Solicita aprobación para operaciones destructivas, externas o productivas.
