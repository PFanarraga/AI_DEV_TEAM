# AI DEV TEAM — Reglas Globales, Catálogo de 12 Agentes y 32 Skills

## Misión
Orquestar un equipo completo de 12 Agentes de Inteligencia Artificial especializados para desarrollar, auditar, probar y desplegar cualquier tipo de software (**Web, Móvil iOS/Android, Desktop Windows/macOS/Linux, Backend, Big Data, IA Generativa, Videojuegos 2D/3D, Computación Espacial XR y E-Commerce**) con estándar de calidad 100% profesional.

## Idioma y Convenciones
- **Conversación y Documentación**: Español.
- **Código Fuente, Variables y Commits**: Inglés (salvo que el proyecto ya utilice otra convención).

## Reglas Obligatorias de Ingeniería
1. **Inspección Previa**: Inspeccionar el repositorio antes de proponer cambios. No asumir comportamientos sin verificar.
2. **Cero Alucinaciones**: No inventar APIs, versiones de paquetes, resultados de compilación ni ejecuciones de pruebas no realizadas.
3. **Estándar UI/UX "Design System First"**:
   - Variables semánticas OKLCH/HSL para modo claro y oscuro.
   - Especificar siempre los 8 estados del componente (*default, hover, focus-visible, active, disabled, loading, error, empty*).
   - Accesibilidad **WCAG 2.2 AAA** con contraste tipográfico ≥ 4.5:1, áreas de toque de 44×44px y navegación por teclado.
4. **Estándar de Seguridad AppSec (OWASP Top 10 & Zero Trust)**:
   - NUNCA hardcodear ni exponer secretos (`service_role`, claves privadas) en el frontend.
   - Validación estricta con **Zod** de todas las entradas del usuario.
   - Políticas RLS estrictas en PostgreSQL/Supabase con aislamiento por `auth.uid()`.
5. **Verificación Financiera Estricta**: Manejar montos monetarios en céntimos enteros (`Cents = number`) para prevenir errores de redondeo en punto flotante.
6. **Testing Obligatorio**: Añadir o actualizar pruebas unitarias/integración para cada cambio de comportamiento.

---

## Catálogo Maestro de 12 Agentes Especialistas (`.agents/agents/`)

| Agente | Rol | Skills Asignados |
| :--- | :--- | :--- |
| **`director.md`** | Director & Orquestador Principal | `planning`, `project-discovery`, `release-checklist`, `documentation` |
| **`architect.md`** | Arquitecto de Sistemas & BD | `architecture`, `database-design-migrations`, `api-design-rest-graphql-grpc`, `cloud-infrastructure` |
| **`developer.md`** | Desarrollador Fullstack & Móvil | `coding-standards`, `nextjs-react-fullstack`, `android-native-kotlin`, `ios-swift-swiftui`, `cross-platform-react-native-flutter`, `state-management`, `pwa-offline-first` |
| **`desktop-developer.md`** | Desarrollador de Escritorio Nativo | `desktop-electron-tauri`, `coding-standards`, `security-basics` |
| **`data-engineer.md`** | Ingeniero de Datos & Big Data | `data-pipelines-etl-elt`, `data-warehousing-analytics`, `database-design-migrations` |
| **`game-developer.md`** | Desarrollador de Videojuegos & XR | `game-engine-unity-godot`, `spatial-computing-android-xr`, `performance-basics` |
| **`tester.md`** | Ingeniero de Calidad (QA) | `unit-testing`, `e2e-testing-playwright-cypress`, `debugging` |
| **`security.md`** | Auditor de Seguridad (AppSec) | `security-basics`, `penetration-testing-owasp-top10`, `authentication-authorization-rbac` |
| **`performance.md`** | Ingeniero de Rendimiento | `performance-basics`, `monitoring-observability-sentry` |
| **`ui-ux.md`** | Diseñador UI/UX & Accesibilidad | `ui-ux-design`, `ui-accessibility`, `design-systems-tailwind-shadcn` |
| **`visual-designer.md`** | Diseñador Visual & Branding | Identidad gráfica, marcas, ilustraciones, iconografía SVG |
| **`researcher.md`** | Investigador Técnico | Benchmarking, evaluación de librerías y documentación oficial |

---

## Catálogo Completo de 32 Skills Categorizadas (`.agents/skills/`)

### Core & Proceso (`skills/core/`)
- `planning`, `debugging`, `code-review`, `unit-testing`, `security-basics`, `penetration-testing-owasp-top10`, `ui-ux-design`, `ui-accessibility`, `project-discovery`, `release-checklist`, `performance-basics`, `coding-standards`, `documentation`, `internationalization-i18n-localization`.

### Desktop (`skills/desktop/`)
- `desktop-electron-tauri`: Aplicaciones nativas instalables para Windows, macOS y Linux con Tauri 2.0 y Electron.

### Data Engineering (`skills/data/`)
- `data-pipelines-etl-elt`: Pipelines de datos en tiempo real, CDC y dbt.
- `data-warehousing-analytics`: Almacenes de datos analíticos con ClickHouse, BigQuery y dashboards.

### Videojuegos & XR (`skills/gaming-xr/`)
- `game-engine-unity-godot`: Motores de juego 2D/3D Unity (C#) y Godot (GDScript/C#).
- `spatial-computing-android-xr`: Computación espacial para Android XR y Apple VisionOS.

### Backend (`skills/backend/`)
- `database-design-migrations`, `api-design-rest-graphql-grpc`, `authentication-authorization-rbac`, `realtime-websockets-queues`.

### Frontend (`skills/frontend/`)
- `nextjs-react-fullstack`, `state-management`, `design-systems-tailwind-shadcn`, `pwa-offline-first`.

### Mobile (`skills/mobile/`)
- `android-native-kotlin`, `ios-swift-swiftui`, `cross-platform-react-native-flutter`, `store-deployment-play-appstore`.

### DevOps & Cloud (`skills/devops/`)
- `docker-containerization`, `cicd-github-actions`, `cloud-infrastructure`, `monitoring-observability-sentry`.

### AI & Agentes (`skills/ai/`)
- `llm-integration-langchain`, `rag-vector-databases`, `agentic-workflows-mcp`.

### E-Commerce & Monetización (`skills/e-commerce/`)
- `payment-gateways`, `in-app-purchases-revenuecat`.

---

## Prioridad de Decisiones
`Seguridad > Integridad de datos / Dinero > Requisitos del usuario > Mantenibilidad > Velocidad.`
