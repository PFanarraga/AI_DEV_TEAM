# Workflow: Integración con IDE o asistente

## Activación
Instalar o adaptar AI DEV TEAM a un IDE, editor, terminal o asistente.

## Secuencia
1. Platform Integration identifica producto, versión, sistema operativo y capacidades disponibles.
2. Consultar documentación oficial vigente del host.
3. Confirmar cómo carga instrucciones, Skills, subagentes, MCP y herramientas.
4. Seleccionar adaptador nativo mínimo que apunte a la fuente canónica.
5. Detectar archivos de configuración existentes y no sobrescribirlos.
6. Proponer merge o backup antes de editar configuraciones del usuario.
7. Verificar que el host lea AGENTS.md y el perfil Director.
8. Probar un caso de solo lectura y otro de planificación.
9. Documentar funciones no soportadas y fallback secuencial.

## Gate
No afirmar compatibilidad completa basándose solo en que el IDE puede abrir Markdown. Distinguir lectura de instrucciones, carga de Skills, delegación real y acceso a herramientas.
