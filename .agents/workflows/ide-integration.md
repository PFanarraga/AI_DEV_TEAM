# Workflow: Integración con IDE o asistente

## Activación
Instalar o adaptar AI DEV TEAM a un IDE, editor, terminal o asistente.

## Secuencia obligatoria
1. Instalar primero el núcleo canónico en la raíz del proyecto: `AGENTS.md` y `.agents/`.
2. Platform Integration identifica producto, versión, sistema operativo y capacidades disponibles.
3. Consultar documentación oficial vigente del host y la guía correspondiente en `docs/integrations/`.
4. Confirmar cómo carga instrucciones, Skills, perfiles, subagentes, MCP y herramientas.
5. Seleccionar el adaptador nativo mínimo que apunte a la fuente canónica.
6. Detectar archivos de configuración existentes. No sobrescribirlos ni eliminarlos.
7. Proponer combinación o backup antes de editar configuraciones del usuario.
8. Verificar que el host lea `AGENTS.md`, `.agents/agents/director.md` y al menos una Skill relevante.
9. Probar una tarea de solo lectura y otra de planificación, sin tocar el código funcional.
10. Documentar funciones no soportadas y fallback secuencial.
11. Cerrar la fase de integración y esperar el prompt de inicio del proyecto.

## Prompts oficiales
Los prompts de las fases 1 (configurar asistente) y 2 (iniciar proyecto) se mantienen en el repositorio central AI_DEV_TEAM. No se copian al proyecto junto con el núcleo; consulta `prompts/01-configure-assistant.md` y `prompts/02-start-project.md` en el repositorio fuente.

## Gate
No afirmar compatibilidad completa basándose solo en que el IDE puede abrir Markdown. Distinguir lectura de instrucciones, carga de Skills, delegación real y acceso a herramientas. La instalación/configuración no autoriza a comenzar el desarrollo del producto.
