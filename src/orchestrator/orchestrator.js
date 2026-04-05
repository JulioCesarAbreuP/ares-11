// Orquestador central de ARES-11
// Responsabilidad: Coordina la recepción de métricas y la validación de observabilidad.
// Extensible para nuevos flujos de orquestación y validaciones.
import { validateObservability } from "../utils/validateObservability.js";
import { runIRP03 } from "../utils/validateProjectPRO.js";
import { sendAlert } from "../utils/alertEngine.js";
import { telemetryBus } from "../utils/telemetryBus.js";
import { logger } from "../utils/logger.js";

/**
 * Orquestador principal de ARES-11
 * - Escucha métricas y valida observabilidad
 * - Aísla errores de listeners
 * - Extensible para nuevos flujos
 */
export function orchestrator() {
  logger.info("🔧 Orquestador ARES‑11 iniciado...", { module: "orchestrator" });

  telemetryBus.on("metric", (data) => {
    try {
      logger.info("📡 Métrica recibida", { module: "orchestrator", data });
      const observabilityOK = validateObservability(process.cwd());
      if (!observabilityOK) {
        logger.warn("Observabilidad fallida", { module: "orchestrator", data });
        sendAlert("Observabilidad fallida", data);
      }
    } catch (err) {
      logger.error("Error en listener de métrica", { module: "orchestrator", error: err, data });
      // No detener el sistema por errores de validación
    }
  });

  try {
    runIRP03();
  } catch (err) {
    logger.error("Error al iniciar IRP-03", { module: "orchestrator", error: err });
  }
}

orchestrator();
