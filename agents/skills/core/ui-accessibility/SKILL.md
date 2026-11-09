---
name: ui-accessibility
description: Garantizar accesibilidad de software conforme al estándar WCAG 2.2 Nivel AAA, incluyendo contraste tipográfico, navegación por teclado, áreas de toque y lectores de pantalla ARIA.
---

# UI Accessibility (WCAG 2.2 AAA) Skill

## Propósito
Garantizar que las aplicaciones sean totalmente accesibles e inclusivas para usuarios con cualquier tipo de discapacidad sensorial o motora.

## Guía de Implementación Paso a Paso

### 1. Contraste y Tipografía
- **Ratio de Contraste Texto Normal**: Mínimo 4.5:1 contra el fondo.
- **Ratio de Contraste Texto Grande / Íconos**: Mínimo 3.0:1.
- No transmitir información únicamente mediante colores (acompañar siempre de íconos o etiquetas de texto).

### 2. Navegación por Teclado
- Habilitar `focus-visible:ring-2 ring-primary ring-offset-2` en todo elemento cliqueable o editable.
- Asegurar orden lógico de tabulación (`tabindex=0`) y atrapamiento de foco (*focus trap*) dentro de modales activos.
- Cerrar modales y paneles flotantes con la tecla `Escape`.

### 3. Etiquetas ARIA y Lectores de Pantalla
- Usar elementos HTML semánticos (`<main>`, `<nav>`, `<header>`, `<section>`, `<article>`, `<button>`).
- En botones que solo contienen íconos, incluir texto accesible:
  `<button aria-label="Cerrar sesión"><LogOut /></button>`
