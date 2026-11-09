# Documentación de AI DEV TEAM

Usa esta página como punto de entrada. Sigue el orden recomendado para evitar duplicar configuraciones.

## Ruta recomendada

1. [Preparar la idea con el consultor](../prompts/00-project-consultant.md) (opcional, antes de iniciar el proyecto).
2. [Instalar y configurar AI DEV TEAM en un proyecto](PROJECT-BOOTSTRAP.md).
3. [Elegir la guía del IDE o asistente](integrations/README.md).
4. [Verificar compatibilidad y capacidades](IDE-COMPATIBILITY.md).
5. [Configurar el asistente con Prompt 1](../prompts/01-configure-assistant.md).
6. [Iniciar el proyecto con Prompt 2](../prompts/02-start-project.md), usando la descripción preparada si se utilizó el consultor.

## Documentación por tema

| Documento | Contenido |
|---|---|
| [PROJECT-BOOTSTRAP.md](PROJECT-BOOTSTRAP.md) | Instalación segura del núcleo, adaptación, verificación y actualización |
| [integrations/README.md](integrations/README.md) | Índice de las 14 guías de asistentes |
| [IDE-COMPATIBILITY.md](IDE-COMPATIBILITY.md) | Matriz de instrucciones, Skills, herramientas y delegación |
| [../prompts/00-project-consultant.md](../prompts/00-project-consultant.md) | Consultor opcional para ordenar la idea y preparar la descripción inicial |
| [../prompts/01-configure-assistant.md](../prompts/01-configure-assistant.md) | Configuración del asistente anfitrión |
| [../prompts/02-start-project.md](../prompts/02-start-project.md) | Inicio del proyecto con el Director |

## Núcleo del framework

Los agentes, Skills y workflows son documentación operativa y se encuentran en `.agents/`. La especificación de orquestación está en `.agents/runtime/ORCHESTRATION.md`; no es un motor ejecutable.
