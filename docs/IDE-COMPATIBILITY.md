# Compatibilidad e integración de AI DEV TEAM

## Propósito
Usar el mismo equipo de ingeniería con distintos asistentes, IDEs y entornos. El núcleo portable está formado por `AGENTS.md`, `.agents/agents/`, `.agents/skills/` y `.agents/workflows/`. Cada host requiere su propio mecanismo de configuración.

## Guías detalladas y prompts base
La fuente de verdad de las integraciones es [docs/integrations/README.md](integrations/README.md). Hay una guía independiente para VS Code/Copilot, Visual Studio/Copilot, Codex, Claude Code, Cursor, Gemini CLI, JetBrains Junie/Android Studio, Windsurf/Devin Local, Cline, Roo Code, Continue, Aider, Zed y un procedimiento genérico.

Cada guía incluye rutas, fragmentos de configuración, activación, prompt para construir proyectos y comprobaciones. Esta documentación se investigó con fuentes oficiales el 9 de noviembre de 2026. Como los productos cambian con frecuencia, consulta la documentación enlazada antes de copiar configuraciones a versiones futuras.

## Matriz de integración

| Host | Mecanismo principal | Skills | Delegación |
|---|---|---|---|
| VS Code + Copilot | `.github/copilot-instructions.md` o `AGENTS.md` | Agent Skills, si el harness lo admite | Agentes personalizados según versión |
| Visual Studio + Copilot | Instrucciones de repositorio soportadas por la versión | Depende del host | Depende del host |
| OpenAI Codex | `AGENTS.md` | `.agents/skills/` | Subagentes según producto/configuración |
| Claude Code | `CLAUDE.md`, `.claude/rules/` | `.claude/skills/` | `.claude/agents/` |
| Cursor | `AGENTS.md`, `.cursor/rules/*.mdc` | `.agents/skills/` | `.cursor/agents/` |
| Gemini CLI | `GEMINI.md`, `.gemini/settings.json` | Agent Skills | Subagentes nativos según versión |
| JetBrains Junie | `AGENTS.md`, `.junie/AGENTS.md` según host | Verificar versión | Verificar versión |
| Devin Local | `AGENTS.md`, `.devin/rules/` | `.agents/skills/` | Subagentes y plugins |
| Windsurf Cascade legado | Reglas y workflows heredados | Legacy | Legacy |
| Cline | `.clinerules/` o `.cline/rules/`, `AGENTS.md` | Consultar perfiles/Skills desde archivos | No asumir perfiles como subagentes |
| Roo Code | `.roomodes`, modos personalizados | Consultar desde `.agents/` según acceso | Tareas delegadas según herramientas/modos |
| Continue | `.continue/rules/`, `config.yaml` | Consultar desde archivos | No asumir subagentes |
| Aider | `--read`, `.aider.conf.yml` | Consultar desde archivos | No es orquestador multiagente nativo |
| Zed | Agent Profiles y settings | Consultar desde archivos cuando el agente tenga acceso | Depende de agente externo/ACP |

La tabla expresa el mecanismo documentado y no una certificación funcional realizada por el usuario. Un agente que puede leer un perfil no necesariamente lo ejecuta como subagente independiente.

## Niveles de capacidad

A. **Instrucciones:** el host carga reglas de proyecto.  
B. **Skills:** el host descubre o puede leer procedimientos bajo demanda.  
C. **Herramientas:** dispone de filesystem, terminal, Git, navegador o APIs con permisos.  
D. **Subagentes:** crea agentes independientes y recibe resultados.  
E. **Orquestación avanzada:** estado persistente, cancelación, sandbox y auditoría.

No inferir un nivel por el nombre del modelo ni del IDE. Verificarlo en la instalación concreta.

## Principios de integración

- Mantener un único núcleo canónico.
- Crear adaptadores nativos mínimos, no copias divergentes de todo el framework.
- No sobrescribir archivos de configuración existentes.
- Cargar solo las Skills relevantes para ahorrar contexto.
- MCP conecta herramientas externas; no sustituye la delegación.
- Respetar permisos, confirmaciones y aislamiento del host.
- No simular subagentes, comandos ni pruebas.
- Verificar documentación oficial y versión instalada antes de actualizar una guía.

## Checklist de comprobación para el usuario

- [ ] El asistente abre el workspace correcto.
- [ ] Carga las instrucciones de AI DEV TEAM.
- [ ] Puede leer `.agents/agents/director.md`.
- [ ] Puede localizar las Skills relevantes.
- [ ] Declara qué herramientas tiene habilitadas.
- [ ] Si afirma delegar, se observa una ejecución real de subagente.
- [ ] Las acciones de escritura y terminal requieren los permisos esperados.
- [ ] Puede ejecutar una tarea pequeña y reportar resultados verificables.

## Referencias oficiales

- VS Code: https://code.visualstudio.com/docs/agent-customization/custom-instructions
- VS Code Skills: https://code.visualstudio.com/docs/agent-customization/agent-skills
- Codex: https://learn.chatgpt.com/docs/customization/overview
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code Skills: https://code.claude.com/docs/en/skills
- Cursor rules: https://cursor.com/docs/rules
- Cursor Skills: https://cursor.com/docs/skills
- Cursor subagents: https://cursor.com/docs/subagents
- Gemini CLI Skills: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- Gemini CLI subagents: https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
- Junie: https://junie.jetbrains.com/docs/guidelines-and-memory.html
- Devin Local: https://docs.devin.ai/desktop/devin-local/customizations
- Cline: https://docs.cline.bot/customization/cline-rules
- Roo Code: https://docs.roocode.com/features/custom-modes
- Continue: https://docs.continue.dev/customize/rules
- Aider: https://aider.chat/docs/config/options.html
- Zed profiles: https://zed.dev/docs/ai/agent-profiles

## Nota sobre Windsurf
La documentación actual de Devin identifica Cascade como agente legado de Devin Desktop y documenta Devin Local como agente actual. No diseñar nuevas instalaciones basadas exclusivamente en workflows antiguos de Cascade. Consulta [la guía Windsurf/Devin Local](integrations/windsurf-devin-local.md).
