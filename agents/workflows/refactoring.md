# Workflow: Refactorización Limpia (Refactoring)

## Objetivo
Mejorar la estructura, legibilidad y rendimiento del código sin alterar su comportamiento externo ni romper funcionalidades existentes.

## Pasos del Flujo de Trabajo

### 1. Garantía de Cobertura de Pruebas (Tester & Developer)
- Verificar o escribir pruebas unitarias para el módulo a refactorizar ANTES de modificar código.
- Confirmar que las pruebas actuales pasan en verde.

### 2. Aislamiento y Aplicación de Patrones (Architect & Developer)
- Extraer duplicaciones usando principios **SOLID** y **Clean Code**.
- Reemplazar tipos implícitos (`any`) por tipos estrictos.
- Centralizar cálculos o reglas de negocio duplicadas.

### 3. Verificación de No Regresión (Tester & Director)
- Ejecutar la suite de pruebas unitarias.
- Confirmar que la firma de APIs públicas no ha cambiado.
- Revisar el diff de Git.
