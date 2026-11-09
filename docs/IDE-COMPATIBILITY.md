# Portabilidad de AI DEV TEAM entre IDEs y asistentes

## Objetivo
Usar el mismo equipo de agentes con el asistente que el usuario prefiera, sin hacer que el framework dependa de un único editor, proveedor de modelos o runtime propio.

## Arquitectura portable
La fuente de verdad es:
- AGENTS.md: reglas generales y protocolo.
- .agents/agents/: perfiles de especialistas.
- .agents/skills/: procedimientos técnicos.
- .agents/workflows/: procesos.
- templates/: formatos de solicitud y handoff.

El asistente anfitrión lee esta fuente y asume el rol Director. Los adaptadores específicos solo enlazan el host con la fuente canónica.

## Niveles de compatibilidad
1. **Nivel A, instrucciones:** el host puede leer AGENTS.md o un archivo nativo que lo referencie.
2. **Nivel B, Skills:** el host puede descubrir/cargar archivos de Skills o el Director puede leerlos bajo demanda.
3. **Nivel C, herramientas:** el host tiene terminal, filesystem, Git, navegador u otras herramientas autorizadas.
4. **Nivel D, subagentes:** el host permite crear/delegar agentes independientes y recibir resultados.
5. **Nivel E, orquestación avanzada:** hay memoria persistente, estado, cancelación, ejecución aislada y permisos auditables.

No asumir que alcanzar un nivel implica los siguientes. Muchos entornos pueden operar útilmente en niveles A-C. Los niveles D-E dependen del producto, versión, configuración y plan.

## Familias de entornos a evaluar
- IDEs generales: Visual Studio Code, Visual Studio, JetBrains IDEs (IntelliJ IDEA, Android Studio, PyCharm, WebStorm, Rider), Eclipse, NetBeans y Xcode.
- Editores AI-first: Cursor, Windsurf, Zed y otros.
- Asistentes de código: GitHub Copilot, Claude Code, Gemini CLI, Cline, Roo Code, Continue, Aider y herramientas equivalentes.
- Terminales y entornos remotos: shells locales, SSH, devcontainers, Codespaces y entornos cloud.
- Plataformas de desarrollo web y low-code: cuando permitan instrucciones del proyecto, exportación de código o herramientas autorizadas.

Esta lista indica objetivos de evaluación, no certifica compatibilidad automática ni integración probada con cada producto.

## Estrategia de adaptadores
- Mantener un único núcleo canónico.
- Añadir archivos nativos solo cuando el host los necesite.
- Usar instrucciones nativas para apuntar a AGENTS.md y activar al Director.
- Cargar Skills bajo demanda según tarea.
- Conectar MCP solo si el host lo soporta y existe un servidor confiable.
- Delegar solo si el host ofrece subagentes reales.
- No sobrescribir reglas, permisos o configuraciones existentes.
- Mantener versiones y pruebas de instalación por adaptador.

## Límites importantes
- No existe un estándar universal que haga que todos los IDEs lean la carpeta .agents/ automáticamente.
- AGENTS.md es una convención útil, pero cada producto puede requerir una ruta o archivo propio.
- MCP normaliza acceso a herramientas, no el formato de agentes, memoria o delegación.
- Las capacidades cambian entre versiones y configuraciones; verificar documentación oficial antes de instalar.
- Un asistente que solo puede conversar y leer archivos no puede ejecutar herramientas ni delegar tareas reales.

## Checklist de certificación por host
- [ ] Producto, versión y sistema operativo documentados.
- [ ] Archivo de instrucciones nativo identificado.
- [ ] AGENTS.md y Director se cargan correctamente.
- [ ] Skills relevantes pueden consultarse.
- [ ] Herramientas probadas con permisos mínimos.
- [ ] Subagentes probados de verdad o marcados como no disponibles.
- [ ] Configuración existente preservada.
- [ ] Instalación, actualización y desinstalación documentadas.
- [ ] Pruebas de humo reproducibles y evidencia guardada.

## Referencias de configuración
Consulta adapters/README.md. Los adaptadores deben verificarse contra la documentación oficial vigente de cada host antes de publicar compatibilidad.
