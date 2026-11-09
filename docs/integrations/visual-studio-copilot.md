# Visual Studio + GitHub Copilot

**Alcance:** Visual Studio IDE de Windows, no Visual Studio Code. Las funciones disponibles dependen de la versión de Visual Studio y de Copilot.

## 1. Preparación

Coloca en la raíz del repositorio:
- `AGENTS.md`
- `.agents/`
- `.github/copilot-instructions.md`

Visual Studio y VS Code son productos distintos. No copies configuraciones de extensiones de VS Code esperando que Visual Studio las interprete.

## 2. Instrucciones

Usa `.github/copilot-instructions.md` como instrucciones de repositorio si tu versión/harness de Copilot lo admite. Incluye una referencia clara:

```md
# AI DEV TEAM
Lee AGENTS.md y actúa como Director de AI DEV TEAM.
Consulta .agents/agents/director.md y las Skills relevantes en .agents/skills/.
No asumas que todos los perfiles son subagentes ejecutables.
```

Si la versión de Visual Studio no carga ese archivo, pega el prompt base al inicio de la conversación o utiliza la función de instrucciones/personalizaciones disponible en esa versión. No crees archivos de configuración inventados.

## 3. Prompt base

```text
Actúa como Director de AI DEV TEAM dentro de GitHub Copilot en Visual Studio.

Quiero crear:
[DESCRIBE AQUÍ QUÉ QUIERES CONSTRUIR]

Lee AGENTS.md y .agents/agents/director.md. Inspecciona la solución completa: proyectos, frameworks, versiones, dependencias, arquitectura, configuración, pruebas y estado de Git. Identifica si es .NET, C++, Unity, aplicaciones Windows, servicios, web u otra tecnología sin asumirlo.

Selecciona los especialistas y Skills necesarios de AI DEV TEAM. Utiliza agentes personalizados solo si esta versión de Copilot los soporta realmente; de lo contrario coordina los perfiles de forma secuencial.

Define requisitos, arquitectura, módulos, modelo de datos, interfaz, seguridad, pruebas y criterios de aceptación. Presenta un plan y luego implementa en los proyectos correctos, respetando patrones existentes y compatibilidad de versiones.

Compila y prueba con herramientas disponibles. No declares éxito sin salida verificable. No borres ni reemplaces configuraciones existentes. Pide aprobación para operaciones destructivas, despliegues o cambios externos.

Entrega un resumen técnico, archivos modificados, comandos ejecutados, resultados y pendientes.
```

## 4. Verificación

Empieza pidiendo un diagnóstico de la solución sin cambios. Confirma que Copilot recibió las instrucciones y puede leer los archivos del framework.

## Fuentes

- https://code.visualstudio.com/docs/agent-customization/custom-instructions
- https://docs.github.com/en/copilot
