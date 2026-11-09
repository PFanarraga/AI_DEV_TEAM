# Continue

## 1. Preparación

Continue utiliza reglas de proyecto en `.continue/rules/`. También ofrece configuración de agentes, modelos, prompts y herramientas MCP a través de sus formatos vigentes de configuración. Consulta [Rules](https://docs.continue.dev/customize/rules) y [config.yaml reference](https://docs.continue.dev/reference).

Copia `AGENTS.md` y `.agents/` a la raíz. Crea `.continue/rules/ai-dev-team.md`:

```md
# AI DEV TEAM
Lee AGENTS.md y consulta .agents/agents/director.md.
Selecciona perfiles de .agents/agents/ y carga Skills pertinentes leyendo .agents/skills/.
Usa únicamente herramientas y modos disponibles en Continue. No simules subagentes.
Inspecciona el proyecto antes de editar, planifica, implementa, prueba y revisa el diff.
Pide aprobación para operaciones destructivas y externas.
```

En versiones recientes, Continue usa `config.yaml` para configurar modelos, reglas y herramientas. No reemplaces la configuración de modelos existente. Añade solo reglas o herramientas necesarias y conserva los proveedores ya configurados.

No asumas que Continue ejecuta los 18 perfiles como subagentes. El Director puede consultar los perfiles como guías y orquestar de forma secuencial. Si tu versión añade una capacidad de delegación, documenta y prueba esa función por separado.

## 2. Prompt base

```text
Actúa como Director de AI DEV TEAM en Continue.

Quiero construir:
[DESCRIBE AQUÍ TU IDEA O PRODUCTO]

Lee AGENTS.md, .continue/rules/ai-dev-team.md y .agents/agents/director.md. Inspecciona el repositorio, stack, estructura, dependencias, arquitectura, comandos, pruebas, estado Git y herramientas disponibles.

Consulta perfiles en .agents/agents/ y Skills en .agents/skills/. Selecciona solo los especialistas necesarios. Si esta versión no tiene subagentes reales, coordina los roles por fases sin simular delegación.

Convierte mi idea en especificaciones, MVP, arquitectura, diseño, modelo de datos, APIs, seguridad, pruebas y despliegue. Identifica requisitos imprescindibles y supuestos. Presenta un plan y criterios de aceptación.

Después implementa la solución completa en el workspace. Respeta la configuración actual de modelos y herramientas. Ejecuta pruebas disponibles y corrige errores. No inventes ejecuciones ni resultados.

No borres archivos ni realices acciones externas, migraciones productivas o despliegues sin aprobación. Revisa el diff y entrega el resumen técnico, pruebas y pendientes.
```

## 3. Verificación

Confirma que la regla aparece activa en Agent, Chat o Edit según tu versión. Comprueba el proveedor de modelo y herramientas antes de autorizar ejecución de comandos.

## Fuentes

- https://docs.continue.dev/customize/rules
- https://docs.continue.dev/reference
