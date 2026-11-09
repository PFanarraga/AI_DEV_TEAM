---
name: state-management
description: Diseñar e implementar la gestión de estado global y asíncrono con Zustand, Redux Toolkit, TanStack Query (React Query) y Jotai para arquitecturas React complejas.
---

# State Management Skill

## Propósito
Estructurar el flujo de datos global y asíncrono garantizando reactividad eficiente, re-renderizados mínimos y sincronización confiable con APIs.

## Guía de Implementación

### 1. Separación de Estado Servidor vs. Estado Cliente
- **Estado del Servidor (Server State)**: Gestionar datos de API mediante **TanStack Query (React Query)** (cacheo automático, reintento, invalidación de consultas y mutaciones optimistas).
- **Estado Global del Cliente (Client State)**: Utilizar **Zustand** o **Redux Toolkit** únicamente para estados de interfaz UI (temas, paneles, modales, preferencias de usuario).

### 2. Mutaciones Optimistas
- Actualizar la interfaz de inmediato antes de que el servidor responda.
- En caso de error del servidor, revertir automáticamente (*rollback*) al estado anterior e informar al usuario con una notificación (Toast).
