---
name: infrastructure-as-code
description: Define reproducible, reviewable and least-privilege infrastructure with Terraform, OpenTofu or provider-native IaC.
---
# Infrastructure as Code

## Procedimiento
1. Inspeccionar proveedor, estado, entornos y recursos gestionados.
2. Elegir herramienta compatible y fijar versiones de providers/modules.
3. Modularizar por responsabilidad evitando abstracciones prematuras.
4. Mantener estado remoto cifrado, bloqueado y restringido.
5. Separar variables y secretos del código.
6. Ejecutar format, validate, lint, policy checks y plan antes de apply.
7. Revisar reemplazos, destrucciones, exposición pública, IAM y costes.
8. Aplicar primero en entorno no productivo.
9. Documentar importación, drift, rollback y recuperación del estado.

## Gates
No aplicar cambios productivos ni destruir recursos sin aprobación explícita. No compartir state ni planes que expongan secretos.
