# Gemini CLI

## 1. Preparación

Gemini CLI usa:
- `GEMINI.md` para contexto e instrucciones.
- `.gemini/settings.json` para configuración del workspace.
- Skills compatibles con Agent Skills.
- Definiciones de subagentes en los formatos y rutas que soporte la versión instalada.

Copia `AGENTS.md` y `.agents/` a la raíz del proyecto. Añade o combina `GEMINI.md` para indicar que debe leer el archivo común y el perfil Director.

## 2. Configuración recomendada

Contenido mínimo para `GEMINI.md`:

```md
Lee AGENTS.md como fuente de reglas del proyecto.
Actúa como Director de AI DEV TEAM y consulta .agents/agents/director.md.
Descubre Skills desde .agents/skills/ y actívalas cuando sean pertinentes.
Selecciona perfiles especialistas desde .agents/agents/.
Usa subagentes nativos solo cuando estén habilitados en esta instalación.
```

Gemini CLI documenta `~/.gemini/settings.json` para usuario y `.gemini/settings.json` para el workspace. No copies opciones experimentales de ejemplos antiguos: revisa la referencia de la versión instalada. La configuración de seguridad y aprobación debe mantenerse restrictiva; no actives YOLO para un repositorio con datos importantes.

Las Skills se pueden listar con `/skills list`; para enlazar una carpeta de Skills local existe el comando `/skills link <path> --scope workspace` cuando esté disponible. Consulta la documentación de Skills actual.

## 3. Prompt base

```text
Actúa como Director de AI DEV TEAM usando Gemini CLI.

Quiero construir:
[DESCRIBE AQUÍ TU IDEA]

Lee GEMINI.md, AGENTS.md y .agents/agents/director.md. Inspecciona el repositorio y detecta tecnologías, estructura, estado Git, dependencias, herramientas, scripts, pruebas, restricciones y cambios existentes.

Descubre las Skills de AI DEV TEAM en .agents/skills/ y carga las pertinentes. Selecciona especialistas de .agents/agents/. Si Gemini CLI dispone de subagentes habilitados, delega tareas independientes a agentes especializados con alcance, herramientas y criterios definidos. Usa @nombre solo cuando el subagente exista. Si no hay delegación, trabaja por etapas secuenciales y dilo.

Conduce el proyecto como un equipo profesional: define requisitos, usuarios, MVP, arquitectura, diseño, datos, backend, frontend o app, seguridad, infraestructura, pruebas y documentación. Propón un plan con dependencias y criterios verificables.

Implementa en el workspace después del plan. Ejecuta las pruebas y comandos que realmente estén disponibles. Corrige fallos, revisa el diff y entrega evidencia.

No inventes agentes, herramientas ni resultados. No borres datos, publiques, despliegues ni cambies servicios externos sin aprobación expresa. Protege secretos y archivos ignorados.
```

## 4. Verificación

En una sesión nueva:
- Comprueba `/skills list`.
- Revisa qué subagentes están habilitados.
- Pide un análisis de solo lectura del proyecto.
- Verifica que el agente no asuma permisos no concedidos.

## Fuentes

- https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md
- https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
- https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/settings.md
- https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/configuration.md
