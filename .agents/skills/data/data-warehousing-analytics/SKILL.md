---
name: data-warehousing-analytics
description: Diseñar almacenes de datos analíticos de alta velocidad con ClickHouse, BigQuery o Snowflake, esquemas estrella/copo de nieve e integración con Metabase/Grafana.
---

# Data Warehousing & Analytics Skill

## Propósito
Permitir consultas analíticas ultarrápidas sobre millones de filas para reportes corporativos y tableros de inteligencia de negocio.

## Guía de Implementación

### 1. Motores Columnares (ClickHouse / BigQuery)
- Utilizar almacenamiento por columnas para compresión masiva (hasta 10x) y velocidad de agregación (`SUM`, `AVG`, `COUNT`).
- Diseñar esquemas estrella con tablas de hechos (*fact tables*) e hilos de dimensiones (*dimension tables*).
