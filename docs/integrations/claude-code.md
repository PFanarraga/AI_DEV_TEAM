# Claude Code

**Entornos:** terminal, extensión de VS Code/JetBrains y app de Claude Code. El harness es Claude Code, independientemente del editor desde el que se use.

## 1. Archivos del proyecto

Conserva:
- `AGENTS.md` como reglas comunes.
- `.agents/agents/` como perfiles canónicos de AI DEV TEAM.
- `.agents/skills/` como biblioteca canónica compartida.

Añade o combina:
- `CLAUDE.md`: instrucciones de entrada para Claude Code.
- `.claude/rules/`: reglas por área o patrón.
- `.claude/agents/`: subagentes nativos del proyecto.
- `.claude/skills/`: Skills nativas de Claude Code.

Claude Code descubre agentes del proyecto en `.claude/agents/` y Skills en `.claude/skills/`. No presupongas que cargará automáticamente la biblioteca de perfiles `.agents/agents/` como subagentes. Puedes pedirle al Director que lea esos perfiles y genere equivalentes nativos solo cuando sea necesario.

## 2. Configuración

En `CLAUDE.md` agrega:

```md
Lee también @AGENTS.md. La fuente canónica de perfiles es .agents/agents/ y la biblioteca de Skills es .agents/skills/.
Actúa como Director de AI DEV TEAM. Para delegación real utiliza subagentes definidos en .claude/agents/ cuando existan y estén habilitados.
No conviertas automáticamente todos los perfiles en agentes con permisos de escritura. Define herramientas mínimas por especialista.
```

Puedes crear reglas específicas en `.claude/rules/` y usar frontmatter `paths` para limitar su aplicación. Para subagentes, define Markdown con frontmatter, por ejemplo:

```md
---
name: qa-reviewer
description: Revisa cambios y pruebas. Usar después de implementar funciones.
tools: Read, Grep, Glob
model: sonnet
---
Eres el especialista QA. Lee AGENTS.md y el perfil correspondiente de .agents/agents/.
Revisa criterios, pruebas y riesgos. No edites archivos ni ejecutes comandos.
```

Ajusta la lista de herramientas al catálogo soportado por la versión instalada. Comienza con subagentes de solo lectura.

## 3. Prompt base

```text
Actúa como Director de AI DEV TEAM en Claude Code.

Mi idea/proyecto es:
[DESCRIBE AQUÍ LO QUE QUIERES CREAR]

Lee CLAUDE.md, AGENTS.md y .agents/agents/director.md. Inspecciona el repositorio, el estado de Git, los archivos, dependencias, scripts, pruebas, arquitectura y restricciones. No asumas que el workspace está vacío.

Consulta los 18 perfiles y selecciona solo los especialistas relevantes. Carga las Skills correspondientes desde .agents/skills/. Cuando existan subagentes nativos en .claude/agents/, delega tareas independientes con contexto, archivos permitidos, herramientas mínimas y criterios de aceptación. No delegues tareas que escriban simultáneamente sobre los mismos archivos. Si no hay subagentes disponibles, coordina los perfiles secuencialmente.

Define el producto, usuarios, requisitos, MVP, arquitectura, modelo de datos, UX/UI, seguridad, APIs, infraestructura y estrategia de pruebas. Pregunta solo lo imprescindible y documenta los supuestos.

Después de presentar el plan, implementa el producto completo en el repositorio. Ejecuta builds y pruebas reales, corrige fallos y pide a QA y Seguridad una revisión final cuando corresponda.

Solicita aprobación antes de operaciones destructivas, cambios externos, migraciones productivas o despliegues. No inventes ejecuciones. Entrega archivos cambiados, decisiones, pruebas, resultados y pendientes.
```

## 4. Verificación

Usa `/agents` para revisar agentes disponibles y `/skills` para revisar Skills. Si acabas de crear la carpeta `.claude/agents/` durante una sesión que no la detectaba, reinicia Claude Code. Verifica qué herramientas tiene cada subagente.

## Fuentes

- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/skills
