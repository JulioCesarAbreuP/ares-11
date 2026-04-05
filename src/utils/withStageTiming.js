
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Utilidad de Telemetría de Pipeline
//  Arquitectura: Decorador asíncrono para instrumentar etapas críticas
//  Patrón: Timing + Emisión de eventos estructurados (durationMs)
//  Extensible: Admite nuevos tipos de métricas y enriquecimiento de eventos
// ────────────────────────────────────────────────────────────────────────────────
import { emitEvent } from "./telemetryBus.js";

/**
 * Ejecuta una función asíncrona midiendo su duración y emitiendo un evento de telemetría estructurada.
 * @function
 * @param {string} stageName - Nombre de la etapa del pipeline (ej: "TAXII", "fingerprinting")
 * @param {Function} fn - Función asíncrona a ejecutar
 * @returns {Promise<any>} Resultado de la función ejecutada
 * @throws {Error} Propaga cualquier error de la función decorada
 * @example
 * await withStageTiming("TAXII", async () => { ... })
 * // Emite evento: { type: "PIPELINE_STAGE", stage, status, durationMs }
 */
export async function withStageTiming(stageName, fn) {
  const start = Date.now();
  try {
    const result = await fn();
    const duration = Date.now() - start;
    emitEvent("metric", {
      type: "PIPELINE_STAGE",
      stage: stageName,
      status: "OK",
      durationMs: duration
    });
    return result;
  } catch (err) {
    const duration = Date.now() - start;
    emitEvent("metric", {
      type: "PIPELINE_STAGE",
      stage: stageName,
      status: "ERROR",
      durationMs: duration,
      error: err && err.message ? err.message : String(err)
    });
    throw err;
  }
}
