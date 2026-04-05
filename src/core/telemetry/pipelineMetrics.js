
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Métricas de Pipeline (Alias)
//  Arquitectura: Alias para utilidades de timing y métricas
//  Patrón: Reexporta withStageTiming para trazabilidad IRP-03
// ────────────────────────────────────────────────────────────────────────────────
// La función withStageTiming emite eventos con la propiedad durationMs
export { withStageTiming } from "../../utils/withStageTiming.js";
