---
name: android-native-kotlin
description: Desarrollar aplicaciones Android nativas de nivel profesional utilizando Kotlin, Jetpack Compose, Coroutines, StateFlow, Hilt (DI), Room Database y arquitectura MVI/MVVM.
---

# Android Native (Kotlin & Jetpack Compose) Skill

## Propósito
Construir aplicaciones nativas Android de alto rendimiento, siguiendo las guías oficiales de Google para la arquitectura de aplicaciones modernas (MAD - Modern Android Development).

## Guía de Implementación

### 1. Arquitectura de Código (MVI / MVVM)
- **UI Layer**: Jetpack Compose con estado inmutable levantado (*state hoisting*).
- **ViewModel Layer**: Manejo de eventos con `StateFlow` o `SharedFlow` sobreviviendo cambios de configuración.
- **Data Layer**: Repositorio unificado que orquesta la base de datos local (Room) y el cliente de red (Ktor o Retrofit).

### 2. Inyección de Dependencias
- Usar **Hilt** para inyectar ViewModels, repositorios, bases de datos y clientes de red.

### 3. Asincronía y Flujos
- Usar **Kotlin Coroutines** con dispatchers adecuados (`Dispatchers.IO` para I/O, `Dispatchers.Main` para UI) y `Flow` para datos reactivos.
