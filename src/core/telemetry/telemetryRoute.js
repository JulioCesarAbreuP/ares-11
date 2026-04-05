
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Ruta de Telemetría (API REST + SSE)
//  Arquitectura: Exposición de eventos vía REST y streaming SSE
//  Extensible: Permite nuevos endpoints y filtros
// ────────────────────────────────────────────────────────────────────────────────
import express from "express";
import { subscribe } from "../../utils/telemetryBus.js";
import { getEvents } from "./store.js";

const router = express.Router();

/**
 * Endpoint REST para obtener eventos de telemetría
 */
router.get("/telemetry", (req, res) => {
  res.json(getEvents());
});

/**
 * Endpoint SSE para streaming robusto de eventos
 */
router.get("/telemetry-stream", (req, res) => {
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");

  let alive = true;
  // Limitar a los últimos 100 eventos históricos
  const history = getEvents({ limit: 100 });
  try {
    history.forEach(e => {
      res.write(`data: ${JSON.stringify(e)}\n\n`);
    });
  } catch (err) {
    alive = false;
    res.end();
    return;
  }

  // Heartbeat para mantener la conexión
  const heartbeat = setInterval(() => {
    if (!alive) return;
    try {
      res.write(":heartbeat\n\n");
    } catch {
      alive = false;
      clearInterval(heartbeat);
      unsubscribe();
      res.end();
    }
  }, 15000);

  // Suscripción en vivo
  const unsubscribe = subscribe(event => {
    if (!alive) return;
    try {
      res.write(`data: ${JSON.stringify(event)}\n\n`);
    } catch (err) {
      alive = false;
      clearInterval(heartbeat);
      unsubscribe();
      res.end();
    }
  });

  req.on("close", () => {
    alive = false;
    clearInterval(heartbeat);
    unsubscribe();
  });
});

export default router;
