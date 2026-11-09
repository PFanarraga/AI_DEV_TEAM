---
name: e2e-testing
description: Validate end-to-end user journeys across UI, API and persistence with reliable browser or device automation.
---
# End-to-End Testing

## Procedimiento
1. Seleccionar journeys críticos por riesgo y valor.
2. Preparar entorno, usuarios sintéticos y datos deterministas.
3. Automatizar con herramienta compatible: Playwright, Cypress, WebdriverIO o pruebas móviles nativas.
4. Usar selectores accesibles y estables; evitar sleeps fijos.
5. Cubrir permisos, errores, estados vacíos, responsive y accesibilidad.
6. Capturar trazas y logs sin PII.
7. Aislar sesiones, paralelismo y limpieza.
8. Repetir pruebas flaky para diagnosticar, no ocultar fallos.

## Gates
E2E no sustituye unitarias ni integración. Mantener smoke suite pequeña y suite ampliada separada. Reportar navegadores/dispositivos y versiones.
