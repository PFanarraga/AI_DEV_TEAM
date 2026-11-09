# IDE o asistente sin adaptador nativo

Esta guía sirve para cualquier entorno que permita conversar con un modelo y, opcionalmente, leer/escribir archivos o ejecutar comandos: Android Studio sin Junie, Xcode, Eclipse, NetBeans, editores, terminales, IDEs especializados y plataformas de desarrollo.

## 1. Preparación universal

Copia a la raíz del proyecto:
- `AGENTS.md`
- `.agents/agents/`
- `.agents/skills/`
- `.agents/workflows/`

No necesitas renombrar `.agents/`. Si el entorno tiene un archivo de instrucciones propio, añade una referencia a `AGENTS.md`. Si no lo tiene, pega el prompt base en una conversación nueva.

## 2. Detectar capacidades reales

Pide al asistente que confirme:
1. ¿Puede leer archivos del workspace?
2. ¿Puede crear y modificar archivos?
3. ¿Puede ejecutar terminal y pruebas?
4. ¿Puede acceder a Git?
5. ¿Puede consultar internet o documentación?
6. ¿Tiene MCP?
7. ¿Puede crear subagentes independientes?
8. ¿Puede mantener contexto entre sesiones?

No habilites herramientas que no necesitas. Si el asistente solo conversa, podrá producir arquitectura, código y archivos para copiar, pero no afirmar que modificó o probó el proyecto.

## 3. Prompt base universal

```text
Quiero que trabajes como el asistente principal y Director de AI DEV TEAM.

PROYECTO QUE QUIERO CREAR:
[DESCRIBE AQUÍ TU IDEA. EXPLICA QUÉ PROBLEMA RESUELVE Y PARA QUIÉN, SI LO SABES.]

RESULTADO QUE ESPERO:
Quiero que conviertas mi idea en un producto de software funcional, no solamente en una explicación, maqueta o conjunto de fragmentos. Puede ser una aplicación web, móvil, desktop, SaaS, API, automatización, videojuego, sistema empresarial, herramienta de IA o cualquier otro producto.

INSTRUCCIONES:
1. Lee AGENTS.md y .agents/agents/director.md.
2. Inspecciona el workspace y su estado actual antes de cambiar nada.
3. Detecta el stack y las herramientas disponibles; no impongas tecnologías sin justificar.
4. Consulta los perfiles de .agents/agents/ y selecciona los especialistas adecuados.
5. Consulta .agents/skills/ y carga solo las Skills pertinentes.
6. Declara qué herramientas y capacidades tienes realmente. No simules subagentes. Si puedes delegar, hazlo con tareas independientes; si no, coordina las especialidades secuencialmente.
7. Convierte la idea en requisitos, usuarios, funcionalidades, MVP, arquitectura, modelo de datos, interfaz, seguridad, pruebas, despliegue y documentación.
8. Pregunta únicamente por decisiones que bloqueen el diseño o puedan cambiar significativamente el producto. Para el resto, propone supuestos explícitos.
9. Presenta un plan por fases con criterios de aceptación.
10. Después de aprobar el plan, implementa los archivos reales del proyecto. Mantén coherencia entre módulos y evita funciones simuladas.
11. Ejecuta las pruebas, compilaciones y validaciones que realmente estén disponibles. Corrige errores y vuelve a probar.
12. Revisa los cambios y entrega un informe con archivos creados/modificados, comandos ejecutados, resultados, limitaciones, riesgos y siguientes pasos.

REGLAS:
- No borres trabajo existente ni sobrescribas archivos de configuración sin revisar.
- No inventes datos, herramientas, agentes, ejecuciones ni resultados.
- No expongas claves, tokens o secretos.
- No realices despliegues, migraciones productivas, compras ni acciones externas sin mi aprobación.
- Prioriza seguridad, integridad de datos, mantenibilidad y experiencia de usuario.
- Si no puedes ejecutar algo, explica exactamente qué falta y dame instrucciones reproducibles.

Empieza inspeccionando el proyecto y proponiendo el plan de construcción.
```

## 4. Resultado esperado

El asistente debe indicar qué partes puede ejecutar y cuáles requieren intervención manual. Un prompt no puede añadir capacidades que el IDE o modelo no tenga.
