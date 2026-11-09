# Roo Code

## 1. Preparación

Roo Code permite modos personalizados globales y de proyecto. La configuración del proyecto se guarda en `.roomodes` en la raíz; los modos globales se gestionan desde el panel de Modes. Consulta [Customizing Modes](https://docs.roocode.com/features/custom-modes).

Copia `AGENTS.md` y `.agents/` a la raíz. Crea un modo Director desde el panel Roo Code → Mode → Edit Project Modes, o pídele a Roo que lo genere. No sustituyas los modos existentes.

## 2. Ejemplo de modo Director

Este es un modo de coordinación con herramientas amplias. Revísalo y limita grupos según tu nivel de confianza antes de usarlo:

```yaml
customModes:
  - slug: ai-dev-team-director
    name: AI DEV TEAM Director
    description: Coordina el equipo de agentes y Skills del proyecto.
    roleDefinition: >-
      Eres el Director de AI DEV TEAM. Lee AGENTS.md y
      .agents/agents/director.md. Inspecciona el proyecto, selecciona
      especialistas y Skills, planifica, coordina, verifica y reporta.
    whenToUse: Para crear productos, planificar funciones o coordinar tareas de ingeniería.
    customInstructions: >-
      Consulta perfiles en .agents/agents/ y Skills en .agents/skills/.
      Usa delegación Boomerang/Task solo cuando la función esté disponible.
      Si no, coordina secuencialmente. No inventes agentes ni resultados.
      Solicita aprobación para acciones destructivas o externas.
    groups:
      - read
      - edit
      - command
```

Si quieres modo de solo análisis, crea otro con `groups: [read]`. Roo soporta custom modes con restricciones de archivos y herramientas. No des permisos de comando a un modo de auditoría.

## 3. Prompt base

```text
Actúa como Director de AI DEV TEAM en Roo Code usando el modo Director.

Quiero crear:
[DESCRIBE AQUÍ TU IDEA]

Lee AGENTS.md y .agents/agents/director.md. Inspecciona el repositorio, Git, tecnologías, dependencias, arquitectura, scripts, pruebas, estructura y permisos disponibles.

Selecciona los perfiles especialistas y Skills pertinentes desde .agents/. Si Roo dispone de tareas Boomerang/subagentes en este modo, delega análisis y trabajos independientes con contexto y criterios. No ejecutes escrituras simultáneas sobre los mismos archivos. Si no hay delegación, coordina por etapas.

Diseña el producto completo con requisitos, MVP, arquitectura, experiencia de usuario, modelo de datos, APIs, seguridad, rendimiento, pruebas y despliegue. Presenta el plan antes de implementar.

Después de mi aprobación, implementa la solución real en el workspace. Ejecuta comandos permitidos, pruebas y builds. Corrige fallos y revisa el diff.

No asumas permisos que no te concedí. No borres archivos, cambies producción ni hagas despliegues sin aprobación. Entrega evidencia, archivos modificados, resultados y pendientes.
```

## 4. Verificación

Comprueba que Roo muestra el modo `AI DEV TEAM Director`. Prueba primero en modo read-only y verifica las herramientas asignadas. La sintaxis YAML puede evolucionar; si la interfaz de Roo genera un formato diferente, prioriza el archivo generado por tu versión.

## Fuentes

- https://docs.roocode.com/features/custom-modes
- https://docs.roocode.com/features/boomerang-tasks
