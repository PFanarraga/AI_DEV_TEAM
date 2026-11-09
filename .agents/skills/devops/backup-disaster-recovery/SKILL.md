---
name: backup-disaster-recovery
description: Design, operate and test backups, restore procedures, RPO/RTO and disaster recovery.
---
# Backup & Disaster Recovery

## Procedimiento
1. Clasificar datos y servicios por criticidad y dependencias.
2. Acordar RPO y RTO con responsables; no inventar objetivos.
3. Definir frecuencia, retención, cifrado, ubicación y aislamiento.
4. Proteger copias contra borrado, ransomware y credenciales comprometidas.
5. Documentar restauración completa y granular y validación de integridad.
6. Ejecutar simulacros en entorno aislado con datos protegidos.
7. Medir tiempo real de restauración y pérdida de datos.
8. Alertar sobre fallos, cobertura y expiración.
9. Actualizar runbooks tras simulacros e incidentes.

## Entregables
Matriz de sistemas, RPO/RTO aprobados, política, runbook y evidencia de restauración.

## Regla
Un backup no está verificado hasta restaurarlo y validarlo. No restaurar destructivamente en producción sin autorización.
