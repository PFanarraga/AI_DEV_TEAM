# Workflow: Auditoría de Seguridad (Security Audit)

## Objetivo
Identificar vulnerabilidades de seguridad (OWASP Top 10, permisos RLS, secretos expuestos, autenticación) y corregirlas de forma verificada.

## Pasos del Flujo de Trabajo

### 1. Escaneo Inicial (Director & Security Agent)
- Buscar secretos en el repositorio (`.env`, tokens hardcodados en scripts/código).
- Verificar que `.gitignore` excluye archivos de entorno locales.

### 2. Auditoría de Base de Datos & RLS (Security Agent & Architect)
- Inspeccionar políticas RLS en PostgreSQL / Supabase:
  - Eliminar políticas permissivas `USING (true)` / `WITH CHECK (true)`.
  - Asegurar aislamiento por `auth.uid()` para datos de usuario.
- Verificar que las consultas no devuelven contraseñas ni datos privados.

### 3. Sanitización de Entradas y Protección de API (Security Agent & Developer)
- Verificar validaciones con **Zod** o esquemas estrictos en todas las entradas.
- Comprobar cabeceras CORS, CSRF y rate limiting.

### 4. Verificación y Reporte (Security Agent & Director)
- Ejecutar suite de pruebas unitarias y de seguridad.
- Entregar reporte estructurado por nivel de riesgo (**CRÍTICO**, **ALTO**, **MEDIO**, **BAJO**).
