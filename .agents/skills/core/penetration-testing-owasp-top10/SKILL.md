---
name: penetration-testing-owasp-top10
description: Metodología de revisión basada en OWASP Top 10:2025 para aplicaciones web y APIs.
---

# Penetration Testing & OWASP Top 10:2025

Realizar pruebas intrusivas solo con autorización. Adaptar la lista al stack y modelo de amenazas.

## A01:2025 - Broken Access Control
- [ ] ¿La autorización se valida en servidor para cada operación y recurso?
- [ ] ¿Se prueban IDOR, escalación horizontal/vertical y aislamiento multi-tenant?
- [ ] ¿RLS, roles y grants coinciden con las reglas de negocio?

## A02:2025 - Security Misconfiguration
- [ ] ¿Defaults inseguros y servicios innecesarios están deshabilitados?
- [ ] ¿CORS, CSP, HSTS y cabeceras se configuran según el despliegue?
- [ ] ¿Errores no exponen rutas, secretos ni datos sensibles?

## A03:2025 - Software Supply Chain Failures
- [ ] ¿Dependencias están fijadas y se revisan vulnerabilidades?
- [ ] ¿Se verifican procedencia e integridad de paquetes, acciones CI y artefactos?
- [ ] ¿Los tokens CI tienen permisos mínimos?

## A04:2025 - Cryptographic Failures
- [ ] ¿Datos sensibles se protegen en tránsito y reposo?
- [ ] ¿Se usan algoritmos y protocolos vigentes?
- [ ] ¿Claves se almacenan, rotan y revocan de forma segura?

## A05:2025 - Injection
- [ ] ¿SQL/NoSQL/OS/LDAP usan consultas o APIs parametrizadas?
- [ ] ¿Entradas se validan en límites de confianza?
- [ ] ¿Salida se codifica según contexto para evitar XSS?

## A06:2025 - Insecure Design
- [ ] ¿Existe un modelo de amenazas para flujos críticos?
- [ ] ¿Se identifican abuso de negocio y límites de confianza?
- [ ] ¿Hay límites, cuotas y controles preventivos adecuados?

## A07:2025 - Authentication Failures
- [ ] ¿Login, recuperación y cambio de credenciales están protegidos?
- [ ] ¿Se controlan fuerza bruta, enumeración y abuso de sesiones?
- [ ] ¿Tokens, cookies, expiración y revocación siguen prácticas seguras?

## A08:2025 - Software or Data Integrity Failures
- [ ] ¿Se verifica integridad de artefactos, actualizaciones y datos importados?
- [ ] ¿Webhooks validan firma, origen, timestamp y repetición?
- [ ] ¿Operaciones críticas son idempotentes y resistentes a replay?

## A09:2025 - Security Logging and Alerting Failures
- [ ] ¿Se registran eventos relevantes de autenticación y operaciones críticas?
- [ ] ¿Logs evitan secretos y datos personales innecesarios?
- [ ] ¿Existen alertas accionables y procedimiento de respuesta?

## A10:2025 - Mishandling of Exceptional Conditions
- [ ] ¿Errores, timeouts y fallos parciales dejan el sistema en estado seguro?
- [ ] ¿Se evita fail-open ante fallos de autorización o dependencias?
- [ ] ¿Se controlan reintentos, duplicados, rollback y consistencia?

## Informe
Indicar categoría, evidencia, impacto, probabilidad, severidad, reproducción autorizada, corrección y verificación. Distinguir controles revisados, no aplicables y no comprobados.

Referencia oficial: https://owasp.org/Top10/2025/
