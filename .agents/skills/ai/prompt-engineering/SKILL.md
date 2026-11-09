---
name: prompt-engineering
description: Design versioned, testable prompts with clear trust boundaries and structured outputs.
---
# Prompt Engineering

## Procedimiento
1. Definir tarea, usuario, salida, restricciones y criterio de éxito.
2. Separar instrucciones confiables, datos del usuario y contenido recuperado no confiable.
3. Usar instrucciones claras, ordenadas y sin contradicciones.
4. Definir formato mediante esquema cuando sea viable.
5. Añadir ejemplos representativos si reducen ambigüedad.
6. Diseñar manejo de incertidumbre, abstención, preguntas y errores.
7. No incluir secretos ni datos sensibles innecesarios.
8. Versionar prompts y evaluar cambios con dataset de regresión.
9. Medir calidad, consistencia, latencia, tokens y coste.

## Regla
El prompt no es control de seguridad suficiente. Validar salida, argumentos y permisos en código.
