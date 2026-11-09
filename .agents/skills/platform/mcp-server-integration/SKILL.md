---
name: mcp-server-integration
description: Design and integrate Model Context Protocol servers and tools with explicit schemas, permissions and operational controls.
---
# MCP Server Integration

## Diseño
1. Definir recursos, prompts y herramientas con propósito acotado.
2. Especificar schemas estrictos, límites, errores y compatibilidad.
3. Seleccionar transporte y autenticación soportados.
4. Tratar contenido externo como no confiable e indicar procedencia.
5. Separar lectura, escritura externa y operaciones productivas.
6. Validar autorización en servidor para cada invocación.
7. Aplicar timeouts, límites, cancelación, rate limiting y auditoría.
8. Evitar filesystem completo, shell irrestricto o secretos expuestos.
9. Documentar instalación, versiones y troubleshooting.
10. Probar clientes MCP reales y permisos denegados.

## Seguridad
Usar allowlists de rutas y comandos, sandbox para ejecutar código y aprobación humana para acciones destructivas. No asumir que el cliente aplica controles suficientes.

## Entregables
Especificación de herramientas, schemas, matriz de permisos, conexión, pruebas y riesgos.
