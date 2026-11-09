---
name: database-design-migrations
description: Diseñar esquemas relacionales (PostgreSQL, MySQL, SQLite) y NoSQL (MongoDB, Redis), definir índices de alto rendimiento y gestionar migraciones de base de datos seguras y reversibles.
---

# Database Design & Migrations Skill

## Propósito
Guiar la creación y evolución de bases de datos relacionales y no relacionales con modelado de datos limpio, integridad referencial, índices optimizados y migraciones sin tiempo de inactividad.

## Guía de Implementación

### 1. Principios de Modelado de Datos
- **Tipado Estricto**: Usar los tipos nativos más eficientes (ej: `UUID` para IDs, `TIMESTAMPTZ` para fechas con zona horaria, `INTEGER` en céntimos para montos financieros).
- **Claves Primarias y Foráneas**: Definir siempre claves primarias (`PK`) y claves foráneas (`FK`) con restricciones de borrado (`ON DELETE CASCADE` o `SET NULL`).
- **Normalización**: Mantener esquemas en 3NF para datos operacionales transaccionales (OLTP).

### 2. Estrategia de Índices
- Crear índices en columnas frecuentemente filtradas (`WHERE`), unidas (`JOIN`) u ordenadas (`ORDER BY`).
- Usar índices compuestos cuando se consulte por múltiples columnas juntas.
- Evitar índices innecesarios en tablas con alto volumen de escrituras.

### 3. Migraciones Seguras
- Toda alteración debe realizarse mediante scripts SQL idempotentes (usar `CREATE TABLE IF NOT EXISTS`, `ALTER TABLE ... ADD COLUMN IF NOT EXISTS`).
- Las migraciones en producción deben ser reversibles y no destructivas (evitar `DROP TABLE` o `TRUNCATE` directos).
- Para cambios grandes, aplicar el patrón **Expand and Contract**:
  1. Expandir: añadir la nueva columna o tabla sin eliminar la antigua.
  2. Migrar: copiar/transformar los datos progresivamente.
  3. Contraer: eliminar la columna antigua una vez validado el sistema.
