---
name: desktop-electron-tauri
description: Desarrollar e instalar aplicaciones de escritorio nativas multiplataforma (Windows, macOS, Linux) usando Tauri 2.0 (Rust + React/Svelte) o Electron, empaquetado y auto-actualizaciones.
---

# Desktop Apps (Tauri & Electron) Skill

## Propósito
Construir software de escritorio nativo de alto rendimiento, bajo consumo de memoria RAM y empaquetado seguro para Windows, macOS y Linux.

## Guía de Implementación

### 1. Tauri 2.0 (Recomendado para Rendimiento)
- **Frontend**: React 19 / Svelte / Vue empaquetado en HTML/JS.
- **Backend Nativo (Rust)**: Comandos invocados vía IPC (`#[tauri::command]`).
- **Aislamiento**: Tamaño de ejecutable < 15 MB y consumo de RAM < 80 MB.

### 2. Electron
- Habilitar `contextIsolation: true` y `nodeIntegration: false` para seguridad.
- Comunicación bidireccional mediante `ipcMain` e `ipcRenderer` con scripts de precarga (`preload.js`).
