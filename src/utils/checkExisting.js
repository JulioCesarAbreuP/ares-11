
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Utilidad de Chequeo de Existencia de Archivos
//  Arquitectura: Script simple para validar presencia de archivos clave
//  Uso: node src/utils/checkExisting.js
// ────────────────────────────────────────────────────────────────────────────────
import fs from "fs";
import path from "path";

const projectRoot = process.cwd();

const files = [
  "src/utils/validateObservability.js",
  "src/utils/validateProjectPRO.js",
  "src/utils/alertEngine.js",
  "src/utils/telemetryBus.js",
  "src/core/telemetry/store.js",
  "src/core/telemetry/telemetryRoute.js",
  "src/core/telemetry/pipelineMetrics.js",
  "src/ui/dashboard/performancePanel.js",
  "src/ui/dashboard/tacticalTerminal.js"
];

/**
 * Imprime solo los archivos que existen de la lista
 */
for (const rel of files) {
  const full = path.join(projectRoot, rel);
  if (fs.existsSync(full) && fs.statSync(full).isFile()) {
    console.log(rel);
  }
}
