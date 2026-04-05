// Flujo IRP-03: Observabilidad avanzada
// Responsabilidad: Detectar fallos de observabilidad en tiempo real.
// Extensible para nuevas reglas IRP.
import { telemetryBus } from "../utils/telemetryBus.js";
import { validateObservability } from "../utils/validateObservability.js";
import { sendAlert } from "../utils/alertEngine.js";
import { logger } from "../utils/logger.js";

/**
 * Flujo IRP-03 para validación avanzada de observabilidad
 * - Escucha métricas y detecta fallos
 * - Aísla errores de listeners
 * - Extensible para nuevas reglas IRP
 */
export function runIRP03Flow() {
  logger.info("🚀 Ejecutando IRP‑03...", { module: "irp03Flow" });

  telemetryBus.on("metric", (metric) => {
    try {
      const ok = validateObservability(process.cwd());
      if (!ok) {
        logger.warn("Fallo detectado en IRP‑03", { module: "irp03Flow", metric });
        sendAlert("Fallo detectado en IRP‑03", metric);
      }
    } catch (err) {
      logger.error("Error en listener IRP-03", { module: "irp03Flow", error: err, metric });
      // No detener el sistema por errores de validación
    }
  });
}

runIRP03Flow();
