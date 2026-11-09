# Cline

## 1. Preparación

Cline admite reglas persistentes de proyecto en `.clinerules/` o `.cline/rules/`. Su documentación también indica compatibilidad con `AGENTS.md` y reglas de Cursor/Windsurf. Puedes mantener `AGENTS.md` y agregar una regla Cline ligera.

Copia:
- `AGENTS.md`
- `.agents/agents/`
- `.agents/skills/`
- `.agents/workflows/`

Crea `.clinerules/ai-dev-team.md`:

```md
# AI DEV TEAM
Lee AGENTS.md y consulta .agents/agents/director.md.
Selecciona perfiles especialistas desde .agents/agents/ y carga las Skills relevantes leyendo .agents/skills/**/SKILL.md.
No supongas que cada perfil es un subagente nativo. Usa únicamente las funciones de delegación que esta versión ofrezca.
Respeta Plan/Act, aprobaciones, límites de herramientas y permisos del workspace.
```

Puedes dividir reglas con frontmatter `paths` para activar pautas por rutas. No dupliques la guía completa dentro de cada regla.

## 2. Herramientas y permisos

Cline puede operar en el editor y CLI, ejecutar comandos y usar MCP. Empieza en Plan mode para análisis y planificación; cambia a Act cuando apruebes la ejecución. Mantén confirmación de acciones. No habilites auto-approve general para shell, filesystem, red o cambios externos.

La documentación de Rules no equivale a una promesa de que Cline convierte automáticamente los 18 perfiles en subagentes. El Director debe coordinar especialistas usando la capacidad real disponible.

## 3. Prompt base

```text
Actúa como Director de AI DEV TEAM en Cline.

Quiero construir:
[DESCRIBE AQUÍ TU IDEA O PRODUCTO]

Lee AGENTS.md y .clinerules/ai-dev-team.md. Consulta .agents/agents/director.md. Inspecciona el repositorio, Git, stack, archivos, dependencias, arquitectura, comandos, pruebas y permisos disponibles.

Selecciona los especialistas necesarios desde .agents/agents/ y lee las Skills correspondientes en .agents/skills/. Usa cualquier mecanismo de delegación solo si está realmente disponible; si no, coordina secuencialmente.

Define requisitos, alcance, MVP, arquitectura, datos, diseño, APIs, seguridad, pruebas y despliegue. Explica supuestos y presenta un plan con fases, tareas y criterios de aceptación.

Primero trabaja en Plan mode. Cuando apruebe el plan, pasa a Act y construye el producto dentro del workspace. No te limites a escribir ejemplos. Mantén consistencia y prueba cada parte.

No ejecutes comandos destructivos, borres archivos, cambies servicios externos, migres producción ni despliegues sin aprobación. No inventes resultados. Revisa el diff, ejecuta pruebas reales y entrega el informe final.
```

## 4. Verificación

Abre el panel Rules de Cline y comprueba que detecta la regla. Pide una inspección de solo lectura. Verifica manualmente qué herramientas MCP y acciones requieren aprobación.

## Fuentes

- https://docs.cline.bot/customization/cline-rules
- https://cline.bot/
