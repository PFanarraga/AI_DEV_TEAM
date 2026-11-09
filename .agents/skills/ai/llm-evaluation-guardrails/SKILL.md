---
name: llm-evaluation-guardrails
description: Evaluate LLM quality and enforce runtime guardrails for reliability, privacy, security and cost.
---
# LLM Evaluation & Guardrails

## Evaluación
1. Crear dataset sintético o anonimizado con tareas, límites y ataques.
2. Definir rúbricas: exactitud, completitud, relevancia, groundedness, formato, seguridad y coste.
3. Combinar evaluación determinista, revisión humana y evaluadores calibrados.
4. Medir baseline y regresiones por versión.
5. Probar prompt injection, jailbreak, fuga de contexto y herramientas no autorizadas.
6. Evaluar retrieval: recall, precision, citas y vigencia.
7. Evaluar antes de liberar cambios de modelo, prompt o herramientas.

## Guardrails runtime
Validar esquemas; allowlist de herramientas; autorización fuera del modelo; límites de tokens, coste, tiempo y reintentos; confirmación para acciones externas/destructivas; redacción de datos sensibles.

## Entregables
Dataset versionado, rúbrica, resultados, thresholds, fallbacks y riesgos. LLM-as-judge no demuestra seguridad.
