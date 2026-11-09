# Tutorial maestro de AI DEV TEAM

## 1. Qué es
Framework portable con 18 agentes, 57 Skills, 8 workflows y adaptadores. El usuario trabaja con su asistente habitual; este asume el rol Director y coordina especialistas.

Los perfiles Markdown son instrucciones y contratos, no procesos autónomos. La delegación depende de que el host soporte subagentes reales. Sin esa capacidad, el Director coordina secuencialmente.

## 2. Flujo de trabajo obligatorio
El orden para cada proyecto es:

1. **Instalar:** copiar `AGENTS.md` y `.agents/` completa a la raíz del proyecto.
2. **Configurar:** abrir el proyecto en el asistente elegido y aplicar el adaptador nativo de su guía.
3. **Verificar:** comprobar lectura del núcleo, Skills, herramientas, permisos y delegación real.
4. **Iniciar:** enviar el prompt de inicio con la idea del proyecto.
5. **Desarrollar:** el Director inspecciona, planifica, coordina, implementa y verifica.

La guía detallada está en [docs/PROJECT-BOOTSTRAP.md](docs/PROJECT-BOOTSTRAP.md).

## 3. Instalar el núcleo
Desde el repositorio AI_DEV_TEAM:

```powershell
py scripts/install_ai_dev_team.py --target "D:\Proyectos\MiProyecto" --dry-run
py scripts/install_ai_dev_team.py --target "D:\Proyectos\MiProyecto"
```

También puedes copiar manualmente `AGENTS.md` y `.agents/`. No copies el repositorio completo ni su carpeta `.git/` dentro del proyecto.

El instalador no sobrescribe archivos existentes. Si detecta conflictos, detente y combina manualmente; usa `--skip-conflicts` solo si entiendes que esos archivos quedarán intactos y no se actualizarán.

## 4. Configurar el asistente
Consulta [docs/integrations/README.md](docs/integrations/README.md) y elige la guía de VS Code/Copilot, Visual Studio/Copilot, Codex, Claude Code, Cursor, Gemini CLI, Junie/Android Studio, Windsurf/Devin Local, Cline, Roo Code, Continue, Aider, Zed o IDE genérico.

Pega [Prompt 1: configurar el asistente](prompts/01-configure-assistant.md). Esta etapa no debe crear funcionalidades del producto ni modificar código funcional.

## 5. Iniciar el proyecto
Cuando la configuración esté verificada, pega [Prompt 2: iniciar el proyecto](prompts/02-start-project.md) o el prompt adaptado de la guía elegida. Describe la idea y las restricciones conocidas. El Director debe inspeccionar primero, presentar requisitos, arquitectura y plan, y esperar aprobación antes de modificar archivos funcionales.

## 6. Orquestación
- El usuario conversa con el asistente anfitrión.
- El Director define tareas y selecciona especialistas.
- Si el host ofrece subagentes reales, delega tareas independientes.
- Si no, coordina perfiles secuencialmente.
- El asistente anfitrión ejecuta las herramientas que tenga habilitadas.
- El Director integra y verifica resultados.

## 7. Seguridad y calidad
Nunca guardes secretos en el repositorio. Verifica autorización en servidor y base de datos. Añade pruebas de regresión. Solicita aprobación para acciones destructivas, externas y productivas. No confundas una prueba documentada con una prueba ejecutada.

## 8. Validación
Desde la raíz de AI_DEV_TEAM ejecuta: `python scripts/validate_framework.py`.
La validación comprueba estructura e inventario documental. No certifica compatibilidad funcional con cada IDE.
