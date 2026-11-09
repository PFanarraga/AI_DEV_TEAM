# Cursor

## 1. Preparación

Cursor reconoce:
- `AGENTS.md` como instrucciones sencillas de proyecto.
- `.cursor/rules/*.mdc` como reglas del proyecto.
- `.cursor/agents/*.md` como subagentes personalizados.
- `.agents/skills/**/SKILL.md` como Agent Skills de proyecto.

Esto permite conservar directamente la biblioteca de Skills de AI DEV TEAM. Consulta [Rules](https://cursor.com/docs/rules), [Agent Skills](https://cursor.com/docs/skills) y [Subagents](https://cursor.com/docs/subagents).

## 2. Configuración

Abre la raíz del proyecto y verifica que existan `AGENTS.md`, `.agents/` y `.cursor/rules/ai-dev-team.mdc`.

Regla recomendada:

```md
---
description: AI DEV TEAM orchestration rules
alwaysApply: true
---
Lee AGENTS.md y consulta .agents/agents/director.md.
El Director selecciona especialistas de .agents/agents/ y Skills de .agents/skills/.
Para delegación independiente usa subagentes reales definidos en .cursor/agents/.
No simules delegación y no otorgues herramientas innecesarias.
```

Puedes crear subagentes con frontmatter nativo. Ejemplo de solo lectura:

```md
---
name: security-reviewer
description: Revisa riesgos de seguridad en cambios de código. Usar para auth, datos, pagos y APIs.
model: inherit
readonly: true
---
Lee AGENTS.md y el perfil security de AI DEV TEAM.
Analiza amenazas, controles de autorización, secretos y vulnerabilidades.
Entrega hallazgos con evidencia y severidad. No edites archivos.
```

Cursor permite crear subagentes desde Agent o escribirlos en `.cursor/agents/`. Empieza con especialistas de análisis y revisión; limita permisos para quienes no deban editar.

## 3. Activación

Abre Agent en Cursor, selecciona el modo adecuado y pega el prompt. Para proyectos grandes puedes usar Projects si están disponibles y permitir al coordinador dividir trabajo. La delegación y anidamiento dependen de versión, herramientas y permisos.

## 4. Prompt base

```text
Actúa como Director de AI DEV TEAM en Cursor Agent.

Quiero crear:
[DESCRIBE AQUÍ TU IDEA O PRODUCTO]

Lee AGENTS.md, .cursor/rules/ai-dev-team.mdc y .agents/agents/director.md. Inspecciona todo el repositorio, su estado Git, stack, dependencias, scripts, arquitectura, UI, backend, datos y pruebas existentes.

Utiliza las Skills de .agents/skills/ y elige especialistas de .agents/agents/. Si puedes invocar subagentes reales, crea o utiliza los especialistas necesarios y delega análisis o tareas independientes. Mantén separadas las escrituras concurrentes y devuelve los resultados al Director. Si no hay subagentes, coordina secuencialmente.

Diseña el producto de extremo a extremo: requisitos, usuarios, funcionalidades, arquitectura, tecnologías, modelo de datos, diseño visual, experiencia, seguridad, rendimiento, pruebas y despliegue. Define un MVP funcional y una hoja de ruta. Aclara supuestos y pregunta lo imprescindible.

Después del plan, implementa el producto en el workspace, conecta los módulos y no dejes botones o flujos ficticios. Ejecuta comandos y pruebas disponibles, corrige errores y revisa el diff.

No sobrescribas trabajo existente ni ejecutes operaciones destructivas o productivas sin aprobación. Informa exactamente qué agentes delegaste, archivos modificados, pruebas ejecutadas y resultados reales.
```

## 5. Verificación

Comprueba que Cursor detecta Skills en `.agents/skills/` y los subagentes en `.cursor/agents/`. En Cloud Agents, las Skills locales de usuario pueden requerir sincronización; para el equipo, prioriza Skills dentro del repositorio.

## Fuentes

- https://cursor.com/docs/rules
- https://cursor.com/docs/skills
- https://cursor.com/docs/subagents
