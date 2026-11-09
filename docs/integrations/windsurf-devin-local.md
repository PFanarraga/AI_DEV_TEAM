# Windsurf y Devin Local: estado y configuración actual

## Aviso de producto importante

La documentación vigente consultada indica que Cascade es el agente legado de Devin Desktop y que las conversaciones nuevas de Devin Desktop usan Devin Local. Por eso no recomiendo construir una integración nueva dependiendo de rutas o workflows exclusivos de Cascade. Si todavía usas Windsurf Editor/Cascade, revisa la versión instalada y conserva sus reglas existentes.

Fuentes:
- https://docs.devin.ai/desktop/devin-local/customizations
- https://docs.windsurf.com/windsurf/cascade/workflows

## 1. Devin Local

Devin Local comparte formato de personalización con Devin CLI y admite Rules, Skills, plugins, MCP, hooks y subagentes.

Copia:
- `AGENTS.md`
- `.agents/agents/`
- `.agents/skills/`
- `.agents/workflows/`

La documentación de Devin Local indica que lee `AGENTS.md` y descubre Skills desde `.agents/skills/`. Esto hace que el núcleo de AI DEV TEAM encaje directamente con su sistema de reglas y Skills.

Para instrucciones específicas, crea reglas en `.devin/rules/*.md`. Para reglas globales, existe `.devin/global_rules.md`. Evita copiar todo el framework dentro de una regla global; usa `AGENTS.md` como fuente principal.

Los MCP se configuran en `.devin/mcp_config.json` (compartido) o `.devin/mcp_config.local.json` (local, no versionado). Mantén aprobaciones activas y no guardes credenciales en el archivo compartido.

## 2. Windsurf Editor / Cascade legado

Cascade documentaba reglas, Skills y workflows propios; sus workflows se invocaban manualmente. La documentación actual de Devin marca Cascade como legado y los workflows Cascade no son compatibles con Devin Local. Para un entorno nuevo, migra procedimientos a Skills en lugar de depender de `.windsurf/workflows/`.

No crees nuevas reglas antiguas sin confirmar que tu versión de Windsurf sigue soportándolas. Si usas Windsurf Editor y el agente disponible carga `AGENTS.md` o reglas compatibles, configura el núcleo común mediante la guía del producto y prueba la lectura real.

## 3. Prompt base para Devin Local

```text
Actúa como Director de AI DEV TEAM en Devin Local.

Quiero construir:
[DESCRIBE AQUÍ TU IDEA O PRODUCTO]

Lee AGENTS.md y .agents/agents/director.md. Inspecciona el workspace, Git, stack, estructura, dependencias, scripts, pruebas, documentación y herramientas autorizadas.

Descubre las Skills desde .agents/skills/ y carga las relevantes. Selecciona especialistas desde .agents/agents/. Si Devin Local permite subagentes en esta sesión, delega tareas independientes con contratos, límites y criterios claros. No asumas que todos los perfiles son subagentes instalados.

Diseña el producto completo: requisitos, alcance MVP, arquitectura, UI/UX, datos, APIs, seguridad, integraciones, infraestructura, pruebas y despliegue. Divide el trabajo en tareas, evita colisiones de archivos y coordina las entregas.

Después de presentar el plan, implementa el proyecto. Usa herramientas y MCP solo con permisos concedidos. Ejecuta pruebas reales y revisa el diff. Mantén checkpoints cuando la plataforma los ofrezca.

No realices operaciones destructivas, despliegues o acciones externas sin mi aprobación. Reporta agentes realmente delegados, cambios, pruebas, resultados y riesgos.
```

## 4. Prompt base para Windsurf si tu versión conserva Cascade

```text
Actúa como Director de AI DEV TEAM en el agente disponible de Windsurf.

Quiero crear:
[DESCRIBE AQUÍ TU IDEA]

Lee AGENTS.md y .agents/agents/director.md si el agente los admite. Si no, utiliza las reglas de proyecto nativas que muestre la versión. Consulta los perfiles y Skills relevantes. Planifica primero, usa subagentes solo si existen realmente y coordina secuencialmente si no.

Inspecciona el proyecto, define requisitos, arquitectura, interfaz, datos, seguridad y pruebas. Presenta el plan y después implementa. No inventes capacidades ni resultados. Pide aprobación antes de operaciones destructivas o externas. Verifica el resultado y resume archivos, pruebas y pendientes.
```

## 5. Verificación

En Devin Local abre Customize y revisa Rules, Skills, MCPs, Hooks y Subagents que realmente se hayan cargado. Comprueba que AI DEV TEAM aparezca desde `.agents/skills/`. En Windsurf legado, comprueba las funciones disponibles en tu instalación antes de aplicar rutas antiguas.
