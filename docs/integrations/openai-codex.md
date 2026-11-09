# OpenAI Codex

**Entornos:** Codex CLI y experiencias de Codex que admitan instrucciones de proyecto. La interfaz y las funciones concretas dependen del producto y versión.

## 1. Preparación

Copia a la raíz:
- `AGENTS.md`
- `.agents/skills/`
- `.agents/agents/`
- `.agents/workflows/`

Codex utiliza `AGENTS.md` como guía persistente. La documentación actual de personalización también describe Skills, MCP y subagentes. Codex reconoce Skills de proyecto en `.agents/skills/`. Consulta [Codex customization](https://learn.chatgpt.com/docs/customization/overview).

## 2. Configuración recomendada

No necesitas un `config.toml` para que Codex lea el `AGENTS.md` del proyecto. Para configuración avanzada, abre la documentación de Codex correspondiente a tu instalación y configura MCP/proveedores/permisos de forma explícita. No pegues API keys en archivos versionados.

Mantén `.agents/skills/<skill>/SKILL.md` con frontmatter `name` y `description` válidos. Los perfiles de `.agents/agents/` son la biblioteca de roles de AI DEV TEAM; no asumas que Codex los convirtió automáticamente en subagentes nativos. Cuando la versión soporte subagentes, crea/ajusta las definiciones nativas siguiendo la documentación vigente.

## 3. Inicio

Abre Codex en la raíz del proyecto. Comprueba que está trabajando sobre el workspace correcto y que ha leído `AGENTS.md`. Pega:

```text
Actúa como Director de AI DEV TEAM usando OpenAI Codex.

Quiero crear:
[DESCRIBE AQUÍ TU IDEA]

Lee AGENTS.md y .agents/agents/director.md. Inspecciona el repositorio y detecta su estado, stack, arquitectura, dependencias, scripts, pruebas, documentación y cambios sin guardar.

Descubre las Skills disponibles en .agents/skills/ y carga las que correspondan. Selecciona especialistas leyendo sus perfiles en .agents/agents/. Usa subagentes nativos de Codex solo si esta versión los ofrece; delega tareas independientes con alcance y criterios definidos. Si no están disponibles, coordina secuencialmente y dilo.

Actúa como equipo profesional de producto e ingeniería: convierte mi idea en requisitos, define alcance MVP y evolución, diseña arquitectura, datos, interfaces, APIs, seguridad, despliegue y pruebas. Señala decisiones que necesitan mi aprobación y supuestos no confirmados.

Primero presenta un plan ejecutable y después construye el producto en este repositorio. No te limites a describir cómo hacerlo. Mantén cambios pequeños y revisables, agrega pruebas y documentación.

No ejecutes acciones destructivas, despliegues, migraciones de producción ni operaciones externas sin mi aprobación. Nunca inventes resultados. Ejecuta validaciones reales, revisa el diff y entrega un informe de cambios, pruebas, riesgos y pendientes.
```

## 4. Verificación

Pide a Codex que enumere las instrucciones y Skills que encontró. Para tareas multiagente, solicita evidencia de delegación real. La lectura de varios perfiles en una misma conversación no significa que se hayan iniciado subagentes.

## Fuentes

- https://learn.chatgpt.com/docs/customization/overview
- https://code.visualstudio.com/docs/agent-customization/custom-instructions
