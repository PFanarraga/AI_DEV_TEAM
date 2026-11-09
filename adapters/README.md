# Adaptadores de AI DEV TEAM

## Propósito
Conectar la fuente canónica de AI DEV TEAM con distintos IDEs, editores, asistentes y terminales. No se requiere motor propio para utilizar el framework: el asistente anfitrión actúa como Director.

## Instalación base
Copia a la raíz del proyecto:
- AGENTS.md
- .agents/

No renombres .agents/. Git admite directorios ocultos.

## Prompt universal de activación
Pega este prompt en el asistente que uses:

> Lee AGENTS.md y actúa como Director de AI DEV TEAM. Inspecciona el repositorio, el estado de Git, el stack, las instrucciones del host y las herramientas que realmente tienes disponibles. Consulta .agents/agents/director.md. Clasifica mi solicitud, selecciona solo los especialistas necesarios y lee sus perfiles y Skills relevantes. Antes de modificar archivos, presenta objetivo, alcance, tareas, dependencias, riesgos y criterios de aceptación. Si tienes subagentes reales, puedes delegar tareas independientes y reportar qué delegaste. Si no tienes subagentes, coordina a los especialistas secuencialmente sin simular procesos paralelos. No inventes herramientas, resultados, pruebas ni capacidades. Conserva mis cambios y solicita aprobación antes de operaciones destructivas, externas o productivas. Al finalizar, revisa el diff, ejecuta las pruebas disponibles y reporta comandos y resultados reales.

## Configuración por host
1. Identifica el archivo de instrucciones nativo del producto y su versión.
2. Crea o actualiza ese archivo para que haga referencia a AGENTS.md y active al Director.
3. Si el producto soporta reglas por proyecto, evita cambiar reglas globales del usuario.
4. Si ya existe configuración, no la reemplaces. Presenta un bloque de integración para combinar manualmente.
5. Carga Skills bajo demanda, no todo el catálogo en cada petición.
6. Habilita MCP y subagentes solo si el host los soporta y el usuario los autoriza.

## Hosts objetivo
La guía de compatibilidad está en docs/IDE-COMPATIBILITY.md. Incluye IDEs de JetBrains, VS Code, Visual Studio, Xcode, Eclipse, editores AI-first, asistentes de terminal y entornos cloud. La lista es una matriz de objetivos, no una certificación de integración de cada producto.

## Qué significa "funciona"
- Instrucciones cargadas: el host leyó el contexto.
- Skills accesibles: el Director puede leer las Skills requeridas.
- Herramientas disponibles: el host puede ejecutar acciones autorizadas.
- Delegación real: el host creó subagentes independientes y recibió sus resultados.
- Orquestación avanzada: el sistema conserva estado, permisos, cancelación y auditoría.

No confundir estos niveles. Si no hay subagentes, AI DEV TEAM sigue siendo utilizable mediante coordinación secuencial del asistente anfitrión.

## Seguridad
Nunca pegues claves o tokens en archivos de instrucciones. No otorgues acceso irrestricto al filesystem o shell. Revisa permisos y comandos antes de aprobar.
