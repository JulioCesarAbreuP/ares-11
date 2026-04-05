/**
 * IRP—03 — Observability Validator
 * Evalúa la calidad de telemetría, alertas, streaming y paneles.
 * Arquitectura: Validación exhaustiva de observabilidad para auditoría y cumplimiento IRP-03.
 * Extensible: Añadir nuevas reglas y checks según necesidades regulatorias.
 *
 * @param {string} projectRoot - Ruta raíz del proyecto
 * @returns {Object} Resultados de validación (score, total, percentage, results[])
 */
import fs from "fs";
import path from "path";

export function validateObservability(projectRoot) {
  const results = [];

  /**
   * Verifica existencia de archivo clave
   * @param {string} relativePath
   * @param {string} description
   * @returns {boolean}
   */
  function checkFile(relativePath, description) {
    const full = path.join(projectRoot, relativePath);
    const exists = fs.existsSync(full);
    results.push({
      check: description,
      file: relativePath,
      status: exists ? "OK" : "MISSING"
    });
    return exists;
  }

  /**
   * Verifica contenido clave en archivo
   * @param {string} relativePath
   * @param {string} description
   * @param {string} keyword
   * @returns {boolean}
   */
  function checkContent(relativePath, description, keyword) {
    const full = path.join(projectRoot, relativePath);
    if (!fs.existsSync(full)) {
      results.push({
        check: description,
        file: relativePath,
        status: "MISSING"
      });
      return false;
    }
    const content = fs.readFileSync(full, "utf8");
    const ok = content.includes(keyword);
    results.push({
      check: description,
      file: relativePath,
      status: ok ? "OK" : "NOT FOUND"
    });
    return ok;
  }

  // --- 1. Telemetry Core ---
  checkFile("src/core/telemetry/store.js", "Store de telemetría existe");
  checkFile("src/utils/telemetryBus.js", "Bus de telemetría existe");
  checkContent(
    "src/utils/telemetryBus.js",
    "emitEvent enriquece eventos",
    "timestamp"
  );

  // --- 2. Alert Engine ---
  checkFile("src/utils/alertEngine.js", "Alert Engine existe");
  checkContent(
    "src/utils/alertEngine.js",
    "Alert Engine detecta errores",
    "HIGH"
  );
  checkContent(
    "src/utils/alertEngine.js",
    "Alert Engine detecta lentitud",
    "MEDIUM"
  );

  // --- 3. Pipeline Metrics ---
  checkFile(
    "src/core/telemetry/pipelineMetrics.js",
    "pipelineMetrics.js existe"
  );
  checkContent(
    "src/core/telemetry/pipelineMetrics.js",
    "withStageTiming registra duración",
    "durationMs"
  );

  // --- 4. Streaming SSE ---
  checkFile(
    "src/core/telemetry/telemetryRoute.js",
    "Ruta de telemetría existe"
  );
  // ...existing code...
  checkContent(
    "src/core/telemetry/telemetryRoute.js",
    "SSE implementado",
    "text/event-stream"
  );

  // --- 5. Dashboard Integration ---
  checkFile(
    "src/ui/dashboard/performancePanel.js",
    "Panel de rendimiento existe"
  );
  checkContent(
    "src/ui/dashboard/performancePanel.js",
    "Panel calcula medias",
    "Avg Duration"
  );

  checkFile(
    "src/ui/dashboard/tacticalTerminal.js",
    "Terminal táctico existe"
  );
  checkContent(
    "src/ui/dashboard/tacticalTerminal.js",
    "Terminal recibe eventos",
    "pushTerminalEvent"
  );

  // --- 6. Pipeline Integration ---
  checkFile("src/orchestrator/pipeline.js", "Pipeline existe");
  checkContent(
    "src/orchestrator/pipeline.js",
    "Pipeline emite eventos",
    "emitEvent"
  );

  // --- Score ---
  const score = results.filter(r => r.status === "OK").length;
  const total = results.length;

  return {
    module: "IRP‑03 Observability",
    score,
    total,
    percentage: Math.round((score / total) * 100),
    results
  };
}
