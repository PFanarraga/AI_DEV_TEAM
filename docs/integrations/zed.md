# Zed Agent

## 1. Preparación

Zed Agent utiliza perfiles de agente y servidores MCP configurados en Zed. Los perfiles controlan herramientas disponibles; los permisos de herramientas controlan si una acción se confirma, permite o deniega. Consulta [Agent Profiles](https://zed.dev/docs/ai/agent-profiles) y [MCP](https://zed.dev/docs/ai/mcp).

Copia `AGENTS.md` y `.agents/` a la raíz. En el Agent Panel, abre el selector de perfiles y crea un perfil para AI DEV TEAM. Si tu versión no carga `AGENTS.md` automáticamente, incluye en las instrucciones del perfil la ruta al archivo y al Director.

No confundas el perfil Zed con un subagente: un perfil configura el comportamiento y herramientas del agente de Zed. Los agentes externos que se ejecutan vía ACP pueden tener sus propias configuraciones.

## 2. Permisos

Mantén `confirm` como comportamiento por defecto para herramientas que puedan cambiar archivos o ejecutar comandos. Crea un perfil de análisis con lectura habilitada y edición/terminal deshabilitadas. Habilita edición y terminal solo en el perfil de implementación y conserva confirmación.

MCP es opcional. No configures servidores con tokens en archivos compartidos ni concedas herramientas externas innecesarias.

## 3. Prompt base

```text
Actúa como Director de AI DEV TEAM en Zed Agent.

Quiero crear:
[DESCRIBE AQUÍ TU IDEA O PRODUCTO]

Lee AGENTS.md y .agents/agents/director.md. Inspecciona el repositorio, stack, arquitectura, estructura, estado Git, dependencias, scripts, pruebas y herramientas habilitadas en el perfil Zed actual.

Consulta los especialistas y Skills pertinentes en .agents/. Si el agente actual no dispone de subagentes, coordina las responsabilidades secuencialmente. No confundas perfiles de herramientas con subagentes independientes.

Define el producto, requisitos, MVP, arquitectura, interfaz, datos, APIs, seguridad, rendimiento, pruebas y despliegue. Presenta un plan y criterios verificables antes de modificar.

Después de mi aprobación, implementa el producto en el workspace. Utiliza solo herramientas disponibles en el perfil. Pide confirmación para acciones de riesgo, operaciones externas y despliegues. Ejecuta pruebas reales, revisa el diff y entrega el informe de resultados.
```

## 4. Verificación

Prueba el perfil Ask/solo lectura primero. Confirma las herramientas visibles, permisos y MCP disponibles. Para usar un agente externo desde Zed, consulta también la documentación del agente externo.

## Fuentes

- https://zed.dev/docs/ai/agent-profiles
- https://zed.dev/docs/ai/mcp
