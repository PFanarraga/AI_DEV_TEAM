# Tutorial maestro de AI DEV TEAM

## 1. Qué es
Framework portable con 18 agentes, 57 Skills, 8 workflows y adaptadores para distintos asistentes. El usuario conversa con su asistente habitual; este asume el rol Director y coordina especialistas.

Los perfiles Markdown son instrucciones, no procesos autónomos. La delegación paralela depende de que el host soporte subagentes reales. Sin esa capacidad, el Director coordina secuencialmente.

## 2. Instalar en un proyecto
1. Copia AGENTS.md y la carpeta .agents/ a la raíz.
2. Copia el adaptador correspondiente desde este repositorio: CLAUDE.md, GEMINI.md, .cursor/, .github/ o .junie/.
3. Conserva la estructura de .agents/.
4. Consulta docs/IDE-COMPATIBILITY.md y adapters/README.md.
5. Comprueba que el asistente carga las instrucciones.
6. No sobrescribas archivos de configuración ya existentes: combina las reglas.

## 3. Activar al Director
Usa el prompt universal de adapters/README.md. El Director inspecciona estructura, stack, scripts, pruebas y estado del repositorio; identifica riesgos; selecciona agentes y Skills; presenta plan y criterios; y solicita aprobación cuando corresponda.

## 4. Orquestación
- El usuario conversa con el asistente anfitrión.
- El Director define tareas y selecciona especialistas.
- Si el host ofrece subagentes reales, delega trabajos independientes.
- Si no, coordina perfiles secuencialmente sin fingir concurrencia.
- El asistente anfitrión ejecuta las herramientas que tenga habilitadas.
- El Director integra y verifica los resultados.

## 5. Especialistas
- Producto: .agents/agents/product-manager.md
- Arquitectura: .agents/agents/architect.md
- Frontend/fullstack: .agents/agents/developer.md
- Backend: .agents/agents/backend-engineer.md
- Android/iOS/multiplataforma: developer.md + Skills mobile/
- Desktop: .agents/agents/desktop-developer.md
- Datos: .agents/agents/data-engineer.md
- Videojuegos/XR: .agents/agents/game-developer.md
- QA: .agents/agents/tester.md y qa-automation.md
- Seguridad: .agents/agents/security.md
- Rendimiento: .agents/agents/performance.md
- DevOps/SRE: .agents/agents/devops-sre.md
- IA/ML: .agents/agents/ai-ml-engineer.md
- Integración IDE/MCP: .agents/agents/platform-integration.md
- UX: .agents/agents/ui-ux.md
- Diseño visual: .agents/agents/visual-designer.md
- Investigación: .agents/agents/researcher.md

## 6. Workflows
Consulta .agents/workflows/ para descubrimiento, nuevas funciones, correcciones, refactorización, seguridad, desarrollo multiagente, integración IDE y despliegue.

## 7. Seguridad y calidad
Nunca guardes secretos en el repositorio. Verifica autorización en servidor y base de datos. Usa unidades menores enteras o decimales exactos para dinero. Añade pruebas de regresión. Solicita aprobación para acciones destructivas, externas y productivas.

## 8. Validación
Desde la raíz ejecuta: python scripts/validate_framework.py
La validación comprueba estructura, inventario y referencias documentales. No ejecuta agentes ni compila aplicaciones externas.
