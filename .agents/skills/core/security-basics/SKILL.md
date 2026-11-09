---
name: security-basics
description: Aplicar principios de seguridad fundamentales, desinfección de entradas, sanitización XSS/CSRF, gestión de secretos en .env y prevención de fuga de datos sensibles.
---

# Security Basics & Data Protection Skill

## Propósito
Establecer las defensas fundamentales en el desarrollo de código fuente para evitar vulnerabilidades comunes e impedir la exposición no autorizada de datos.

## Guía de Implementación Paso a Paso

### 1. Gestión Segura de Secretos
- **Cero Secretos en Repositorios**: NUNCA guardar claves privadas (`service_role`, credenciales de BD, llaves secretas) en el código.
- **Aislamiento `.env`**: Confirmar que `.env` está registrado en `.gitignore`.
- Usar únicamente variables públicas `VITE_*` o `NEXT_PUBLIC_*` en el cliente.

### 2. Sanitización y Validación de Entradas
- Validar todas las entradas del usuario con esquemas **Zod** antes de procesarlas o guardarlas.
- Desinfectar HTML/textos ingresados por el usuario para prevenir Cross-Site Scripting (XSS).

### 3. Integridad Financiera
- Manejar todos los montos monetarios en céntimos enteros (`Cents = number`), evitando flotantes JavaScript (`0.1 + 0.2 = 0.30000000000000004`).
