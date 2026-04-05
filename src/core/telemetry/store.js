
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Almacén Persistente de Telemetría
//  Arquitectura: Buffer en memoria con persistencia JSONL
//  Extensible: Permite filtros, paginación y limpieza
// ────────────────────────────────────────────────────────────────────────────────
import fs from "fs";
import path from "path";
const MAX_EVENTS = 500;
const TELEMETRY_FILE = path.resolve(process.cwd(), "telemetry.jsonl");

let events = [];

// Al iniciar, cargar últimos eventos desde disco si existe
if (fs.existsSync(TELEMETRY_FILE)) {
  const lines = fs.readFileSync(TELEMETRY_FILE, "utf8").split("\n").filter(Boolean);
  events = lines.map(line => {
    try { return JSON.parse(line); } catch { return null; }
  }).filter(Boolean).slice(-MAX_EVENTS);
}

/**
 * Agrega un evento al almacén
 * @param {Object} event - Evento de telemetría
 */
export function addEvent(event) {
  events.push(event);
  if (events.length > MAX_EVENTS) {
    events = events.slice(-MAX_EVENTS);
  }
  // Persistir a disco (append JSONL)
  try {
    fs.appendFileSync(TELEMETRY_FILE, JSON.stringify(event) + "\n");
  } catch (err) {
    // No bloquear si falla la persistencia
  }
}

/**
 * Obtiene todos los eventos almacenados
 * @returns {Array} Lista de eventos
 */
export function getEvents(opts = {}) {
  let filtered = [...events];
  if (opts.type) filtered = filtered.filter(e => e.type === opts.type);
  if (opts.since) filtered = filtered.filter(e => e.timestamp >= opts.since);
  if (opts.until) filtered = filtered.filter(e => e.timestamp <= opts.until);
  if (opts.limit) filtered = filtered.slice(-opts.limit);
  return filtered;
}

/**
 * Limpia el almacén de eventos
 */
export function clearEvents() {
  events = [];
}
