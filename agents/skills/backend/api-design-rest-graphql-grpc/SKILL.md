---
name: api-design-rest-graphql-grpc
description: Diseñar e implementar APIs profesionales utilizando RESTful, GraphQL o gRPC, con contratos OpenAPI/Swagger, filtrado, paginación, manejo unificado de errores y versionado.
---

# API Design (REST, GraphQL, gRPC) Skill

## Propósito
Establecer un estándar limpio para la arquitectura de comunicación cliente-servidor mediante APIs robustas, documentadas, escalables y seguras.

## Guía de Implementación

### 1. Convenciones RESTful
- **Sustantivos en Plural**: `/api/v1/drivers`, `/api/v1/records`, `/api/v1/settlements`.
- **Verbos HTTP**:
  - `GET`: Lectura idempotente.
  - `POST`: Creación de recursos.
  - `PUT`/`PATCH`: Actualización completa o parcial.
  - `DELETE`: Eliminación o inactivación lógica.
- **Códigos de Estado HTTP Unificados**:
  - `200 OK`, `201 Created`, `204 No Content`.
  - `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `409 Conflict`.
  - `500 Internal Server Error`.

### 2. Estructura de Respuesta Unificada
```json
{
  "success": true,
  "data": { ... },
  "error": null,
  "meta": {
    "page": 1,
    "pageSize": 20,
    "total": 100
  }
}
```

### 3. Paginación y Filtrado
- Implementar paginación por cursor o por límite/desplazamiento (`limit` / `offset`).
- Soporte para ordenamiento transparente: `?sort=-created_at`.
