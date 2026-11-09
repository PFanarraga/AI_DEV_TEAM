# AI DEV TEAM | Reglas globales

## Alcance
Biblioteca documental de ingeniería asistida por IA con 12 agentes, 41 Skills únicas y 5 workflows. Incluye perfiles, criterios, procedimientos, plantillas y una especificación de orquestación. Los Markdown no ejecutan agentes ni crean concurrencia por sí solos; eso depende del IDE o runtime. Ver .agents/runtime/ORCHESTRATION.md.

## Reglas obligatorias
1. Inspeccionar estructura, stack, estado Git, convenciones y archivos afectados.
2. Definir alcance, riesgos y criterios de aceptación antes de implementar.
3. Pedir aprobación antes de cambios amplios, destructivos, migraciones irreversibles o despliegues.
4. Validar entradas y autorización en servidor; la validación del cliente no es frontera de seguridad.
5. Proteger secretos, datos personales y registros sensibles.
6. Usar unidades menores enteras o decimales exactos para dinero, nunca float binario.
7. Añadir o actualizar pruebas para cambios de comportamiento.
8. Revisar diff y reportar resultados reales, limitaciones y pendientes.
9. No borrar datos, cambiar permisos ni alterar producción sin autorización.

## Accesibilidad
- Declarar el nivel WCAG objetivo y no mezclar AA y AAA.
- AA: contraste 4.5:1 para texto normal y 3:1 para texto grande.
- AAA: contraste 7:1 para texto normal y 4.5:1 para texto grande.
- Componentes e información gráfica: 3:1 cuando aplique WCAG 1.4.11.
- Objetivo táctil recomendado: 44×44 CSS px. WCAG 2.2 AA 2.5.8 establece 24×24 CSS px con excepciones; AAA 2.5.5 establece 44×44 CSS px.
- Diseñar para teclado, foco visible, lectores de pantalla, zoom y movimiento reducido.

## Seguridad
OWASP Top 10:2025 es una guía de concienciación, no certificación. Adaptar controles al stack y modelo de amenazas. No exponer secretos. Aplicar mínimo privilegio, autorización del lado servidor, consultas parametrizadas y RLS cuando corresponda.

## Agentes (12)
Todos en .agents/agents/: director, architect, developer, desktop-developer, data-engineer, game-developer, tester, security, performance, ui-ux, visual-designer y researcher.

## Skills (41 únicas)
Todas en .agents/skills/, cada una con SKILL.md.
- Core y proceso (15): architecture, coding-standards, code-review, debugging, documentation, internationalization-i18n-localization, performance-basics, penetration-testing-owasp-top10, planning, project-discovery, release-checklist, security-basics, ui-accessibility, ui-ux-design, unit-testing.
- Backend (4): api-design-rest-graphql-grpc, authentication-authorization-rbac, database-design-migrations, realtime-websockets-queues.
- Frontend (4): design-systems-tailwind-shadcn, nextjs-react-fullstack, pwa-offline-first, state-management.
- Mobile (4): android-native-kotlin, cross-platform-react-native-flutter, ios-swift-swiftui, store-deployment-play-appstore.
- Desktop (1): desktop-electron-tauri.
- Data (2): data-pipelines-etl-elt, data-warehousing-analytics.
- DevOps (4): cicd-github-actions, cloud-infrastructure, docker-containerization, monitoring-observability-sentry.
- IA (3): agentic-workflows-mcp, llm-integration-langchain, rag-vector-databases.
- Gaming/XR (2): game-engine-unity-godot, spatial-computing-android-xr.
- E-commerce (2): in-app-purchases-revenuecat, payment-gateways.

## Workflows (5)
En .agents/workflows/: bug-fix.md, deployment.md, new-feature.md, refactoring.md y security-audit.md.

## Prioridad
Seguridad > Integridad de datos y dinero > Requisitos del usuario > Mantenibilidad > Rendimiento > Velocidad.
