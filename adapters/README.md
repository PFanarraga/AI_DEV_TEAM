# Adaptadores de AI DEV TEAM

El procedimiento completo está en [docs/PROJECT-BOOTSTRAP.md](../docs/PROJECT-BOOTSTRAP.md).

## Núcleo común

En cada proyecto instala en la raíz:
- `AGENTS.md`
- `.agents/` completa, incluyendo agents, skills, workflows y runtime.

No renombres `.agents/`. No copies el repositorio completo ni su carpeta `.git/` dentro del proyecto.

Desde la raíz del repositorio AI_DEV_TEAM puedes ejecutar:

```bash
python scripts/install_ai_dev_team.py --target "/ruta/al/proyecto" --dry-run
python scripts/install_ai_dev_team.py --target "/ruta/al/proyecto"
```

El instalador preserva archivos existentes y se detiene si detecta conflictos. No sobrescribe por defecto.

## Secuencia estándar

1. Copiar el núcleo.
2. Abrir el proyecto con el asistente elegido.
3. Consultar su guía en [docs/integrations/](../docs/integrations/README.md).
4. Ejecutar [Prompt 1: configurar asistente](../prompts/01-configure-assistant.md).
5. Verificar instrucciones, Skills, herramientas, permisos y subagentes reales.
6. Ejecutar [Prompt 2: iniciar proyecto](../prompts/02-start-project.md) o el prompt específico de la guía.

## Principios

- El asistente anfitrión asume el rol Director.
- El Director lee perfiles y Skills relevantes, y selecciona especialistas.
- Solo se afirma delegación cuando el host crea subagentes reales.
- Si no hay subagentes, coordina de forma secuencial.
- MCP conecta herramientas, no crea por sí mismo subagentes.
- Cada integración debe verificarse en la versión y configuración real.
- No conceder permisos irrestrictos ni ejecutar operaciones destructivas o productivas sin aprobación.
