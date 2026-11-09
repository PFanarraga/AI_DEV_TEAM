# VS Code + GitHub Copilot

**Estado documental:** adaptador nativo disponible. Confirmar el harness Copilot y la versión instalada.

## 1. Preparación del proyecto

En la raíz del proyecto coloca:
- `AGENTS.md`
- `.agents/agents/`
- `.agents/skills/`
- `.agents/workflows/`
- `.github/copilot-instructions.md`

VS Code documenta `.github/copilot-instructions.md` y `AGENTS.md` como ubicaciones de instrucciones de proyecto para Copilot. Los archivos de instrucciones no crean por sí solos agentes personalizados. Agent Skills son una capa diferente y se cargan bajo demanda en clientes compatibles. Consulta [Custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) y [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

## 2. Configuración

Si ya tienes `.github/copilot-instructions.md`, agrega una referencia a `AGENTS.md` sin borrar sus reglas. Puedes usar:

```md
# AI DEV TEAM
Lee AGENTS.md como fuente principal de reglas del proyecto.
Actúa como Director y consulta .agents/agents/director.md.
Carga los perfiles y Skills relevantes bajo demanda.
No simules subagentes: usa únicamente los agentes que Copilot realmente muestre y permita invocar.
```

Para Skills, conserva `.agents/skills/` en la raíz. En versiones compatibles de VS Code/Copilot se detectan Skills del estándar Agent Skills. Comprueba la vista de personalizaciones o el listado de Skills del host.

Los agentes personalizados de Copilot usan archivos propios del host, por ejemplo `.github/agents/*.agent.md`. No copies perfiles de AI_DEV_TEAM allí sin convertirlos al formato de Copilot y revisar herramientas y permisos.

## 3. Activación

1. Abre la carpeta raíz en VS Code.
2. Abre Copilot Chat y selecciona el modo Agent, no solo Ask.
3. Inicia una conversación nueva.
4. Pega el prompt base de abajo.
5. Comprueba que el asistente mencione el Director y rutas reales del repositorio.

## 4. Prompt base para crear un proyecto

```text
Actúa como el asistente principal y Director de AI DEV TEAM en GitHub Copilot Agent.

Quiero construir lo siguiente:
[DESCRIBE AQUÍ TU IDEA, PRODUCTO O PROBLEMA]

Lee AGENTS.md y .agents/agents/director.md. Inspecciona el repositorio, el estado de Git, los archivos existentes, las tecnologías, las dependencias y las herramientas disponibles. No asumas que el proyecto está vacío.

Coordina el trabajo con los 18 perfiles de AI DEV TEAM. Selecciona solo los especialistas necesarios y consulta sus Skills en .agents/skills/. Si esta sesión permite invocar agentes personalizados o subagentes, delega tareas independientes y explícame cuáles. Si no, coordina las especialidades secuencialmente sin fingir delegación.

Primero define el producto, usuarios, funcionalidades, arquitectura, stack, estructura, seguridad, datos, experiencia visual, pruebas y criterios de aceptación. Identifica preguntas imprescindibles; si algo no bloquea, declara una suposición razonable y continúa.

Presenta un plan por fases. Después implementa el proyecto en el workspace, no te limites a dar ejemplos o fragmentos. Mantén coherencia entre frontend, backend, base de datos, autenticación, infraestructura y documentación.

No inventes herramientas, archivos, pruebas ni resultados. Conserva mis cambios. Solicita mi aprobación antes de operaciones destructivas, despliegues, migraciones productivas, publicación o acciones externas.

Al finalizar ejecuta las pruebas disponibles, revisa el diff y entrega: funcionalidades implementadas, archivos creados/modificados, arquitectura, comandos ejecutados, resultados reales, limitaciones y siguientes pasos.
```

## 5. Limitaciones y verificación

Copilot en VS Code puede usar instrucciones, Skills y agentes personalizados según la versión y el harness. La carga de un modelo Anthropic dentro de Copilot no equivale a ejecutar Claude Code. Verifica el harness seleccionado.

Prueba primero una tarea de solo lectura: “Identifica el stack y enumera qué agentes y Skills de AI DEV TEAM aplicarías, sin modificar archivos”.

## Documentación oficial

- https://code.visualstudio.com/docs/agent-customization/custom-instructions
- https://code.visualstudio.com/docs/agent-customization/agent-skills
- https://code.visualstudio.com/docs/agents/guides/customize-copilot-guide
