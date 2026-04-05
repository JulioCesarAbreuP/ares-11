
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Logger Estructurado
//  Arquitectura: Logging resiliente, estructurado y auditable (JSONL)
//  Patrón: Logger centralizado, extensible a nuevos niveles y destinos
// ────────────────────────────────────────────────────────────────────────────────
import fs from "fs";
import path from "path";

const LOG_FILE = path.join(process.cwd(), "ares11.log");

/**
 * Escribe una entrada de log estructurada
 * @param {string} level - Nivel (info, warn, error, debug)
 * @param {string} msg - Mensaje
 * @param {object} [context] - Contexto adicional
 */
function writeLog(level, msg, context) {
  const entry = {
    timestamp: new Date().toISOString(),
    level,
    message: msg,
    ...(context ? { context } : {})
  };
  const line = JSON.stringify(entry);
  // Consola
  if (level === "error") {
    console.error(`[${level.toUpperCase()}]`, msg, context || "");
  } else if (level === "warn") {
    console.warn(`[${level.toUpperCase()}]`, msg, context || "");
  } else {
    console.log(`[${level.toUpperCase()}]`, msg, context || "");
  }
  // Archivo
  try {
    fs.appendFileSync(LOG_FILE, line + "\n");
  } catch (err) {
    console.error("[LOGGER] Error escribiendo log:", err);
  }
}

/**
 * Logger centralizado para ARES-11
 * @namespace logger
 * @property {Function} info - Log nivel info
 * @property {Function} warn - Log nivel warning
 * @property {Function} error - Log nivel error
 * @property {Function} debug - Log nivel debug
 */
export const logger = {
  info: (msg, context) => writeLog("info", msg, context),
  warn: (msg, context) => writeLog("warn", msg, context),
  error: (msg, context) => writeLog("error", msg, context),
  debug: (msg, context) => writeLog("debug", msg, context)
};
