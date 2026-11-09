# Tutorial maestro de AI DEV TEAM

## 1. Qué es
AI DEV TEAM es un framework portable con 18 agentes, 57 Skills, 8 workflows y plantillas. El usuario trabaja con el asistente que ya tiene en su IDE, editor, terminal o plataforma. Ese asistente asume el rol Director y coordina especialistas.

Los perfiles Markdown son instrucciones y contratos, no procesos autónomos. La delegación paralela depende de que el asistente anfitrión soporte subagentes reales. Sin esa capacidad, el Director coordina por etapas secuenciales.

## 2. Instalar en un proyecto
1. Copia AGENTS.md a la raíz del proyecto.
2. Copia la carpeta completa .agents/ a esa misma raíz.
3. Conserva nombres y jerarquía.
4. Consulta docs/IDE-COMPATIBILITY.md y adapters/README.md.
5. Configura el asistente anfitrión para cargar las instrucciones del repositorio.
6. Comprueba que puede leer AGENTS.md y los perfiles solicitados.

Git y GitHub admiten carpetas que comienzan con punto. No renombres .agents/.

## 3. Activar al Director
Usa el prompt de adapters/README.md. El Director inspecciona estructura, stack, scripts, pruebas y estado del repositorio; identifica riesgos; selecciona agentes y Skills; presenta plan y criterios; y solicita aprobación cuando corresponda.

## 4. Orquestación
- El usuario conversa con el asistente anfitrión.
- El Director define tareas y selecciona especialistas.
- Si el host ofrece subagentes reales, delega trabajos independientes.
- Si no, coordina cada especialista secuencialmente, sin fingir concurrencia.
- El asistente anfitrión ejecuta las herramientas que tenga habilitadas.
- El Director integra y verifica los resultados.

## 5. Especialistas
- Producto: .agents/agents/product-manager.md
- Arquitectura: .agents/agents/architect.md
- Frontend/fullstack: .agents/agents/developer.md
- Backend: .agents/agents/backend-engineer.md
- Android/iOS/multiplataforma: .agents/agents/developer.md + Skills mobile/
- Desktop: .agents/agents/desktop-developer.md
- Datos: .agents/agents/data-engineer.md
- Videojuegos/XR: .agents/agents/game-developer.md
- QA y automatización: .agents/agents/tester.md y qa-automation.md
- Seguridad: .agents/agents/security.md
- Rendimiento: .agents/agents/performance.md
- DevOps/SRE: .agents/agents/devops-sre.md
- IA/ML: .agents/agents/ai-ml-engineer.md
- Integración IDE/MCP: .agents/agents/platform-integration.md
- UX: .agents/agents/ui-ux.md
- Diseño visual: .agents/agents/visual-designer.md
- Investigación: .agents/agents/researcher.md

## 6. Workflows
- Descubrimiento: .agents/workflows/product-discovery.md
- Nueva función: .agents/workflows/new-feature.md
- Corrección: .agents/workflows/bug-fix.md
- Refactorización: .agents/workflows/refactoring.md
- Seguridad: .agents/workflows/security-audit.md
- Desarrollo multiagente: .agents/workflows/multi-agent-development.md
- Integración IDE: .agents/workflows/ide-integration.md
- Despliegue: .agents/workflows/deployment.md

## 7. Seguridad y calidad
Nunca guardes secretos en el repositorio. Verifica autorización en servidor y base de datos. Usa unidades menores enteras o decimales exactos para dinero. Añade pruebas de regresión. Ejecuta comandos reales y conserva evidencias. Solicita aprobación para acciones destructivas, externas y productivas.

## 8. Validación
Desde la raíz ejecuta: python scripts/validate_framework.py
La validación comprueba estructura, inventario y referencias documentales. No compila aplicaciones externas ni ejecuta agentes.
