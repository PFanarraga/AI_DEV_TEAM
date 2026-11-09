# AI DEV TEAM

Framework portable de ingeniería asistida por IA con **18 agentes, 57 Skills únicas y 8 workflows** para proyectos web, móviles, desktop, backend, datos, IA, videojuegos, XR y e-commerce.

## Método oficial: instalar primero, configurar después, desarrollar al final

Cada proyecto nuevo comienza copiando el núcleo canónico a su raíz:

- `AGENTS.md`
- `.agents/` completa

No hace falta copiar el repositorio AI_DEV_TEAM entero dentro del proyecto. Puedes instalar el núcleo manualmente o con el instalador seguro:

```powershell
py scripts/install_ai_dev_team.py --target "D:\Proyectos\MiProyecto" --dry-run
py scripts/install_ai_dev_team.py --target "D:\Proyectos\MiProyecto"
```

Después:
1. Abre el proyecto en el IDE/asistente elegido.
2. Sigue [la guía de instalación y bootstrap](docs/PROJECT-BOOTSTRAP.md).
3. Ejecuta [Prompt 1: configurar el asistente](prompts/01-configure-assistant.md).
4. Verifica las capacidades reales y el adaptador nativo.
5. Ejecuta [Prompt 2: iniciar el proyecto](prompts/02-start-project.md) o el prompt específico de la guía de tu asistente.

## Guías por asistente

Consulta [docs/integrations/README.md](docs/integrations/README.md). Hay guías para VS Code/Copilot, Visual Studio/Copilot, OpenAI Codex, Claude Code, Cursor, Gemini CLI, JetBrains Junie/Android Studio, Windsurf/Devin Local, Cline, Roo Code, Continue, Aider, Zed y otros IDEs.

## Qué contiene el framework

- `AGENTS.md`: reglas globales y protocolo de orquestación.
- `.agents/agents/`: 18 perfiles especialistas.
- `.agents/skills/`: 57 Skills organizadas por dominio.
- `.agents/workflows/`: 8 procesos reutilizables.
- `.agents/runtime/`: especificación de arquitectura para un runtime opcional.
- `docs/integrations/`: guías y prompts por asistente.
- `prompts/`: los dos prompts universales de configuración e inicio.
- `scripts/install_ai_dev_team.py`: instalador seguro del núcleo.
- `templates/`: solicitudes, handoffs, ADR y pull requests.

## Rol del asistente

El usuario conversa con el asistente que prefiera. Ese asistente asume el rol de **Director**, inspecciona el proyecto, selecciona especialistas y Skills, coordina la implementación y verifica resultados.

Los perfiles Markdown son instrucciones y contratos de rol. La delegación paralela depende de que el asistente anfitrión soporte subagentes reales. Si no los soporta, el Director coordina secuencialmente.

## Validación

Desde este repositorio ejecuta:

```bash
python scripts/validate_framework.py
```

La validación comprueba estructura e inventario documental. No certifica compatibilidad funcional con cada asistente. Cada integración debe probarse en la versión y configuración reales del host.

## Seguridad

Nunca subas secretos. No habilites permisos irrestrictos. Solicita aprobación para operaciones destructivas, externas o productivas. El instalador no sobrescribe archivos existentes.
