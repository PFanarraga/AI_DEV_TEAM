# Instalación de AI DEV TEAM en un proyecto

## Objetivo

Usar el mismo núcleo de agentes, Skills y workflows en cualquier proyecto y con el asistente que el usuario prefiera. La instalación se realiza antes de configurar el asistente y antes de pedirle que construya el producto.

## Flujo oficial

1. **Preparar el proyecto:** crea o abre la carpeta raíz del proyecto. Si ya contiene código, no lo muevas ni lo reemplaces.
2. **Obtener AI DEV TEAM:** clona o descarga este repositorio en una ubicación auxiliar. No es necesario copiar el repositorio completo dentro del proyecto.
3. **Instalar el núcleo:** copia únicamente `AGENTS.md` y la carpeta `.agents/` a la raíz del proyecto. Puedes hacerlo manualmente o ejecutar el instalador seguro descrito abajo.
4. **Elegir el asistente:** abre la carpeta del proyecto en el IDE/asistente que usarás y consulta la guía correspondiente en [docs/integrations](integrations/README.md).
5. **Configurar el asistente:** pega [Prompt 1: configurar el asistente](../prompts/01-configure-assistant.md), junto con la guía específica. El asistente debe detectar su versión, comprobar la documentación oficial vigente y preparar solo el adaptador nativo necesario.
6. **Verificar la integración:** confirma que el asistente puede leer `AGENTS.md`, el perfil Director y las Skills; revisa las herramientas, permisos y disponibilidad real de subagentes.
7. **Iniciar el proyecto:** completa [Prompt 2: iniciar un proyecto](../prompts/02-start-project.md) o utiliza el prompt de inicio incluido en la guía específica del asistente.
8. **Desarrollar:** el Director inspecciona, planifica, coordina, implementa y verifica siguiendo las reglas del núcleo.

## Qué copiar y qué no copiar

| Elemento | ¿Va a la raíz del proyecto? | Motivo |
|---|---:|---|
| `AGENTS.md` | Sí | Instrucciones globales del framework |
| `.agents/agents/` | Sí | Perfiles de especialistas y Director |
| `.agents/skills/` | Sí | Procedimientos técnicos reutilizables |
| `.agents/workflows/` | Sí | Procesos de trabajo |
| `.agents/runtime/` | Sí | Contrato y especificación de orquestación |
| `docs/` | No, normalmente | Guías de referencia del repositorio central |
| `adapters/` | No, normalmente | Material de adaptación y documentación |
| `scripts/` | No, normalmente | Herramientas de mantenimiento del framework |
| `.git/` | No | No anidar el repositorio del framework dentro del proyecto |

El núcleo mínimo es `AGENTS.md` más `.agents/` completa. No copies solamente los agentes: las Skills y workflows son parte del sistema.

## Instalación automática segura

Desde una terminal, ejecuta el instalador que viene en el repositorio AI_DEV_TEAM:

```bash
python scripts/install_ai_dev_team.py --target "/ruta/a/tu/proyecto" --dry-run
python scripts/install_ai_dev_team.py --target "/ruta/a/tu/proyecto"
```

En Windows PowerShell, por ejemplo:

```powershell
py .\scripts\install_ai_dev_team.py --target "D:\Proyectos\MiProyecto" --dry-run
py .\scripts\install_ai_dev_team.py --target "D:\Proyectos\MiProyecto"
```

El instalador:
- Copia solo `AGENTS.md` y `.agents/`.
- No copia `.git`, documentación, cachés ni archivos del repositorio auxiliar.
- No sobrescribe archivos existentes.
- Si detecta un archivo con el mismo destino pero contenido distinto, se detiene antes de escribir y muestra el conflicto.
- Con `--skip-conflicts`, conserva los archivos conflictivos y copia únicamente los archivos que faltan.
- Puede ejecutarse varias veces: los archivos idénticos se omiten.

Si ya existe un `AGENTS.md` o una carpeta `.agents/`, revisa los conflictos y combina manualmente las instrucciones. No reemplaces reglas del proyecto sin entenderlas.

## Configuración del asistente

El núcleo es común, pero los mecanismos de descubrimiento no lo son. El asistente debe usar la guía de su host para decidir si necesita `CLAUDE.md`, `.cursor/rules/`, `.github/copilot-instructions.md`, `GEMINI.md`, `.junie/AGENTS.md` u otro adaptador.

Reglas:
- Mantener `AGENTS.md` y `.agents/` como fuente canónica.
- Crear el mínimo adaptador nativo necesario y enlazarlo al núcleo.
- Si ya existe un archivo de instrucciones, combinarlo sin borrar contenido.
- No crear copias divergentes de todos los agentes y Skills.
- No activar permisos irrestrictos ni instalar MCP/subagentes sin necesidad y autorización.
- No afirmar que una capacidad funciona hasta comprobarla en la versión instalada.

## Verificación mínima antes de iniciar

- [ ] El asistente está abierto en la raíz correcta.
- [ ] Puede leer `AGENTS.md`.
- [ ] Puede leer `.agents/agents/director.md`.
- [ ] Puede localizar y abrir al menos una Skill pertinente.
- [ ] Identifica las herramientas que realmente tiene habilitadas.
- [ ] Distingue perfiles Markdown de subagentes ejecutables.
- [ ] Declara si coordinará en paralelo o secuencialmente.
- [ ] No ha modificado código funcional del producto durante la configuración.

La validación documental del repositorio central (`python scripts/validate_framework.py`) no certifica la integración funcional del asistente dentro de cada IDE.

## Actualizaciones futuras

Cada proyecto conserva una copia del núcleo instalado. Para actualizarla, compara primero la versión nueva con los archivos del proyecto. No hagas una copia encima de otra ni reemplaces `.agents/` a ciegas: integra cambios, conserva personalizaciones locales y vuelve a ejecutar las verificaciones.
