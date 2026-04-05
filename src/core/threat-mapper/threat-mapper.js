// Genera controles CIS por técnica para exportación dashboard
/**
 * Genera controles CIS por técnica para exportación dashboard
 */
export function generateCisControls(heatmap) {
  if (!Array.isArray(heatmap)) return [];
  return heatmap.map(t => ({
    techniqueId: t.id || t.external_id,
    control: "CIS 1.1 - Inventory of Assets",
    IG1: "Identificar activos",
    IG2: "Endurecimiento básico",
    IG3: "Automatización continua"
  }));
}
// Threat Mapper Engine — correlación mínima pero realista

// Reglas de mapeo MITRE ↔ NIST CSF (simplificadas)
const mitreToNist = {
  T1046: {
    nist: ["ID.AM-1", "ID.RA-1"],
    func: "ID"
  },
  T1133: {
    nist: ["PR.AC-3", "PR.IP-1"],
    func: "PR"
  },
  T1021: {
    nist: ["DE.CM-7"],
    func: "DE"
  }
};

// Construye datos para el heatmap MITRE

import { loadKEV, matchKevByCve, kevSeverityBoost } from "../kev/kevClient.js";

// techniques: [{ id, name, cves: [], severity }]
// assets: lo que ya uses
/**
 * Construye datos para el heatmap MITRE enriquecido con KEV
 */
export async function buildMitreHeatmap(techniques, assets) {
  if (!Array.isArray(techniques)) return [];
  const kevEntries = await loadKEV();
  return techniques.map(t => {
    if (!t) return null;
    const kevMatches = matchKevByCve(t.cves || [], kevEntries);
    const kevBoost = kevSeverityBoost(kevMatches);
    const baseSeverity = t.severity || "medium";
    const baseScore = baseSeverity === "high" ? 5 : baseSeverity === "medium" ? 3 : 1;
    const totalScore = baseScore + kevBoost;
    return {
      ...t,
      kevMatches,
      kevBoost,
      totalScore,
      isKev: kevMatches.length > 0
    };
  }).filter(Boolean);
}

// NIST plan puede usar ya el heatmap enriquecido
export function buildNistPlan(heatmap) {
  return (heatmap || []).map(t => ({
    techniqueId: t.id,
    category: "PROTECT",
    priority: t.isKev ? "CRITICAL" : "NORMAL"
  }));
}

// Construye datos para el panel NIST CSF
export function buildNistPlan(techniques, assets) {
  const functions = {
    ID: { id: "ID", name: "Identify", priority: "LOW", controls: new Set() },
    PR: { id: "PR", name: "Protect", priority: "LOW", controls: new Set() },
    DE: { id: "DE", name: "Detect", priority: "LOW", controls: new Set() }
  };

  const hasRemoteExposure = assets.some(a =>
    a.port === 22 || a.port === 3389
  );

  techniques.forEach(t => {
    const map = mitreToNist[t.external_id];
    if (!map) return;

    const fn = functions[map.func];
    map.nist.forEach(c => fn.controls.add(c));

    // Priorización mínima basada en exposición
    if (hasRemoteExposure && map.func === "PR") {
      fn.priority = "HIGH";
    } else if (hasRemoteExposure) {
      fn.priority = "MEDIUM";
    } else {
      fn.priority = "LOW";
    }
  });

  // Convertimos Sets a arrays y filtramos funciones sin controles
  return Object.values(functions)
    .map(f => ({
      id: f.id,
      name: f.name,
      priority: f.priority,
      controls: Array.from(f.controls)
    }))
    .filter(f => f.controls.length > 0);
}
