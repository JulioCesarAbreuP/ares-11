
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Panel Heatmap MITRE ATT&CK
//  Arquitectura: Renderizador D3.js de técnicas MITRE y severidad
//  Extensible: Añadir nuevos estilos y atributos según contexto de riesgo
// ────────────────────────────────────────────────────────────────────────────────
import * as d3 from "d3";

/**
 * Renderiza un Heatmap táctico basado en técnicas MITRE ATT&CK
 * Cada técnica se representa como una celda:
 *  - CRITICAL → rojo pulsante
 *  - STABLE → verde tenue
 * @param {Array} data - Técnicas MITRE enriquecidas
 */
export function renderMitreHeatmap(data) {
  const container = d3.select("#mitre-heatmap");

  // Limpia render previo
  container.selectAll("*").remove();

  const cellSize = 140;
  const padding = 6;

  const grid = container
    .style("display", "grid")
    .style("grid-template-columns", `repeat(auto-fill, minmax(${cellSize}px, 1fr))`)
    .style("gap", `${padding}px`);

  // Render de cada técnica MITRE
  grid
    .selectAll("div")
    .data(data)
    .enter()
    .append("div")
    .attr("class", d => `technique-cell ${d.status}`)
    .style("padding", "10px")
    .style("border", "1px solid #30363d")
    .style("background", "#0a0c10")
    .style("color", "#c9d1d9")
    .style("font-size", "0.75rem")
    .style("text-align", "center")
    .style("transition", "all 0.3s ease")
    .html(d => `
      <strong>${d.external_id || "???"}</strong><br>
      ${d.name}<br>
      <span style="font-size: 0.65rem; opacity: 0.7;">
        ${d.kill_chain || ""}
      </span>
      ${d.kevMatch ? '<span title="KEV: Vulnerabilidad explotada" style="display:inline-block;margin-top:4px;font-size:1.2em;vertical-align:middle;">🛡️<span style="color:#ffd700;font-size:0.8em;">KEV</span></span>' : ''}
    `);
}
