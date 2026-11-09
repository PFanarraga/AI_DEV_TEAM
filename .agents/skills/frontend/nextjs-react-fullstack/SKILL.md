---
name: nextjs-react-fullstack
description: Desarrollar aplicaciones web modernas con React 19, Next.js App Router, TanStack Start/Router, Server Components, Server Actions y renderizado híbrido (SSR, SSG, ISR).
---

# Next.js & React Fullstack Skill

## Propósito
Construir aplicaciones web de alto rendimiento, optimizadas para motores de búsqueda (SEO) y con arquitectura React moderna e híbrida.

## Guía de Implementación

### 1. Arquitectura de Componentes en React 19
- **Server Components (RSC)**: Cargar datos directamente en el servidor para reducir el JavaScript enviado al cliente.
- **Client Components (`'use client'`)**: Usar únicamente para componentes interactivos con estado local, hooks o eventos del navegador.
- **Manejo de Formularios**: Utilizar Server Actions, `useActionState` y `useOptimistic` para experiencias de usuario instantáneas.

### 2. Enrutamiento y Carga
- **Layouts Anidados**: Reutilizar estructuras de navegación sin recargar partes innecesarias del árbol de componentes.
- **Estados de Carga y Suspenso**: Implementar `loading.tsx` y `<Suspense>` para evitar pantallas en blanco durante la obtención de datos.
