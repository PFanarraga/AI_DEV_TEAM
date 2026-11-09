---
name: payment-gateways
description: Integrar pasarelas de pago (Stripe, Mercado Pago, Culqi, Niubiz) con procesamiento seguro de tarjetas, cobros recurrentes y verificación de webhooks criptográficos.
---

# Payment Gateways Skill

## Propósito
Implementar procesamiento de pagos seguro, suscripciones y transacciones financieras cumpliendo con los estándares de seguridad de la industria de tarjetas (PCI-DSS).

## Guía de Implementación

### 1. Integración de Pasarelas
- Usar SDKs oficiales de pasarelas de pago (Stripe Elements, Mercado Pago SDK).
- Nunca enviar ni procesar datos de tarjetas directamente en nuestros servidores (usar tokenización de pasarela).

### 2. Verificación de Webhooks Criptográficos
- Validar siempre la firma criptográfica del webhook recibido en el servidor antes de procesar un pago o activar una suscripción.
- Garantizar idempotencia en el procesamiento de eventos de webhook.
