# Tutorial maestro de AI DEV TEAM

## 1. Qué es
Framework portable con 18 agentes, 57 Skills, 8 workflows y adaptadores. El usuario trabaja con su asistente habitual; este asume el rol Director y coordina especialistas.

Los perfiles Markdown son instrucciones y contratos, no procesos autónomos. La delegación depende de que el host soporte subagentes reales. Sin esa capacidad, el Director coordina secuencialmente.

## 2. Integración por asistente
Consulta [docs/integrations/README.md](docs/integrations/README.md). Hay guías con configuraciones y prompts base para VS Code/Copilot, Visual Studio/Copilot, Codex, Claude Code, Cursor, Gemini CLI, Junie/Android Studio, Windsurf/Devin Local, Cline, Roo Code, Continue, Aider, Zed y otros IDEs.

## 3. Instalar en un proyecto
1. Copia `AGENTS.md` y `.agents/` a la raíz.
2. Abre la guía del asistente que usarás.
3. Copia o combina su archivo de instrucciones nativo. No sobrescribas configuraciones existentes.
4. Comprueba que el asistente puede leer el Director y las Skills.
5. Pega el prompt base de esa guía y describe tu proyecto.

## 4. Activar al Director
El Director inspecciona estructura, stack, scripts, pruebas y estado Git; identifica riesgos; selecciona agentes y Skills; presenta plan y criterios; solicita aprobación cuando corresponda.

## 5. Orquestación
- El usuario conversa con el asistente anfitrión.
- El Director define tareas y selecciona especialistas.
- Si el host ofrece subagentes reales, delega tareas independientes.
- Si no, coordina perfiles secuencialmente.
- El asistente anfitrión ejecuta las herramientas que tenga habilitadas.
- El Director integra y verifica resultados.

## 6. Seguridad y calidad
Nunca guardes secretos en el repositorio. Verifica autorización en servidor y base de datos. Añade pruebas de regresión. Solicita aprobación para acciones destructivas, externas y productivas. No confundas una prueba documentada con una prueba ejecutada.

## 7. Validación
Desde la raíz ejecuta: `python scripts/validate_framework.py`.
La validación comprueba estructura e inventario documental. No certifica compatibilidad funcional con cada IDE.
