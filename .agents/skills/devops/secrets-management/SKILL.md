---
name: secrets-management
description: Store, inject, rotate and audit credentials without exposing them in source, logs or artifacts.
---
# Secrets Management

## Procedimiento
1. Identificar secretos, propietarios, consumidores, alcance y caducidad.
2. Preferir secret manager o variables seguras del entorno.
3. Separar secretos por entorno y servicio; mínimo privilegio.
4. Inyectar en runtime, nunca en código, imágenes, frontend o artefactos.
5. No imprimir variables, cabeceras Authorization, cookies ni URLs firmadas.
6. Rotar con estrategia de solapamiento y rollback.
7. Escanear historial y artefactos; ante exposición, revocar/rotar primero.
8. Auditar accesos y alertar sobre uso anómalo.
9. Documentar recuperación sin copiar el valor.

## Gates
.env.example solo contiene nombres y valores ficticios. Borrar el archivo no revoca un secreto filtrado.
