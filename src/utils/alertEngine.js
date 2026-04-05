
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Motor de Alertas de Telemetría
//  Arquitectura: Detección y emisión de alertas críticas y de lentitud
//  Extensible: Añadir nuevas reglas y niveles de alerta
// ────────────────────────────────────────────────────────────────────────────────
import { emitEvent } from "./telemetryBus.js";
import { logger } from "./logger.js";

/**
 * Envía una alerta personalizada al bus de telemetría.
 * @param {string} mensaje - Mensaje de alerta.
 * @param {object} datos - Datos adicionales.
 */
export function sendAlert(mensaje, datos) {
  try {
    emitEvent("alert", {
      type: "ALERT",
      level: "HIGH",
      message: mensaje,
      ...datos
    });
    logger.info("Alerta enviada", { module: "alertEngine", mensaje, datos });
  } catch (err) {
    logger.error("Error enviando alerta", { module: "alertEngine", error: err, mensaje, datos });
  }
}

const SLOW_THRESHOLD_MS = 5000;

/**
 * Evalúa si un evento PIPELINE_STAGE debe generar una alerta.
 * Detecta errores críticos y lentitud anómala.
 * @param {object} event - Evento de telemetría.
 */
export function evaluateAlert(event) {
  if (!event || typeof event !== "object") return;
  if (event.type !== "PIPELINE_STAGE") return;
  try {
    if (event.status === "ERROR") {
      logger.error(`[ALERTA] Falla en etapa ${event.stage}: ${event.error || ""}`, { module: "alertEngine", event });
      emitEvent("alert", {
        type: "ALERT",
        level: "HIGH",
        message: `Stage ${event.stage} failed: ${event.error || ""}`
      });
    }
    if (event.durationMs > SLOW_THRESHOLD_MS) {
      logger.warn(`[ALERTA] Etapa lenta: ${event.stage} (${event.durationMs} ms)`, { module: "alertEngine", event });
      emitEvent("alert", {
        type: "ALERT",
        level: "MEDIUM",
        message: `Stage ${event.stage} is slow (${event.durationMs} ms)`
      });
    }
  } catch (err) {
    logger.error("Error evaluando alerta de etapa", { module: "alertEngine", error: err, event });
  }
}
