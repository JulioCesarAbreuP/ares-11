
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Simulador de Eventos de Telemetría
//  Arquitectura: Generador sintético de métricas para pruebas y desarrollo
//  Patrón: Resiliencia ante fallos de listeners, útil para pruebas de paneles
// ────────────────────────────────────────────────────────────────────────────────
import { telemetryBus } from "./telemetryBus.js";
import { logger } from "./logger.js";

/**
 * Inicia el simulador de eventos de telemetría
 * Emite métricas sintéticas periódicamente y aísla errores de listeners.
 * @function
 */
export function startEventSimulator() {
  logger.info("🎛️ Simulador de eventos iniciado...", { module: "eventSimulator" });
  setInterval(() => {
    try {
      const metric = {
        type: "cpu",
        value: Math.floor(Math.random() * 100),
        timestamp: Date.now()
      };
      telemetryBus.emit("metric", metric);
    } catch (err) {
      logger.error("Error emitiendo métrica simulada", { module: "eventSimulator", error: err });
      // El simulador sigue funcionando aunque falle un consumidor
    }
  }, 1500);
}

startEventSimulator();
