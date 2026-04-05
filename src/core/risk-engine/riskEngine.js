// Importación explícita para IRP-02
import { buildMitreHeatmap } from "../threat-mapper/threat-mapper.js";

/**
 * Wrapper opcional: permite calcular el riesgo directamente desde técnicas y assets,
 * usando internamente el Threat Mapper (buildMitreHeatmap).
 * Cumple con el check IRP-02.
 */
/**
 * Calcula el riesgo a partir de técnicas MITRE y assets.
 * Valida entradas y usa Threat Mapper internamente.
 */
export async function computeRiskFromTechniques(mitreTechniques, assets) {
  if (!Array.isArray(mitreTechniques) || !Array.isArray(assets)) {
    return { score: 0, level: "LOW", kevTechniques: [], totalTechniques: 0 };
  }
  const heatmap = await buildMitreHeatmap(mitreTechniques, assets);
  return computeRisk(assets, heatmap);
}

// Risk Engine — usa el heatmap enriquecido con KEV

export function riskScore(heatmap) {
  if (!Array.isArray(heatmap)) return 0;
  let score = 0;
  for (const t of heatmap) {
    if (!t) continue;
    const base = t.severity === "high" ? 5 : t.severity === "medium" ? 3 : 1;
    const kev = t.kevBoost || 0;
    score += base + kev;
  }
  return score;
}

export function computeRisk(assets, heatmap) {
  // Valida entradas
  if (!Array.isArray(assets) || !Array.isArray(heatmap)) {
    return { score: 0, level: "LOW", kevTechniques: [], totalTechniques: 0 };
  }
  const score = riskScore(heatmap);
  const level =
    score > 100 ? "CRITICAL" : score > 60 ? "HIGH" : score > 30 ? "MEDIUM" : "LOW";
  const kevTechniques = (heatmap || []).filter(t => t && t.isKev);
  return {
    score,
    level,
    kevTechniques,
    totalTechniques: heatmap.length
  };
}
  
