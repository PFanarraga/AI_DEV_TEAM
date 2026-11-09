# Aider

## 1. Preparación

Aider es un agente de programación orientado a terminal. Usa archivos de convenciones indicados por `--read` o `--read-only`, y permite configurar instrucciones persistentes en `.aider.conf.yml` según la versión. Consulta la [referencia de opciones](https://aider.chat/docs/config/options.html).

Copia `AGENTS.md` y `.agents/` a la raíz. Crea un archivo `.aider.conf.yml` mínimo, sin reemplazar tu configuración de modelo:

```yaml
read:
  - AGENTS.md
  - .agents/agents/director.md
```

Si ya tienes `.aider.conf.yml`, añade esas rutas a la lista existente. Para iniciar, usa el modo Architect para discutir el diseño y después Code para editar. La opción exacta depende de la versión; los modos documentados son `ask`, `code` y `architect`.

Aider no debe considerarse un orquestador nativo de múltiples agentes. AI DEV TEAM opera como metodología de coordinación en el contexto principal; los perfiles se consultan como documentos. Si integras un orquestador externo, hazlo como componente separado.

## 2. Prompt base

```text
Actúa como Director de AI DEV TEAM usando Aider.

Quiero construir:
[DESCRIBE AQUÍ TU IDEA O PRODUCTO]

Lee AGENTS.md y .agents/agents/director.md como contexto de solo lectura. Inspecciona el repositorio, mapa de código, archivos, stack, dependencias, convenciones, estado Git y comandos de prueba.

Selecciona los perfiles relevantes de .agents/agents/ y lee las Skills necesarias de .agents/skills/. En Aider no simules subagentes: coordina las especialidades secuencialmente y registra qué responsabilidades asumiste.

Primero trabaja en modo Architect: convierte mi idea en requisitos, MVP, arquitectura, módulos, datos, interfaz, seguridad, pruebas y plan de implementación. Pregunta solo lo imprescindible y declara supuestos.

Cuando el plan esté claro, pasa a Code e implementa en archivos reales. Mantén cambios acotados, utiliza los patrones existentes, añade pruebas y ejecuta lint/build/test configurados. Si hay fallos, analiza la salida y corrige.

No borres ni reemplaces archivos ajenos al alcance. No hagas push, despliegues ni cambios externos sin aprobación. Revisa el diff y entrega resultados reales, archivos tocados y pendientes.
```

## 3. Verificación

Inicia Aider con el repositorio correcto. Comprueba que `AGENTS.md` y el perfil Director están en el contexto. Usa `/architect` para planificar y `/code` para implementar. Configura lint y test commands reales del proyecto.

## Fuentes

- https://aider.chat/docs/config/options.html
- https://aider.chat/docs/usage/modes.html
- https://aider.chat/docs/usage/lint-test.html
