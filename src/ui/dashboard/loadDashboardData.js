
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Loader de Datos para Dashboard
//  Arquitectura: Carga y renderiza datos MITRE y NIST en paneles
//  Extensible: Añadir nuevos orígenes y paneles
// ────────────────────────────────────────────────────────────────────────────────
import { renderMitreHeatmap } from "./mitreHeatmap.js";
import { renderNistPanel } from "./renderNistPanel.js";

/**
 * Carga y renderiza datos para el dashboard táctico
 * @function
 */
async function loadDashboardData() {
  const mitre = await fetch("./dashboard-mitre.json").then(r => r.json());
  const nist = await fetch("./dashboard-nist.json").then(r => r.json());

  renderMitreHeatmap(mitre);
  renderNistPanel(nist);
}

loadDashboardData();
