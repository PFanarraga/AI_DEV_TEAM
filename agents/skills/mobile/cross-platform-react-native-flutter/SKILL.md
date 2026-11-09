---
name: cross-platform-react-native-flutter
description: Crear aplicaciones híbridas de alto rendimiento con React Native (Expo, Reanimated) o Flutter (Dart, Bloc/Provider) compiladas nativamente para iOS y Android.
---

# Cross-Platform Mobile Skill

## Propósito
Desarrollar aplicaciones multiplataforma eficientes reutilizando la lógica de negocio para iOS y Android sin sacrificar rendimiento nativo.

## Guía de Implementación

### 1. React Native (Expo Workflow)
- **Navegación**: Expo Router o React Navigation.
- **Animaciones**: React Native Reanimated (ejecutadas a 60/120 fps en el hilo nativo UI).
- **Manejo de Estado**: TanStack Query + Zustand.

### 2. Flutter (Dart)
- **Gestión de Estado**: Bloc o Riverpod.
- **Rendimiento**: Minimizar reconstrucciones de árbol de widgets y usar widgets `const`.
