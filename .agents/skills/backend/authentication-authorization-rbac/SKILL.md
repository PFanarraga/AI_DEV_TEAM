---
name: authentication-authorization-rbac
description: Implementar sistemas de autenticación y autorización seguros mediante OAuth2, OIDC, JWT, Supabase Auth, Firebase Auth, control de acceso basado en roles (RBAC) y políticas RLS a nivel de base de datos.
---

# Authentication & Authorization (RBAC & RLS) Skill

## Propósito
Proteger las aplicaciones e infraestructura garantizando autenticación fuerte, gestión de sesiones, control de acceso jerárquico y aislamiento estricto de datos en la base de datos.

## Guía de Implementación Paso a Paso

### 1. Principios de Seguridad en Autenticación
- **Cero Contraseñas en Texto Plano**: Contraseñas gestionadas mediante hashing fuerte (Argon2 / Bcrypt) o proveedores delegados de Auth (Supabase Auth, Firebase Auth, Auth0).
- **Tokens de Sesión**: `access_token` JWT de corta duración y `refresh_token` en cookies `HttpOnly; Secure; SameSite=Strict`.
- **Cierre de Sesión e Invalidation**: Limpiar explícitamente tokens en servidor y localStorage/cookies en cliente al cerrar sesión.

### 2. Control de Acceso Basado en Roles (RBAC)
- Definir roles jerárquicos claros (`superadmin`, `admin`, `conductor`, `user`).
- Validar permisos en cada endpoint o Server Action del lado del servidor (nunca depender únicamente del renderizado condicional en React).

### 3. Seguridad Row Level Security (RLS) en PostgreSQL
- Habilitar RLS en todas las tablas transaccionales y privadas:
  `ALTER TABLE public.records ENABLE ROW LEVEL SECURITY;`
- Aplicar políticas restrictivas basadas en `auth.uid()` y claims de JWT:
  ```sql
  CREATE POLICY "Aislamiento por usuario" ON public.records
    FOR SELECT USING (
      driver_id = auth.uid() OR
      (auth.jwt() ->> 'role') IN ('admin', 'superadmin')
    );
  ```
