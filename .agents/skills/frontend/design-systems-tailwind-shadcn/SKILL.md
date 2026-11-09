---
name: design-systems-tailwind-shadcn
description: Construir sistemas de diseño corporativos accesibles con Tailwind CSS v4, Shadcn UI, Radix Primitives y Lucide Icons, garantizando consistencia visual, tokens OKLCH y modo oscuro nativo.
---

# Design Systems (Tailwind CSS v4 & Shadcn UI) Skill

## Propósito
Desarrollar componentes e interfaces de usuario profesionales, accesibles, reactivas y consistentes mediante utilidades modernas de CSS y primitivas de componentes headless.

## Guía de Implementación Paso a Paso

### 1. Variables Temáticas Semánticas en CSS (OKLCH / HSL)
- Definir paletas mediante variables CSS semánticas en `:root` y `.dark`:
```css
:root {
  --background: oklch(1 0 0);
  --foreground: oklch(0.27 0.02 250);
  --primary: oklch(0.64 0.13 232);
  --primary-foreground: oklch(1 0 0);
  --card: oklch(0.975 0.004 240);
  --card-foreground: oklch(0.27 0.02 250);
  --destructive: oklch(0.56 0.2 25);
  --positive: oklch(0.55 0.14 155);
}

.dark {
  --background: oklch(0.18 0.015 245);
  --foreground: oklch(0.95 0.005 240);
  --primary: oklch(0.74 0.12 228);
  --card: oklch(0.225 0.018 245);
}
```

### 2. Accesibilidad y Primitivas Headless con Radix UI
- Modales, menús y diálogos construidos sobre **Radix Primitives** para garantizar atrapamiento de foco, navegación por teclado (`Esc`, `Tab`) e indicadores visuales (`focus-visible:ring-2 ring-primary`).

### 3. Utilidad de Clases Dinámicas con `cn()`
```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```
- Usar siempre `cn()` para fusionar clases de Tailwind CSS sin conflictos de especificidad.
