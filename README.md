# AI DEV TEAM

Framework portable de ingeniería asistida por IA: **18 agentes, 57 Skills y 8 workflows** para proyectos web, móviles, desktop, backend, datos, IA, videojuegos, XR y e-commerce.

## Empieza aquí

El método recomendado tiene tres momentos: **definir la idea, instalar y configurar, después iniciar y desarrollar**.

1. **Ordena tu idea (recomendado):** usa [Prompt 0: consultor de ideas](prompts/00-project-consultant.md) en ChatGPT, Gemini, Claude u otra IA. Te ayudará a expresar lo básico del proyecto y generará un bloque inicial para el Director. No define la arquitectura ni sustituye a AI DEV TEAM.
2. Prepara la carpeta del proyecto.
3. Instala `AGENTS.md` y `.agents/` con el [instalador seguro](scripts/install_ai_dev_team.py).
4. Abre el proyecto en tu IDE/asistente y sigue [la guía de instalación](docs/PROJECT-BOOTSTRAP.md).
5. Ejecuta [Prompt 1: configurar el asistente](prompts/01-configure-assistant.md).
6. Verifica las capacidades reales del host.
7. Ejecuta [Prompt 2: iniciar el proyecto](prompts/02-start-project.md), incorporando el bloque generado por Prompt 0 si lo utilizaste.

### Instalar en Windows PowerShell

Desde la carpeta donde clonaste AI_DEV_TEAM:

```powershell
py .\scripts\install_ai_dev_team.py --target "D:\Proyectos\MiProyecto" --dry-run
py .\scripts\install_ai_dev_team.py --target "D:\Proyectos\MiProyecto"
```

El instalador copia solo el núcleo, no sobrescribe archivos y se detiene si detecta conflictos.

## Documentación

Consulta el [índice de documentación](docs/README.md), que organiza:
- [Bootstrap de proyectos](docs/PROJECT-BOOTSTRAP.md): instalación, configuración y verificación.
- [Integraciones](docs/integrations/README.md): 14 guías por IDE/asistente.
- [Compatibilidad](docs/IDE-COMPATIBILITY.md): matriz de capacidades y límites.
- [Prompts oficiales](prompts/): consultor de ideas, configuración e inicio.

## Estructura del repositorio

```text
AI_DEV_TEAM/
├── .agents/
│   ├── agents/       # 18 perfiles, incluido Director
│   ├── skills/       # 57 Skills
│   ├── workflows/    # 8 flujos de trabajo
│   └── runtime/      # especificación opcional, no runtime ejecutable
├── docs/             # documentación e integraciones
├── prompts/          # consultor, configuración e inicio
├── scripts/          # instalador y validador
├── templates/        # plantillas de tareas, handoffs y ADR
├── tests/            # pruebas automatizadas
└── AGENTS.md         # instrucciones canónicas
```

Los archivos de integración en la raíz (`CLAUDE.md`, `GEMINI.md`, `.cursor/`, `.github/` y `.junie/`) permiten probar AI_DEV_TEAM desde esos asistentes cuando abren este repositorio. **No se copian al proyecto destino**: allí el Prompt 1 prepara el adaptador mínimo que corresponda.

## Cómo trabaja el equipo

El asistente que elijas asume el rol de **Director**. Lee los perfiles pertinentes, selecciona Skills y coordina el trabajo. Los perfiles Markdown son instrucciones, no procesos autónomos. La delegación paralela depende de que el host ofrezca subagentes reales; de lo contrario, el Director coordina secuencialmente.

## Validar el repositorio

```bash
python scripts/validate_framework.py
python -m unittest discover -s tests -v
```

Estas comprobaciones validan estructura e instalador. No certifican que las 14 integraciones funcionen en todas las versiones de los asistentes: cada una debe probarse en su entorno real.

## Seguridad

No subas secretos ni habilites permisos irrestrictos. Conserva los archivos del proyecto, revisa el diff y solicita aprobación antes de operaciones destructivas, externas o productivas.
