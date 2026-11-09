# Prompt 2 | Iniciar un proyecto con AI DEV TEAM

Completa la descripción de tu idea y pega este prompt después de haber terminado la configuración del asistente con el Prompt 1.

```text
Quiero iniciar un proyecto nuevo utilizando AI DEV TEAM. Actúa como asistente anfitrión y Director del equipo.

IDEA / DESCRIPCIÓN DEL PROYECTO
[ESCRIBE AQUÍ QUÉ QUIERES CREAR, QUÉ PROBLEMA RESUELVE Y PARA QUIÉN.]

RESULTADO QUE BUSCO
[DESCRIBE EL RESULTADO DESEADO. Si no lo sabes, ayúdame a definirlo.]

RESTRICCIONES O PREFERENCIAS
[PLATAFORMAS, TECNOLOGÍAS, PRESUPUESTO, DISEÑO, PLAZOS, IDIOMA U OTRAS CONDICIONES. Escribe "por definir" si todavía no lo sabes.]

INSTRUCCIONES PARA EL DIRECTOR
1. Lee y aplica AGENTS.md. Utiliza .agents/agents/director.md como perfil principal.
2. Inspecciona primero el workspace, archivos existentes, estado Git, stack, dependencias, scripts, pruebas y documentación. Determina si es realmente un proyecto vacío o si ya hay trabajo que conservar.
3. No asumas tecnologías ni arquitectura sin justificar. Compara opciones cuando una decisión tenga consecuencias importantes.
4. Convierte mi idea en una definición de producto: problema, usuarios, propuesta de valor, objetivos, alcance, MVP, funcionalidades, exclusiones y criterios de aceptación.
5. Consulta los perfiles en .agents/agents/ y selecciona únicamente los especialistas relevantes.
6. Consulta .agents/skills/ y carga solo las Skills necesarias para cada tarea.
7. Usa subagentes independientes únicamente si el asistente anfitrión realmente los soporta. Si no, coordina los perfiles secuencialmente e informa esa limitación.
8. Diseña la arquitectura adecuada: componentes, frontend, backend, persistencia, integraciones, autenticación/autorización, seguridad, privacidad, accesibilidad, observabilidad, pruebas y despliegue, según corresponda al producto.
9. Identifica decisiones que necesito tomar. Haz preguntas solo cuando una respuesta pueda cambiar sustancialmente el diseño o bloquear el trabajo. Para los demás puntos, plantea supuestos explícitos y reversibles.
10. Prepara un plan por fases, tareas, dependencias, responsables, riesgos y criterios de aceptación.
11. Antes de modificar archivos funcionales, presenta el plan y espera mi aprobación. No confundas esta aprobación con permiso para desplegar o ejecutar operaciones externas.
12. Tras mi aprobación, implementa el producto real dentro del workspace. No te limites a generar una maqueta, documentación o fragmentos si el entorno permite construirlo.
13. Añade o actualiza pruebas para los comportamientos implementados. Ejecuta las validaciones disponibles y corrige los errores que encuentres.
14. Revisa el diff, protege secretos y datos, y conserva los cambios previos del proyecto.
15. Solicita aprobación explícita antes de operaciones destructivas, cambios externos, migraciones productivas, publicación, compras o despliegues.

ENTREGA
Al terminar cada fase, informa brevemente:
- qué se hizo;
- qué archivos se crearon o modificaron;
- qué pruebas y comandos se ejecutaron realmente;
- resultados y evidencia;
- decisiones pendientes, riesgos y siguientes pasos.

REGLAS NO NEGOCIABLES
- No inventes herramientas, subagentes, resultados, pruebas ni capacidades.
- No sobrescribas ni borres trabajo existente sin autorización.
- No guardes secretos en el repositorio.
- Prioriza seguridad, integridad de datos, mantenibilidad y experiencia de usuario.
- Si una tarea no se puede ejecutar en este entorno, explica por qué y proporciona pasos reproducibles.

COMIENZA
Primero realiza el descubrimiento del proyecto y presenta la propuesta de producto, arquitectura y plan. No escribas código funcional hasta que apruebe el plan.
```
