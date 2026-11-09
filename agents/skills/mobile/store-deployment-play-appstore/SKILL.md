---
name: store-deployment-play-appstore
description: Configurar el empaquetado, firmado de APK/Android App Bundle (AAB) e iOS IPA, automatización con Fastlane y publicación en Google Play Console y Apple App Store.
---

# Store Deployment (Play Store & App Store) Skill

## Propósito
Gestionar la preparación, firmado criptográfico y publicación de aplicaciones móviles en las tiendas oficiales.

## Guía de Implementación

### 1. Android (Google Play Store)
- Generar **Android App Bundle (.aab)** firmados con Keystore de producción.
- Configurar Google Play Console: capturas de pantalla, política de privacidad, clasificación de contenido.

### 2. iOS (Apple App Store)
- Configurar Certificados de Distribución y Provisioning Profiles en Apple Developer Console.
- Subir builds vía **TestFlight** / Xcode / Fastlane.
