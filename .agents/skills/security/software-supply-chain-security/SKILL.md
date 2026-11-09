---
name: software-supply-chain-security
description: Reduce dependency, build, artifact and source supply-chain risks with provenance and controlled updates.
---
# Software Supply Chain Security

## Procedimiento
1. Inventariar dependencias, imágenes base, plugins, actions y artefactos.
2. Fijar versiones y usar lockfiles; evitar rangos flotantes en producción.
3. Verificar origen, mantenimiento, licencias y avisos de seguridad.
4. Aplicar SCA, secret scanning, SAST y escaneo de imágenes según riesgo.
5. Generar SBOM en formato estándar cuando aporte valor.
6. Proteger CI con permisos mínimos y pinning de Actions.
7. Firmar/verificar artefactos y registrar procedencia cuando sea viable.
8. Actualizar dependencias en lotes pequeños con pruebas y rollback.
9. Documentar excepciones, vencimiento y responsable.

## Gates
Un escáner limpio no demuestra ausencia de vulnerabilidades. No actualizar dependencias a ciegas ni ignorar advisories sin evaluación.
