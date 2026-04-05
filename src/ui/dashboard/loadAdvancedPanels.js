import { renderTerminal, subscribeTerminalToTelemetry, pushTerminalEvent } from "./tacticalTerminal.js";
import { subscribe } from "../../utils/telemetryBus.js";
import { renderPerformancePanel } from "./performancePanel.js";

import { remediationPlan } from "../../../core/remediation-engine/remediationEngine.js";

// Render helpers (puedes personalizar el renderizado)
function renderRiskPanel(risk) {
  const el = document.getElementById("risk-panel");
  if (!el) return;
  if (!risk) {
    el.innerHTML = "<em>No hay datos de riesgo</em>";
    return;
  }
  el.innerHTML = `
    <div><b>Score:</b> ${risk.score} <b>Nivel:</b> ${risk.level}</div>
    <div><b>Técnicas KEV detectadas:</b> ${risk.kevTechniques && risk.kevTechniques.length > 0 ? risk.kevTechniques.map(t => `<span class="risk-kev-tech">${t.id || t.external_id || "?"}</span>`).join(", ") : "Ninguna"}</div>
    <div style="font-size:0.9em;opacity:0.7;">Total técnicas analizadas: ${risk.totalTechniques}</div>
  `;
}
// Estilo visual para técnicas KEV en el panel de riesgo
const style = document.createElement('style');
style.innerHTML = `.risk-kev-tech { color: #ffd700; font-weight: bold; margin-right: 6px; }`;
document.head.appendChild(style);

function renderRemediationPanel(remediations) {
  const el = document.getElementById("remediation-panel");
  if (!el) return;
  if (!Array.isArray(remediations) || remediations.length === 0) {
    el.innerHTML = "<em>No hay recomendaciones</em>";
    return;
  }
  el.innerHTML = remediations.map(r => {
    const isKev = r.recommendation && r.recommendation.includes("KEV");
    return `
      <div class="rem-item">
        <b>${r.technique}</b>: ${r.control}<br>
        IG1: ${r.IG1} | IG2: ${r.IG2} | IG3: ${r.IG3}<br>
        <span class="rem-recommendation${isKev ? ' kev-highlight' : ''}"><b>Recomendación:</b> ${r.recommendation || ''}</span>
      </div>
    `;
  }).join("");
// Estilo visual para recomendaciones KEV en el panel de remediación
const styleRemKev = document.createElement('style');
styleRemKev.innerHTML = `.rem-recommendation.kev-highlight { background: #2d2300; border-left: 5px solid #ffd700; color: #ffd700; font-weight: bold; box-shadow: 0 2px 8px #ffd70033; }`;
document.head.appendChild(styleRemKev);
}

function renderKevPanel(kev) {
  const el = document.getElementById("kev-panel");
  if (!el) return;
  if (!Array.isArray(kev) || kev.length === 0) {
    el.innerHTML = "<em>No hay CVEs KEV</em>";
    return;
  }
  el.innerHTML = kev.map(k => `
    <div class="kev-item">
      <b>${k.cve}</b> (${k.vendor} - ${k.product})
    </div>
  `).join("");
}

  // Cargar datos persistidos
  const [risk, mitre] = await Promise.all([
    fetch("./dashboard-risk.json").then(r => r.json()),
    fetch("./dashboard-mitre.json").then(r => r.json())
  ]);

  renderRiskPanel(risk);

  // Panel de remediación basado en heatmap enriquecido persistido
  const remediations = remediationPlan(mitre);
  renderRemediationPanel(remediations);

  // Precargar historial de telemetría antes de la suscripción en tiempo real
  fetch("/api/telemetry.json")
    .then(r => r.json())
    .then(events => {
      events.forEach(e => pushTerminalEvent(e));
      renderPerformancePanel(events);
    })
    .catch(() => pushTerminalEvent({ message: "No telemetry yet" }));

  // Suscribir el terminal táctico al bus de telemetría para eventos en tiempo real
  subscribeTerminalToTelemetry(subscribe);
}

// Autoejecutar
loadAdvancedPanels();

export function loadTelemetry() {
  fetch("/api/telemetry")
    .then(r => r.json())
    .then(events => {
      events.forEach(e => pushTerminalEvent(e));
      renderPerformancePanel(events);
    });
}
