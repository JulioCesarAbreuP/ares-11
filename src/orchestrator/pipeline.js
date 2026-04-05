import { emitEvent } from "../core/telemetry/telemetryBus.js";
// ARES‑11 — Pipeline Orchestrator
// Fingerprinting → TAXII → Threat Mapper → Dashboard

import { execSync } from "child_process";
import { TaxiiClient } from "../core/taxii-client/taxiiClient.js";
import { buildMitreHeatmap, buildNistPlan, generateCisControls } from "../core/threat-mapper/threat-mapper.js";
import { computeRisk } from "../core/risk-engine/riskEngine.js";
import fs from "fs";
import { logger } from "../utils/logger.js";
import pathConfig from "../config/paths.config.json" assert { type: "json" };
import { withStageTiming } from "../utils/withStageTiming.js";
/**
 * Orquesta el pipeline principal de ARES-11:
 * 1. Ejecuta el motor de fingerprinting (Go)
 * 2. Sincroniza inteligencia MITRE ATT&CK vía TAXII
 * 3. Correlaciona activos y técnicas con Threat Mapper
 * 4. Exporta datos para el dashboard
 *
 * Cada etapa es tolerante a fallos y usa datos de ejemplo si es necesario.
 * El sistema sigue operativo aunque un módulo falle.
 */
  logger.info("[ARES‑11] Starting pipeline...");
  // Validación de configuración esencial
  if (!pathConfig || !pathConfig.fingerprintOutput || !pathConfig.dashboardMitre || !pathConfig.dashboardNist || !pathConfig.dashboardDir) {
    logger.error("[CONFIG] Configuración de rutas incompleta. Revisa paths.config.json", { pathConfig });
    return;
  }

  // ─────────────────────────────────────────────
  // 1) Fingerprinting Engine (Go)
  // ─────────────────────────────────────────────
  logger.info("[FP] Running Fingerprinting Engine...");
  emitEvent("metric", { type: "PIPELINE_START" });
  let pipelineStatus = "OK";
  let pipelineError = null;
  // Fingerprinting con telemetría
  const assets = await withStageTiming("fingerprinting", async () => {
    try {
      execSync(`go run ./src/core/fingerprint/main.go > ${pathConfig.fingerprintOutput}`);
      const rawAssets = fs.readFileSync(pathConfig.fingerprintOutput, "utf8");
      const parsed = JSON.parse(rawAssets);
      if (!Array.isArray(parsed) || !parsed.every(a => a && typeof a.ip === "string" && typeof a.port === "number" && a.service)) {
        throw new Error("[FP] Invalid asset data structure");
      }
      logger.info(`[FP] Assets discovered: ${parsed.length}`);
      return parsed;
    } catch (err) {
      logger.error(`[FP] Error ejecutando fingerprinting: ${err.message}`, { error: err });
      logger.warn("[FP] Usando datos de ejemplo para assets.");
      return [
        { ip: "10.0.0.10", port: 22, service: "open" },
        { ip: "10.0.0.20", port: 3389, service: "open" }
      ];
    }
  });

  // ─────────────────────────────────────────────
  // 2) TAXII Intelligence Sync
  // ─────────────────────────────────────────────
  logger.info("[INTEL] Syncing MITRE ATT&CK via TAXII...");
  // TAXII con telemetría
  let techniques;
  try {
    techniques = await withStageTiming("taxii", async () => {
      try {
        const t = await TaxiiClient.sync();
        if (!Array.isArray(t) || !t.every(x => x && x.external_id && x.name)) {
          throw new Error("[INTEL] Invalid MITRE techniques structure");
        }
        logger.info(`[INTEL] Techniques downloaded: ${t.length}`);
        return t;
      } catch (err) {
        logger.error(`[INTEL] Error sincronizando TAXII: ${err.message}`, { error: err });
        logger.warn("[INTEL] Usando técnicas MITRE de ejemplo.");
        return [
          { external_id: "T1046", name: "Network Service Scanning", kill_chain: "reconnaissance" },
          { external_id: "T1133", name: "External Remote Services", kill_chain: "initial-access" },
          { external_id: "T1021", name: "Remote Services", kill_chain: "lateral-movement" }
        ];
      }
    });
  } catch (err) {
    pipelineStatus = "ERROR";
    pipelineError = err;
    logger.error("[INTEL] Error crítico en TAXII", { error: err });
    emitEvent("metric", { type: "PIPELINE_END", status: "ERROR", error: err.message });
    throw err;
  }

  // ─────────────────────────────────────────────
  // 3) Threat Mapper Correlation
  // ─────────────────────────────────────────────
  logger.info("[MAP] Correlating assets with MITRE + NIST...");
  // Threat Mapper y Risk Engine con telemetría
  let mitreHeatmapData = [];
  let nistPlan = [];
  let risk = {};
  let cisControls = [];
  try {
    mitreHeatmapData = await withStageTiming("threat-mapper", () => buildMitreHeatmap(techniques, assets));
    nistPlan = buildNistPlan(mitreHeatmapData, assets);
    risk = await withStageTiming("risk-engine", () => Promise.resolve(computeRisk(assets, mitreHeatmapData)));
    cisControls = generateCisControls(mitreHeatmapData);
    logger.info("[MAP] Correlación completada.");
  } catch (err) {
    pipelineStatus = "ERROR";
    pipelineError = err;
    logger.error(`[MAP] Error en correlación: ${err.message}`, { error: err });
    mitreHeatmapData = [];
    nistPlan = [];
    risk = {};
    cisControls = [];
  }
  emitEvent("metric", { type: "PIPELINE_END", status: pipelineStatus, error: pipelineError ? pipelineError.message : undefined });

  // ─────────────────────────────────────────────
  // 4) Export to Dashboard (JSON)
  // ─────────────────────────────────────────────
  logger.info("[UI] Exporting data for dashboard...");
  try {
    fs.writeFileSync(pathConfig.dashboardMitre, JSON.stringify(mitreHeatmapData, null, 2));
    fs.writeFileSync(pathConfig.dashboardNist, JSON.stringify(nistPlan, null, 2));
    fs.writeFileSync(path.join(pathConfig.dashboardDir, "dashboard-risk.json"), JSON.stringify(risk, null, 2));
    fs.writeFileSync(path.join(pathConfig.dashboardDir, "dashboard-cis.json"), JSON.stringify(cisControls, null, 2));
    logger.info("[UI] Datos exportados para dashboard.");
  } catch (err) {
    logger.error(`[UI] Error exportando datos de dashboard: ${err.message}`, { error: err });
  }
  logger.info("[ARES‑11] Pipeline finalizado.");
}
