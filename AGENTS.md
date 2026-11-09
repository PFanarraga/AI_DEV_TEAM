# AI DEV TEAM | Reglas globales

## Alcance
Framework de ingeniería asistida por IA con 18 agentes, 57 Skills únicas y 8 workflows. La fuente canónica es este archivo más .agents/. Los adaptadores conectan esa fuente a asistentes e IDEs. Los perfiles Markdown no ejecutan procesos por sí solos: la delegación real depende del host o de un runtime opcional. Ver .agents/runtime/ORCHESTRATION.md y docs/IDE-COMPATIBILITY.md. Para cada proyecto, instala primero este archivo y .agents/ en la raíz, configura el asistente y solo después inicia el desarrollo siguiendo docs/PROJECT-BOOTSTRAP.md.

## Principios obligatorios
1. Inspeccionar estructura, stack, estado Git, convenciones y archivos afectados antes de actuar.
2. Definir objetivo, alcance, riesgos y criterios de aceptación.
3. El Director coordina el trabajo y selecciona solo los especialistas necesarios.
4. El asistente anfitrión debe declarar honestamente si puede delegar subagentes, ejecutar herramientas, usar MCP o trabajar solo secuencialmente.
5. No afirmar que se ejecutó una herramienta, prueba, build, agente o despliegue sin evidencia real.
6. Pedir aprobación antes de cambios amplios, destructivos, migraciones irreversibles, operaciones externas o despliegues.
7. Validar entradas y autorización en servidor; la validación del cliente no es frontera de seguridad.
8. Proteger secretos, datos personales y registros sensibles.
9. Usar unidades menores enteras o decimales exactos para dinero, nunca float binario.
10. Añadir o actualizar pruebas para cambios de comportamiento.
11. Revisar diff y reportar resultados reales, limitaciones y pendientes.
12. No borrar datos, cambiar permisos ni alterar producción sin autorización.

## Protocolo de orquestación con el asistente anfitrión
- El usuario habla con el asistente disponible en su IDE, editor, terminal o plataforma.
- Ese asistente asume el rol de Director leyendo .agents/agents/director.md.
- El Director inspecciona el proyecto, clasifica la solicitud, consulta perfiles y Skills y propone un plan.
- Si el host dispone de subagentes reales, delega tareas independientes con contratos y permisos explícitos.
- Si no dispone de subagentes, coordina especialistas de forma secuencial en el mismo contexto o en sesiones separadas, sin simular concurrencia.
- Las decisiones, handoffs, cambios y evidencias se consolidan en el contexto del proyecto.
- Las herramientas y permisos los concede el host/runtime; los Markdown no pueden concederlos por sí solos.
- MCP es una vía de interoperabilidad de herramientas, no un requisito ni un motor universal de agentes.

## Agentes (18)
En .agents/agents/:
director, architect, developer, desktop-developer, data-engineer, game-developer, tester, security, performance, ui-ux, visual-designer, researcher, product-manager, backend-engineer, devops-sre, ai-ml-engineer, platform-integration y qa-automation.

## Skills (57 únicas)
Cada Skill contiene SKILL.md en .agents/skills/.
- Core (15): architecture, code-review, coding-standards, debugging, documentation, internationalization-i18n-localization, penetration-testing-owasp-top10, performance-basics, planning, project-discovery, release-checklist, security-basics, ui-accessibility, ui-ux-design, unit-testing.
- Backend (5): api-design-rest-graphql-grpc, api-integration-testing, authentication-authorization-rbac, database-design-migrations, realtime-websockets-queues.
- Frontend (4): design-systems-tailwind-shadcn, nextjs-react-fullstack, pwa-offline-first, state-management.
- Mobile (4): android-native-kotlin, cross-platform-react-native-flutter, ios-swift-swiftui, store-deployment-play-appstore.
- Desktop (1): desktop-electron-tauri.
- Data (2): data-pipelines-etl-elt, data-warehousing-analytics.
- DevOps (7): backup-disaster-recovery, cicd-github-actions, cloud-infrastructure, docker-containerization, infrastructure-as-code, monitoring-observability-sentry, secrets-management.
- AI (5): agentic-workflows-mcp, llm-evaluation-guardrails, llm-integration-langchain, prompt-engineering, rag-vector-databases.
- Gaming/XR (2): game-engine-unity-godot, spatial-computing-android-xr.
- E-commerce (2): in-app-purchases-revenuecat, payment-gateways.
- Product (2): product-requirements-discovery, user-stories-acceptance-criteria.
- Security (3): privacy-data-protection, software-supply-chain-security, threat-modeling.
- Testing (3): e2e-testing, integration-testing, performance-load-testing.
- Platform (2): ide-agent-adapters, mcp-server-integration.

## Workflows (8)
En .agents/workflows/: bug-fix.md, deployment.md, new-feature.md, refactoring.md, security-audit.md, product-discovery.md, multi-agent-development.md y ide-integration.md.

## Accesibilidad
- Declarar el nivel WCAG objetivo y no mezclar AA y AAA.
- AA: contraste 4.5:1 para texto normal y 3:1 para texto grande.
- AAA: contraste 7:1 para texto normal y 4.5:1 para texto grande.
- Componentes e información gráfica: 3:1 cuando aplique WCAG 1.4.11.
- Objetivo táctil recomendado: 44×44 CSS px. WCAG 2.2 AA 2.5.8 establece 24×24 CSS px con excepciones; AAA 2.5.5 establece 44×44 CSS px.
- Diseñar para teclado, foco visible, lectores de pantalla, zoom y movimiento reducido.

## Seguridad
OWASP Top 10:2025 es una guía de concienciación, no certificación. Adaptar controles al stack y modelo de amenazas. Aplicar mínimo privilegio, autorización server-side, consultas parametrizadas, aislamiento multi-tenant y RLS cuando corresponda.

## Prioridad
Seguridad > Integridad de datos y dinero > Requisitos del usuario > Mantenibilidad > Rendimiento > Velocidad.
