
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Panel de Métricas de Rendimiento
//  Arquitectura: Renderizador de promedios por etapa del pipeline
//  Extensible: Añadir nuevas métricas y visualizaciones
// ────────────────────────────────────────────────────────────────────────────────

/**
 * Renderiza el panel de rendimiento con promedios por etapa.
 * @param {Array} events - Lista de eventos de telemetría
 */
export function renderPerformancePanel(events) {
  const el = document.getElementById("performance-panel");
  if (!el) return;

  const stages = events.filter(e => e.type === "PIPELINE_STAGE");

  if (!stages.length) {
    el.innerHTML = "<em>No performance data yet</em>";
    return;
  }

  const stats = {};

  stages.forEach(e => {
    if (!stats[e.stage]) stats[e.stage] = { total: 0, count: 0 };
    stats[e.stage].total += e.durationMs || 0;
    stats[e.stage].count++;
  });

  const rows = Object.entries(stats)
    .map(([stage, v]) => {
      const avg = Math.round(v.total / v.count);
      return `
        <tr>
          <td>${stage}</td>
          <td>${avg} ms</td>
          <td>${v.count}</td>
        </tr>
      `;
    })
    .join("");

  el.innerHTML = `
    <table class="metrics-table">
      <thead>
        <tr>
          <th>Stage</th>
          <th>Avg Duration</th>
          <th>Runs</th>
        </tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>
  `;
}
