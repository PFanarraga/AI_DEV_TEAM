---
name: pwa-offline-first
description: Crear Progressive Web Apps (PWA) instalables en iOS/Android/Desktop con Service Workers, estrategias de caché inteligentes, IndexedDB y soporte offline-first.
---

# Progressive Web Apps (PWA) & Offline-First Skill

## Propósito
Convertir aplicaciones web en experiencias instalables de alta disponibilidad que funcionen incluso en condiciones de baja o nula conectividad.

## Guía de Implementación

### 1. Configuración del Manifiesto PWA
- Definir `manifest.json` con `name`, `short_name`, `icons` (192px y 512px), `theme_color`, `background_color` y `display: standalone`.

### 2. Service Worker e Integración de Caché Segura
- **Estrategias de Caché**:
  - `Cache First` para recursos estáticos (HTML, CSS, JS, fuentes, imágenes).
  - `Network First` para datos dinámicos.
- **Seguridad en Caché PWA**: EXCLUIR explícitamente peticiones de la API privada de autenticación y bases de datos (`/auth/`, `/rest/`) para evitar almacenar datos sensibles en la caché del navegador.
