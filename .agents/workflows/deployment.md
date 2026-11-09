# Workflow: Despliegue a Producción (Deployment)

## Objetivo
Empaquetar, verificar y publicar la aplicación en servidores de producción (Cloudflare Pages, Vercel, Supabase, Google Play, App Store) sin interrupciones.

## Pasos del Flujo de Trabajo

### 1. Verificación de Compilación y Calidad (Director & Tester)
- Ejecutar análisis de tipos TypeScript y linter.
- Ejecutar suite de pruebas automatizadas: `npm test` / `vitest`.
- Ejecutar compilación de producción: `npm run build`.

### 2. Verificación de Secretos y Variables de Entorno (Security Agent)
- Confirmar que las variables de entorno de producción están configuradas en el panel del proveedor cloud.
- Confirmar que claves privadas (`service_role`, tokens) no están incluidas en los bundles públicos.

### 3. Ejecución del Despliegue (Developer & Director)
- Ejecutar el script/comando de despliegue oficial (`wrangler pages deploy`, `vercel --prod`, etc.).
- Probar la respuesta HTTP en vivo (código 200 OK) y realizar verificación post-despliegue.
