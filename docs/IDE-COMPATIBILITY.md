# Portabilidad de AI DEV TEAM entre IDEs y asistentes

## Objetivo
Usar el mismo equipo de agentes con el asistente que el usuario prefiera, sin depender de un único editor, proveedor de modelos o runtime propio.

## Fuente canónica
- AGENTS.md: reglas y protocolo.
- .agents/agents/: perfiles.
- .agents/skills/: procedimientos técnicos.
- .agents/workflows/: procesos.
- templates/: formatos de tareas y handoffs.

El asistente anfitrión lee esta fuente y asume el rol Director. Los adaptadores son archivos nativos del host que apuntan a esa fuente.

## Adaptadores implementados en este repositorio
| Host | Archivo | Estado |
|---|---|---|
| GitHub Copilot (VS Code / Visual Studio / JetBrains con Copilot) | .github/copilot-instructions.md | Archivo creado; validar en cada host |
| OpenAI Codex | AGENTS.md | Convención de instrucciones |
| Cursor | AGENTS.md y .cursor/rules/ai-dev-team.mdc | Archivos creados |
| Claude Code | CLAUDE.md | Archivo creado |
| Gemini CLI | GEMINI.md | Archivo creado |
| Junie | .junie/AGENTS.md | Archivo creado |

La existencia del archivo no certifica que una versión específica lo cargue correctamente. Ejecutar checklist de humo en la instalación real.

## Familias adicionales
Visual Studio, JetBrains IDEs, Android Studio, Eclipse, NetBeans, Xcode, Windsurf, Zed, Cline, Roo Code, Continue, Aider, terminales y entornos remotos. Si el host no tiene adaptador implementado, se configura su archivo de instrucciones nativo o se utiliza el prompt universal de adapters/README.md.

## Niveles de compatibilidad
A. Instrucciones: carga AGENTS.md o un archivo nativo.
B. Skills: descubre o consulta archivos SKILL.md bajo demanda.
C. Herramientas: terminal, filesystem, Git, navegador o APIs con permisos.
D. Subagentes: delega agentes independientes y recibe resultados.
E. Orquestación avanzada: memoria persistente, estado, cancelación, ejecución aislada y auditoría.

Un nivel no implica los siguientes. Muchos entornos funcionan en A-C. D-E dependen de producto, versión, configuración y permisos.

## Estrategia
- Mantener un único núcleo canónico.
- Añadir archivos nativos solo cuando el host los necesite.
- No sobrescribir configuraciones existentes.
- Consultar documentación oficial vigente antes de crear nuevos adaptadores.
- Cargar Skills bajo demanda.
- Usar MCP solo cuando el host lo soporte y exista un servidor confiable.
- Delegar solo si hay subagentes reales.
- Mantener pruebas de instalación y actualización.

## Checklist por host
- [ ] Producto, versión y sistema operativo.
- [ ] Archivo nativo y método de carga confirmados.
- [ ] AGENTS.md y Director cargados.
- [ ] Skills pertinentes consultables.
- [ ] Herramientas probadas con permisos mínimos.
- [ ] Subagentes probados realmente o marcados no disponibles.
- [ ] Configuración previa preservada.
- [ ] Instalación, actualización y desinstalación documentadas.
- [ ] Pruebas de humo reproducibles.

## Documentación oficial de referencia
- VS Code custom instructions: https://code.visualstudio.com/docs/agent-customization/custom-instructions
- Copilot custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide
- Cursor rules: https://prod.cursor.com/docs/rules
- Gemini CLI GEMINI.md: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- Junie guidelines: https://junie.jetbrains.com/docs/guidelines-and-memory.html

Revisar estas fuentes periódicamente porque los formatos y capacidades evolucionan.
