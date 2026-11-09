---
name: penetration-testing-owasp-top10
description: Ejecutar auditorías de seguridad y pruebas de penetración siguiendo el estándar OWASP Top 10 para identificar y mitigar vulnerabilidades en aplicaciones web, móviles y APIs.
---

# Penetration Testing & OWASP Top 10 Skill

## Propósito
Proporcionar una metodología sistemática de auditoría de seguridad para descubrir y corregir vulnerabilidades antes de pasar a producción.

## Lista de Verificación OWASP Top 10

### 1. Broken Access Control (Control de Acceso)
- `[ ]` ¿Está RLS activado en todas las tablas transaccionales de PostgreSQL?
- `[ ]` ¿Existen políticas permisivas `USING (true)` que deban ser reemplazadas por filtros de `auth.uid()`?
- `[ ]` ¿Puede un usuario modificar o consultar registros de otro usuario alterando el ID en la URL o API?

### 2. Cryptographic Failures
- `[ ]` ¿Todas las conexiones forzan HTTPS con TLS 1.3?
- `[ ]` ¿Las contraseñas usan hashing fuerte (Argon2 / Bcrypt) sin posibilidad de revertirlas?

### 3. Injection (Inyección)
- `[ ]` ¿Se ejecutan las consultas SQL mediante ORMs parametrizados sin concatenar strings?
- `[ ]` ¿Se validan y desinfectan todos los payloads recibidos en la API?

### 4. Security Misconfiguration
- `[ ]` ¿Están configuradas las cabeceras HTTP de seguridad (`CSP`, `X-Frame-Options`, `HSTS`)?
- `[ ]` ¿Están las políticas CORS restringidas únicamente a los dominios autorizados?
