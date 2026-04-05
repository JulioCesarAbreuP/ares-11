
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Bus de Telemetría Central
//  Arquitectura: EventEmitter extensible para eventos de pipeline, alertas y métricas
//  Patrón: Event Bus desacoplado, resiliente a fallos de listeners
// ────────────────────────────────────────────────────────────────────────────────
import { EventEmitter } from "events";
import { logger } from "./logger.js";

/**
 * Bus de eventos de telemetría global
 * @type {EventEmitter}
 */
export const telemetryBus = new EventEmitter();

/**
 * Emite un evento enriquecido (agrega timestamp) al bus de telemetría.
 * Aísla errores de listeners y añade trazabilidad.
 * @param {string} tipo - Tipo de evento (canal)
 * @param {object} datos - Datos del evento
 */
export function emitEvent(tipo, datos) {
	const enriched = {
		timestamp: Date.now(),
		...datos
	};
	try {
		telemetryBus.emit(tipo, enriched);
		logger.debug("Evento emitido", { module: "telemetryBus", tipo, enriched });
	} catch (err) {
		logger.error("Error emitiendo evento en telemetryBus", { module: "telemetryBus", error: err, tipo, enriched });
	}
}
