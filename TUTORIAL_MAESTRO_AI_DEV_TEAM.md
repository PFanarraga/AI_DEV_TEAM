# Tutorial maestro de AI DEV TEAM

## 1. Qué es
AI DEV TEAM organiza el trabajo de ingeniería en 12 agentes, 41 Skills, 5 workflows y 4 plantillas.

**Importante:** los perfiles Markdown no son procesos ejecutables. Delegación automática, ejecución paralela, memoria compartida y herramientas requieren un runtime. La arquitectura objetivo está en .agents/runtime/ORCHESTRATION.md.

## 2. Instalar en un proyecto
1. Copia AGENTS.md a la raíz del proyecto.
2. Copia la carpeta completa .agents/ a esa misma raíz.
3. Conserva los nombres y la jerarquía internos.
4. Abre el proyecto en VS Code, Cursor, Windsurf, Android Studio u otro entorno compatible.
5. Comprueba que el asistente puede leer AGENTS.md y .agents/.

Git y GitHub admiten carpetas que comienzan con punto. No renombres .agents/ a agents/.

## 3. Activar al Director
Lee AGENTS.md y .agents/agents/director.md. Actúa como Director de AI DEV TEAM. Inspecciona estructura, stack, scripts, pruebas y estado del repositorio. Analiza mi solicitud, identifica riesgos, selecciona especialistas y Skills, presenta un plan con criterios de aceptación y espera mi aprobación. No inventes resultados ni afirmes delegación real si tu entorno no la soporta.

## 4. Invocar especialistas
- Arquitectura: .agents/agents/architect.md y .agents/skills/backend/database-design-migrations/SKILL.md
- Desarrollo fullstack: .agents/agents/developer.md y .agents/skills/frontend/nextjs-react-fullstack/SKILL.md
- Android: .agents/agents/developer.md y .agents/skills/mobile/android-native-kotlin/SKILL.md
- Desktop: .agents/agents/desktop-developer.md y .agents/skills/desktop/desktop-electron-tauri/SKILL.md
- Datos: .agents/agents/data-engineer.md y .agents/skills/data/data-pipelines-etl-elt/SKILL.md
- Videojuegos/XR: .agents/agents/game-developer.md y .agents/skills/gaming-xr/game-engine-unity-godot/SKILL.md
- QA: .agents/agents/tester.md y .agents/skills/core/unit-testing/SKILL.md
- Seguridad: .agents/agents/security.md y .agents/skills/core/penetration-testing-owasp-top10/SKILL.md
- Rendimiento: .agents/agents/performance.md y .agents/skills/core/performance-basics/SKILL.md
- UX: .agents/agents/ui-ux.md y .agents/skills/core/ui-accessibility/SKILL.md
- Diseño visual: .agents/agents/visual-designer.md
- Investigación: .agents/agents/researcher.md y .agents/skills/core/project-discovery/SKILL.md

Si el IDE no dispone de subagentes reales, ejecuta los perfiles secuencialmente o en conversaciones separadas. No confundas esa coordinación con concurrencia autónoma.

## 5. Workflows
- .agents/workflows/new-feature.md
- .agents/workflows/bug-fix.md
- .agents/workflows/refactoring.md
- .agents/workflows/security-audit.md
- .agents/workflows/deployment.md

Antes de desplegar, borrar datos, cambiar permisos o ejecutar migraciones productivas, solicita aprobación explícita.

## 6. Seguridad y calidad
Nunca guardes secretos en el repositorio. Verifica autorización en servidor y base de datos. Usa unidades menores enteras o decimales exactos para dinero. Añade pruebas de regresión. Ejecuta comandos reales y conserva evidencias. No declares WCAG AAA usando solo umbrales AA. La Skill AppSec usa OWASP Top 10:2025.

## 7. Validación
Desde la raíz ejecuta: python scripts/validate_framework.py
La validación comprueba estructura, inventario y referencias de Skills. No compila ni prueba aplicaciones externas.
