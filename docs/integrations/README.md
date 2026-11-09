# AI DEV TEAM | Guías de integración por asistente

**Investigación documental:** 9 de noviembre de 2026.  
**Objetivo:** instalar el mismo equipo AI DEV TEAM en el asistente que el usuario elija, sin obligarlo a usar un IDE, proveedor o motor propio.

## Orden recomendado

Antes de iniciar, puedes ordenar tu idea con [Prompt 0: consultor de ideas](../../prompts/00-project-consultant.md). Es opcional y solo prepara una descripción básica; no sustituye el análisis del Director ni define la arquitectura técnica.

La integración se hace en dos fases separadas. No empieces a desarrollar el producto durante la primera fase.

1. **Instala el núcleo en el proyecto:** copia `AGENTS.md` y la carpeta `.agents/` completa a la raíz del proyecto. No copies el repositorio entero ni su carpeta `.git/`. Consulta [la guía de instalación paso a paso](../PROJECT-BOOTSTRAP.md).
2. **Configura el asistente:** elige una guía de esta página y utiliza [Prompt 1: configurar el asistente](../../prompts/01-configure-assistant.md). El asistente debe crear o adaptar únicamente su configuración nativa, sin sobrescribir reglas existentes.
3. **Verifica:** confirma lectura del núcleo, Skills y Director; comprueba las capacidades reales del host y sus permisos.
4. **Inicia el proyecto:** utiliza [Prompt 2: iniciar el proyecto](../../prompts/02-start-project.md) e incorpora la descripción preparada con Prompt 0, si lo utilizaste. La configuración debe estar terminada antes de esta fase.

### Instalación del núcleo

Desde el repositorio AI_DEV_TEAM puedes usar el instalador:

```bash
python scripts/install_ai_dev_team.py --target "/ruta/al/proyecto" --dry-run
python scripts/install_ai_dev_team.py --target "/ruta/al/proyecto"
```

El instalador copia solo `AGENTS.md` y `.agents/`, preserva archivos idénticos, detecta conflictos y nunca sobrescribe por defecto. Si ya existe contenido, revisa los conflictos antes de combinar.

## Guías

| Asistente / entorno | Guía |
|---|---|
| VS Code + GitHub Copilot | [vscode-copilot.md](vscode-copilot.md) |
| Visual Studio + GitHub Copilot | [visual-studio-copilot.md](visual-studio-copilot.md) |
| OpenAI Codex (CLI y extensiones) | [openai-codex.md](openai-codex.md) |
| Claude Code | [claude-code.md](claude-code.md) |
| Cursor | [cursor.md](cursor.md) |
| Gemini CLI | [gemini-cli.md](gemini-cli.md) |
| JetBrains Junie (incluye Android Studio) | [jetbrains-junie.md](jetbrains-junie.md) |
| Windsurf / Devin Local | [windsurf-devin-local.md](windsurf-devin-local.md) |
| Cline | [cline.md](cline.md) |
| Roo Code | [roo-code.md](roo-code.md) |
| Continue | [continue.md](continue.md) |
| Aider | [aider.md](aider.md) |
| Zed | [zed.md](zed.md) |
| IDE sin adaptador nativo | [generic-ide.md](generic-ide.md) |

## Qué hace el Director

El asistente principal debe:
- Leer `AGENTS.md` y `.agents/agents/director.md`.
- Inspeccionar el proyecto y sus cambios actuales antes de tocar archivos.
- Elegir especialistas desde `.agents/agents/` y consultar Skills relevantes desde `.agents/skills/`.
- Dividir trabajo en tareas con objetivos, rutas permitidas, dependencias y criterios de aceptación.
- Usar subagentes reales solo si el host los ofrece y están habilitados.
- Si no hay subagentes, coordinar perfiles secuencialmente y decirlo.
- Implementar, probar, revisar el diff y entregar evidencias reales.

## Reglas de compatibilidad

- `AGENTS.md` y `.agents/skills/` son el núcleo compartido, pero cada host tiene su propio mecanismo de descubrimiento.
- No todos los hosts cargan automáticamente los perfiles de `.agents/agents/` como subagentes. En varios casos el Director debe leerlos como instrucciones y ejecutar los roles en secuencia.
- No confundas MCP con subagentes: MCP conecta herramientas y datos; no crea por sí mismo un equipo de agentes.
- No asumas que un archivo de configuración de otro producto funciona aquí.
- La disponibilidad de funciones depende de la versión, configuración, extensión, plan y permisos del host.

## Política de seguridad

Mantén el modo de aprobación del host. No actives permisos irrestrictos ni ejecuciones automáticas globales. No permitas cambios destructivos, despliegues, migraciones productivas, compras, publicación o envío de mensajes externos sin aprobación expresa.

## Referencias principales

- [VS Code: custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions)
- [VS Code: Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)
- [Codex: customization](https://learn.chatgpt.com/docs/customization/overview)
- [Claude Code: subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code: skills](https://code.claude.com/docs/en/skills)
- [Cursor: rules](https://cursor.com/docs/skills)
- [Cursor: rules](https://cursor.com/docs/rules)
- [Cursor: subagents](https://cursor.com/docs/subagents)
- [Gemini CLI: Skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md)
- [Gemini CLI: subagents](https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md)
- [Gemini CLI: settings](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/settings.md)
- [Junie: guidelines and memory](https://junie.jetbrains.com/docs/guidelines-and-memory.html)
- [Devin Local: customizations](https://docs.devin.ai/desktop/devin-local/customizations)
- [Cline: rules](https://docs.cline.bot/customization/cline-rules)
- [Roo Code: custom modes](https://docs.roocode.com/features/custom-modes)
- [Continue: rules](https://docs.continue.dev/customize/rules)
- [Aider: configuration](https://aider.chat/docs/config/options.html)
- [Zed: agent profiles](https://zed.dev/docs/ai/agent-profiles)
