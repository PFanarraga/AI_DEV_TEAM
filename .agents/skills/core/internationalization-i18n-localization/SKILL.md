---
name: internationalization-i18n-localization
description: Implementar soporte multi-idioma nativo e internacionalización (i18n) con next-intl, react-i18next, formatos de moneda, horas y fechas regionales.
---

# Internationalization (i18n) & Localization Skill

## Propósito
Permitir que la aplicación se adapte automáticamente al idioma, región geográfica, formato de moneda y zona horaria del usuario.

## Guía de Implementación

### 1. Traducciones Dinámicas
- Usar archivos JSON de diccionarios por código de idioma (`es.json`, `en.json`, `pt.json`).
- Utilizar `next-intl` o `react-i18next` para intercalar variables dentro de las frases.

### 2. Formateadores Nativos de la API `Intl`
```ts
// Formato de moneda por región
new Intl.NumberFormat('es-PE', { style: 'currency', currency: 'PEN' }).format(150.50);
// Formato de fecha localizado
new Intl.DateTimeFormat('es-PE', { dateStyle: 'full' }).format(new Date());
```
