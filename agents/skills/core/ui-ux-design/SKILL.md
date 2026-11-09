---
name: ui-ux-design
description: Diseñar e implementar interfaces de usuario profesionales con arquitectura de información clara, jerarquía visual, principios Gestalt, maquetación responsiva y densidad de datos controlada.
---

# UI/UX Design Professional Skill

## Propósito
Guiar la creación de experiencias de usuario profesionales, atractivas y funcionales para aplicaciones web, móviles y dashboards de administración.

## Guía de Implementación Paso a Paso

### 1. Arquitectura de Información y Maquetación Responsiva
- **Grilla y Espaciados**: Usar una grilla base de 8px (o 4px para elementos compactos).
- **Jerarquía Visual**:
  1. Elemento Primario (Título principal, indicador clave o CTA destacado).
  2. Elemento Secundario (Información contextual, filtros o metadatos).
  3. Elemento Terciario (Detalles secundarios u opcionales).
- **Diseño Mobile-First**: Diseñar primero la experiencia táctil móvil (360px - 414px) y extender hacia pantallas de escritorio (1024px - 1440px+).

### 2. Estados de Componente Indispensables
Todo componente interactivo debe especificar 8 estados:
- **Default**, **Hover**, **Focus-Visible**, **Active**, **Disabled**, **Loading/Skeleton**, **Error**, **Empty**.

### 3. Densidad Visual y Dashboarding
- Para paneles administrativos: mantener densidad controlada, separando tarjetas de estadísticas en cuadrículas de 2 a 4 columnas.
- Usar tipografías monoespaciadas con números tabulares para montos y métricas clave.
