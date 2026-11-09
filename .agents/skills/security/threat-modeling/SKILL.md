---
name: threat-modeling
description: Identify trust boundaries, assets, attackers, abuse cases and mitigations during system design.
---
# Threat Modeling

## Método
1. Definir alcance, componentes y flujos de datos.
2. Inventariar activos: identidad, secretos, PII, dinero, disponibilidad, integridad y propiedad intelectual.
3. Marcar límites de confianza, entradas, salidas, integraciones y privilegios.
4. Identificar actores, capacidades y escenarios de abuso.
5. Aplicar STRIDE u otra taxonomía apropiada.
6. Evaluar probabilidad e impacto con escala explícita.
7. Priorizar controles preventivos, detectivos y de recuperación.
8. Asignar responsable, estado y evidencia a cada mitigación.
9. Repetir ante cambios de arquitectura, permisos o datos.

## Entregables
Descripción de límites, registro de amenazas, escenarios de abuso, matriz de riesgo, mitigaciones y riesgos aceptados.

## Controles
Autorización server-side, aislamiento multi-tenant, validación, rate limiting, CSRF/CORS, SSRF, inyección, sesiones, cifrado, auditoría y backups.

## Reglas
HTTPS, WAF o escáneres no demuestran seguridad. No ocultar riesgos residuales. Validar mitigaciones con pruebas.
