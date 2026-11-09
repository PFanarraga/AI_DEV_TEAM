---
name: cicd-github-actions
description: Diseñar e implementar pipelines automatizados de Integración y Despliegue Continuo (CI/CD) con GitHub Actions para ejecución de tests, linting, compilación y despliegue a la nube.
---

# CI/CD & GitHub Actions Skill

## Propósito
Automatizar la verificación de calidad del código y la entrega de actualizaciones a producción en cada Commit o Pull Request.

## Guía de Implementación

### 1. Estructura de Workflow (`.github/workflows/ci-cd.yml`)
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test-and-build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm run build
```

### 2. Gestión de Secretos
- Almacenar tokens de despliegue en **GitHub Repository Secrets** (nunca hardcodear claves en el archivo YAML).
