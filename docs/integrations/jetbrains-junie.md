# JetBrains Junie (Android Studio incluido)

## 1. Alcance

Junie es el agente de JetBrains. Android Studio está basado en la plataforma IntelliJ, pero las funciones disponibles dependen de la versión del IDE y de la versión/plugin de Junie. Esta guía no afirma que todos los IDEs JetBrains tengan idénticas funciones.

## 2. Instrucciones del proyecto

Junie CLI documenta `AGENTS.md` y `.junie/AGENTS.md`. La guía oficial indica que Junie CLI lee `AGENTS.md` y puede detectar instrucciones de otros agentes para sugerir su importación. En Junie dentro del IDE, verifica el soporte de la versión instalada.

En la raíz conserva:
- `AGENTS.md`
- `.agents/agents/`
- `.agents/skills/`
- `.agents/workflows/`

Si el host no carga `AGENTS.md`, agrega las reglas a `.junie/AGENTS.md` sin borrar el contenido existente. Evita duplicar el documento completo: enlaza la fuente canónica y ordena al Director leerla.

## 3. Uso en Android Studio

1. Abre el proyecto Android desde la raíz del repositorio.
2. Comprueba que Junie esté instalado y habilitado.
3. Abre la configuración de guidelines/memory del proyecto.
4. Verifica qué archivo de instrucciones detecta la versión actual.
5. Inicia una conversación nueva y pega el prompt base.

Para Android nativo, el Director debe elegir Skills como `android-native-kotlin`, `unit-testing`, `integration-testing`, `ui-accessibility` y las de backend/seguridad que realmente correspondan. No fuerces Android si el proyecto requiere otra plataforma.

## 4. Prompt base

```text
Actúa como Director de AI DEV TEAM en JetBrains Junie.

Quiero crear:
[DESCRIBE AQUÍ TU IDEA O PRODUCTO]

Lee AGENTS.md y .agents/agents/director.md. Si Junie está usando .junie/AGENTS.md, integra esas reglas con la fuente común sin duplicarlas. Inspecciona la solución completa, módulos, plugins, versiones, dependencias, configuración, recursos, pruebas, estado Git y restricciones.

Selecciona los agentes y Skills de AI DEV TEAM pertinentes. Usa subagentes solo si Junie o el host actual ofrece delegación real; no supongas que los perfiles Markdown son agentes nativos. Si no hay delegación, coordina los roles por fases.

Define requisitos, arquitectura, módulos, navegación, datos, servicios, diseño UI/UX, accesibilidad, seguridad, pruebas y publicación. Si es Android, determina si corresponde Kotlin/Compose, XML, Room, servicios, permisos y compatibilidad con versiones reales del proyecto. Si es otra tecnología, respeta su stack.

Presenta el plan y luego implementa en los archivos correctos. Compila, ejecuta pruebas y analiza errores reales. No reemplaces configuraciones del IDE ni secretos. Pide aprobación antes de operaciones destructivas, cambios externos o publicación en tiendas.

Entrega archivos modificados, decisiones técnicas, compilación, pruebas, resultados y pendientes.
```

## 5. Verificación

Primero solicita un inventario de módulos y versiones sin editar. Comprueba que Junie haya leído las instrucciones y que puede ejecutar las tareas autorizadas.

## Fuente oficial

- https://junie.jetbrains.com/docs/guidelines-and-memory.html
- https://www.jetbrains.com/help/junie/
