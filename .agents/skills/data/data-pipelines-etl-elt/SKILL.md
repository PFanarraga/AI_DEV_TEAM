---
name: data-pipelines-etl-elt
description: Diseñar e implementar pipelines de datos en tiempo real (ETL/ELT), conectores CDC (Change Data Capture) y transformaciones automatizadas con dbt y Webhooks.
---

# Data Pipelines (ETL / ELT) Skill

## Propósito
Extraer, transformar y cargar datos de forma confiable entre sistemas operacionales (OLTP) y almacenes analíticos (OLAP).

## Guía de Implementación

### 1. Arquitectura ELT (Extract, Load, Transform)
- Cargar datos crudos en la base de datos de destino y realizar las transformaciones dentro del motor analítico usando **dbt**.
- Usar conectores CDC (Change Data Capture) para sincronizar cambios en tiempo real desde PostgreSQL / Supabase hacia ClickHouse o BigQuery.
