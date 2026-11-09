# AI DEV TEAM — Framework Profesional Multiagente con Cobertura Total (100%)

Sistema integral de **12 Agentes de IA Especialistas**, **32 Skills Categorizadas** y **Flujos de Trabajo** preparado para construir, auditar y desplegar cualquier tipo de software: **Web, Móvil, Desktop, Backend, Big Data, IA, Videojuegos, XR y E-Commerce**.

---

## 🛠️ Qué Incluye este Framework Maestro

- **12 Agentes Especialistas (`.agents/agents/`)**: Director, Arquitecto, Desarrollador Fullstack/Móvil, Desarrollador Desktop, Ingeniero de Datos, Desarrollador de Videojuegos/XR, QA Tester, Seguridad AppSec, Rendimiento, UI/UX, Diseñador Visual e Investigador.
- **32 Skills Especializadas Categorizadas (`.agents/skills/`)**:
  - `desktop/`: Tauri 2.0 (Rust + React), Electron para Windows/macOS/Linux.
  - `data/`: Pipelines ETL/ELT, dbt, ClickHouse, BigQuery y dashboards analíticos.
  - `gaming-xr/`: Unity (C#), Godot (GDScript), Android XR (Glimmer), VisionOS.
  - `core/`: Planificación, debugging, testing unitario, i18n multi-idioma, accesibilidad WCAG 2.2 AAA, OWASP Top 10.
  - `backend/`: PostgreSQL, pgvector, ORMs (Drizzle/Prisma), APIs REST/GraphQL/gRPC, Auth RBAC/RLS, Realtime.
  - `frontend/`: Next.js 15 App Router, React 19, Zustand/React Query, Tailwind v4/Shadcn UI, PWAs.
  - `mobile/`: Android Kotlin (Compose/Hilt), iOS Swift 6 (SwiftUI/SwiftData), React Native/Flutter, Tiendas.
  - `devops/`: Docker multietapa, CI/CD GitHub Actions, Cloudflare, AWS, Supabase, Vercel, Sentry.
  - `ai/`: Vercel AI SDK, LangChain, RAG Vectorial (pgvector), Agentes autónomos MCP.
  - `e-commerce/`: Pasarelas de pago (Stripe, Mercado Pago) y compras In-App (RevenueCat).
- **Flujos de Trabajo (`.agents/workflows/`)**: `bug-fix.md`, `new-feature.md`, `security-audit.md`, `refactoring.md`, `deployment.md`.
- **Plantillas Estándar (`templates/`)**: Requests, Handoffs entre agentes, ADRs y Pull Requests.

---

## 🚀 Cómo Usar en un Proyecto Nuevo

1. Copia el archivo `AGENTS.md` y la carpeta `.agents/` a la raíz de tu nuevo proyecto.
2. Abre tu IDE favorito (Android Studio, VS Code, Cursor, Windsurf, JetBrains).
3. Invoca al **Director** en el chat del asistente pegando el siguiente prompt inicial:

> "Lee AGENTS.md y .agents/agents/director.md. Actúa como Director del AI DEV TEAM. Analiza la siguiente solicitud, selecciona los especialistas y Skills correspondientes, presenta un plan y espera mi aprobación antes de modificar archivos."

---

## 🔒 Reglas de Seguridad e Integridad

- **Cero Secretos Expuestos**: Las claves API y tokens privados deben permanecer en `.env` (excluido de Git).
- **Verificación Financiera**: Todo valor monetario debe gestionarse en céntimos enteros para evitar errores de precisión.
- **Pruebas Automatizadas**: Todo cambio debe ir acompañado de pruebas unitarias o de integración verificadas.
