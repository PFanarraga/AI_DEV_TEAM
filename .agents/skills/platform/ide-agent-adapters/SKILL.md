---
name: ide-agent-adapters
description: Integrate a canonical agent framework with multiple IDEs and coding assistants through native instruction files and safe adapters.
---
# IDE & Agent Adapters

## Principio
Mantener fuente canónica: AGENTS.md, .agents/agents/, .agents/skills/ y .agents/workflows/. Los archivos del host son adaptadores delgados, no copias divergentes.

## Procedimiento
1. Identificar host, versión y capacidades: reglas, Skills, subagentes, MCP, terminal, filesystem y approvals.
2. Consultar documentación vigente del host.
3. Generar el archivo nativo mínimo que apunte a AGENTS.md y al Director.
4. No sobrescribir configuración existente; ofrecer instrucciones de merge.
5. Mantener rutas relativas y compatibilidad multiplataforma.
6. Verificar carga de instrucciones y ausencia de secretos.
7. Documentar funciones no soportadas y fallback secuencial.
8. Probar instalación repetible e idempotente.

## Hosts
VS Code/GitHub Copilot, Visual Studio, JetBrains, Android Studio, IntelliJ, PyCharm, WebStorm, Cursor, Windsurf, Claude Code, Gemini CLI, Cline, Roo Code, Continue, Aider, Zed y hosts compatibles con instrucciones de repositorio.

## Interoperabilidad
Markdown + rutas + convenciones es el núcleo portable. MCP conecta herramientas; delegación, memoria y approvals dependen del host/runtime.

## Criterios
No afirmar compatibilidad automática universal. Diferenciar instrucciones leídas, Skills descubiertas, herramientas conectadas y subagentes realmente ejecutables.
