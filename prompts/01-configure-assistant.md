# Prompt 1 | Configurar AI DEV TEAM en este asistente

Copia este prompt en el asistente que usarás para trabajar en el proyecto. Adjunta o consulta también la guía específica de ese asistente desde el repositorio AI_DEV_TEAM.

```text
Quiero preparar este proyecto para trabajar con AI DEV TEAM. Esta es una fase EXCLUSIVA de instalación, adaptación y verificación. Todavía NO comiences a construir el producto ni modifiques su código funcional.

OBJETIVO
Configurar el asistente anfitrión para que utilice el núcleo AI DEV TEAM que ya está copiado en la raíz del proyecto.

FUENTE CANÓNICA
- AGENTS.md
- .agents/agents/
- .agents/skills/
- .agents/workflows/
- .agents/runtime/ORCHESTRATION.md

INSTRUCCIONES
1. Confirma qué carpeta tienes abierta y verifica que es la raíz del proyecto.
2. Lee AGENTS.md y .agents/agents/director.md completos.
3. Inspecciona la estructura existente y detecta archivos de instrucciones/configuración del asistente. No sobrescribas ni elimines nada.
4. Identifica el producto, extensión o CLI que estás utilizando y su versión exacta cuando sea posible. No supongas capacidades por el nombre del modelo.
5. Usa la guía específica proporcionada y, si tienes acceso a internet, contrasta la configuración con la documentación oficial vigente. Si no puedes consultar fuentes actuales, dilo.
6. Determina cómo este host descubre instrucciones, Skills, perfiles, herramientas, MCP y subagentes. Distingue entre:
   - leer un perfil Markdown;
   - cargar una Skill como procedimiento;
   - invocar una herramienta;
   - delegar a un subagente independiente.
   No los presentes como equivalentes.
7. Diseña el adaptador nativo mínimo necesario para que el host lea el núcleo. Mantén AGENTS.md y .agents/ como fuente de verdad.
8. Si ya existe un archivo de configuración, propone una combinación que preserve todas las reglas útiles. Antes de sobrescribir, renombrar o eliminar cualquier archivo, solicita mi aprobación. Si no puedes editar archivos, entrega el contenido exacto y su ruta.
9. No instales extensiones, paquetes, MCP servers, modelos ni dependencias sin autorización.
10. Comprueba de forma segura que puedes leer AGENTS.md, el perfil Director y una Skill pertinente. No ejecutes comandos destructivos ni modifiques el código funcional.
11. Declara las capacidades reales: lectura/escritura del workspace, terminal, Git, navegación, MCP, subagentes, aprobaciones y persistencia. Marca cada una como verificada, no disponible o no comprobada.
12. Si no hay subagentes reales, informa que coordinarás especialistas secuencialmente. Nunca simules delegación paralela.

ENTREGABLE
Presenta:
A. Asistente y versión detectados.
B. Archivos del núcleo encontrados.
C. Adaptador/configuración creada o propuesta, con rutas.
D. Archivos preexistentes preservados y conflictos detectados.
E. Matriz de capacidades con evidencia.
F. Pruebas de lectura realizadas y sus resultados.
G. Limitaciones y acciones que requieren mi intervención.

CONDICIÓN DE CIERRE
No comiences el desarrollo del producto. Termina cuando la integración esté configurada o cuando hayas entregado instrucciones manuales claras. Espera mi siguiente prompt para iniciar el proyecto.
```
