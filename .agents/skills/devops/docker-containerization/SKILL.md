---
name: docker-containerization
description: Empaquetar aplicaciones en contenedores Docker ligeros y seguros mediante Dockerfiles multietapa (multi-stage builds), Docker Compose e imágenes minimizadas (Alpine/Distroless).
---

# Docker Containerization Skill

## Propósito
Garantizar la portabilidad de aplicaciones entre entornos de desarrollo, pruebas y producción usando contenedores aislados y livianos.

## Guía de Implementación

### 1. Dockerfile Multietapa (Multi-Stage Build)
```dockerfile
# Etapa 1: Construcción
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Etapa 2: Producción ligera
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=builder /app/.output ./.output
EXPOSE 3000
CMD ["node", ".output/server/index.mjs"]
```

### 2. Buenas Prácticas
- Ejecutar el contenedor con un usuario sin privilegios de root (`USER node`).
- Incluir un archivo `.dockerignore` para excluir `node_modules`, `.git` y secretos locales `.env`.
