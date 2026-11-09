---
name: ui-accessibility
description: Evaluar accesibilidad conforme a WCAG 2.2, declarando con precisión el nivel AA o AAA.
---

# UI Accessibility Skill - WCAG 2.2

## Contraste
- WCAG AA, texto normal: mínimo 4.5:1.
- WCAG AA, texto grande: mínimo 3:1.
- WCAG AAA, texto normal: mínimo 7:1.
- WCAG AAA, texto grande: mínimo 4.5:1.
- Componentes e información gráfica: mínimo 3:1 cuando aplique el criterio 1.4.11.
- No transmitir información únicamente mediante color, posición, forma o sonido.

Texto grande significa al menos 18 pt (aprox. 24 CSS px) en peso normal o 14 pt (aprox. 18.67 CSS px) en negrita.

## Teclado y foco
Toda funcionalidad debe poder operarse con teclado. Mantener orden lógico de foco visible, evitar trampas, gestionar foco al abrir/cerrar diálogos y evitar que quede oculto.

## Objetivos táctiles
WCAG 2.2 AA 2.5.8: mínimo 24×24 CSS px con excepciones. WCAG AAA 2.5.5: mínimo 44×44 CSS px con excepciones. Como objetivo móvil, preferir 44×44 CSS px incluso con nivel AA.

## Semántica
Usar elementos semánticos y nombres accesibles. Asociar etiquetas, instrucciones y errores con controles. Anunciar cambios de estado. Verificar orden de lectura, encabezados, landmarks y texto alternativo. Evitar ARIA redundante.

## Movimiento y adaptabilidad
Respetar prefers-reduced-motion. Mantener funcionalidad con zoom y ampliación de texto. Probar tamaños, orientaciones y métodos de entrada.

## Informe
Nivel objetivo y alcance, criterios comprobados y método, barreras y evidencia, severidad, correcciones y criterios no verificados.
