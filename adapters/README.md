# Adaptadores de AI DEV TEAM

La documentación actualizada de integración y los prompts específicos por asistente se encuentran en:

**[docs/integrations/README.md](../docs/integrations/README.md)**

Incluye guías para VS Code/Copilot, Visual Studio/Copilot, OpenAI Codex, Claude Code, Cursor, Gemini CLI, JetBrains Junie/Android Studio, Windsurf/Devin Local, Cline, Roo Code, Continue, Aider, Zed y otros IDEs.

## Núcleo común

Copia a la raíz de cada proyecto:
- `AGENTS.md`
- `.agents/`

No renombres `.agents/`. Conserva los perfiles, Skills y workflows. Añade el adaptador nativo indicado por la guía del host y combina reglas existentes sin sobrescribirlas.

## Prompt universal de activación

Cuando el asistente no detecte automáticamente las instrucciones, usa el prompt base de [generic-ide.md](../docs/integrations/generic-ide.md).

## Principios

- El asistente anfitrión asume el rol Director.
- El Director lee perfiles y Skills relevantes, y selecciona especialistas.
- Solo se afirma delegación cuando el host crea subagentes reales.
- Si no hay subagentes, coordina de forma secuencial.
- MCP conecta herramientas, no crea por sí mismo subagentes.
- Cada integración debe verificarse en la versión y configuración real del usuario.
- No conceder permisos irrestrictos ni ejecutar operaciones destructivas o productivas sin aprobación.
