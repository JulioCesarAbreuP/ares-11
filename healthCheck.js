// healthCheck.js — Diagnóstico centralizado de ARES-11
import { TaxiiClient } from "./src/core/taxii-client/taxiiClient.js";
import { buildMitreHeatmap } from "./src/core/threat-mapper/threat-mapper.js";
import { computeRisk } from "./src/core/risk-engine/riskEngine.js";
import { remediationPlan } from "./src/core/remediation-engine/remediationEngine.js";
import { loadKEV } from "./src/core/kev/kevClient.js";
import fs from "fs";
import pathConfig from "./src/config/paths.config.json" assert { type: "json" };
import { logger } from "./src/utils/logger.js";

async function healthCheck() {
  logger.info("[HEALTH] Iniciando diagnóstico de ARES-11...");
  const report = [];

  // 1. Fingerprinting
  let fpStatus = "OK";
  try {
    if (!fs.existsSync(pathConfig.fingerprintOutput)) throw new Error("No fingerprint output");
    const assets = JSON.parse(fs.readFileSync(pathConfig.fingerprintOutput, "utf8"));
    if (!Array.isArray(assets) || assets.length === 0) throw new Error("Sin assets detectados");
  } catch (e) {
    fpStatus = "FALLBACK/ERROR";
  }
  report.push({ modulo: "Fingerprinting", estado: fpStatus });

  // 2. TAXII
  let taxiiStatus = "OK";
  try {
    const techniques = await TaxiiClient.sync();
    if (!Array.isArray(techniques) || techniques.length === 0) throw new Error("Sin técnicas");
  } catch (e) {
    taxiiStatus = "FALLBACK/ERROR";
  }
  report.push({ modulo: "TAXII", estado: taxiiStatus });

  // 3. Threat Mapper
  let tmStatus = "OK";
  try {
    const techniques = [{ external_id: "T1046", name: "Test" }];
    const assets = [{ ip: "127.0.0.1", port: 80, service: "open" }];
    const heatmap = await buildMitreHeatmap(techniques, assets);
    if (!Array.isArray(heatmap)) throw new Error("No heatmap");
  } catch (e) {
    tmStatus = "FALLBACK/ERROR";
  }
  report.push({ modulo: "Threat Mapper", estado: tmStatus });

  // 4. Risk Engine
  let riskStatus = "OK";
  try {
    const risk = computeRisk([{ ip: "127.0.0.1", port: 80, service: "open" }], [{ severity: "high", kevBoost: 3, isKev: true }]);
    if (!risk || typeof risk.score !== "number") throw new Error("Sin score");
  } catch (e) {
    riskStatus = "FALLBACK/ERROR";
  }
  report.push({ modulo: "Risk Engine", estado: riskStatus });

  // 5. Remediation Engine
  let remStatus = "OK";
  try {
    const rem = remediationPlan([{ id: "T1046", isKev: true }]);
    if (!Array.isArray(rem)) throw new Error("No remediaciones");
  } catch (e) {
    remStatus = "FALLBACK/ERROR";
  }
  report.push({ modulo: "Remediation Engine", estado: remStatus });

  // 6. KEV
  let kevStatus = "OK";
  try {
    const kev = await loadKEV();
    if (!Array.isArray(kev) || kev.length === 0) throw new Error("No KEV");
  } catch (e) {
    kevStatus = "FALLBACK/ERROR";
  }
  report.push({ modulo: "KEV", estado: kevStatus });

  // 7. Dashboard JSONs
  let dashStatus = "OK";
  try {
    [pathConfig.dashboardMitre, pathConfig.dashboardNist, pathConfig.dashboardDir + "/dashboard-risk.json", pathConfig.dashboardDir + "/dashboard-cis.json"].forEach(f => {
      if (!fs.existsSync(f)) throw new Error(f + " no existe");
    });
  } catch (e) {
    dashStatus = "FALLBACK/ERROR";
  }
  report.push({ modulo: "Dashboard", estado: dashStatus });

  // Resultado
  logger.info("[HEALTH] Diagnóstico completo:");
  report.forEach(r => logger.info(`${r.modulo}: ${r.estado}`));
  fs.writeFileSync("health-report.json", JSON.stringify(report, null, 2));
  logger.info("[HEALTH] Reporte guardado en health-report.json");
}

healthCheck();
