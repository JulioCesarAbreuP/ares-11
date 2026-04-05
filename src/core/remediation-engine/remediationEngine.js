
// Remediation Engine — prioriza técnicas KEV y mapea a CIS / IG1/2/3
// Genera una recomendación base para una técnica
function baseRemediation(techniqueId, isKev) {
  const base = {
    control: "CIS 1.1 - Inventory of Assets",
    IG1: "Identificar activos afectados",
    IG2: "Aplicar endurecimiento básico",
    IG3: "Automatizar verificación continua"
  };
  const kevNote = isKev
    ? "Priorizar esta técnica por estar asociada a KEV explotado activamente."
    : "Revisar exposición y aplicar controles estándar.";
  return {
    technique: techniqueId,
    control: base.control,
    IG1: base.IG1,
    IG2: base.IG2,
    IG3: base.IG3,
    recommendation: kevNote
  };
}

/**
 * Genera un plan de remediación a partir del heatmap enriquecido
 */
export function remediationPlan(heatmap) {
  if (!Array.isArray(heatmap)) return [];
  return heatmap.map(t =>
    baseRemediation(t.id || t.techniqueId || "UNKNOWN", t && t.isKev)
  );
}
  
