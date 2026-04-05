import { renderPerformancePanel } from "./performancePanel.js";

let events = [];

// Carga inicial de métricas históricas
export async function loadPerformancePanel() {
  try {
    const res = await fetch("/api/telemetry?type=PIPELINE_STAGE&limit=200");
    events = await res.json();
    renderPerformancePanel(events);
  } catch (err) {
    const el = document.getElementById("performance-panel");
    if (el) el.innerHTML = `<em>Error cargando métricas: ${err.message}</em>`;
  }
}

// Llama automáticamente al cargar el módulo
loadPerformancePanel();

// Actualización en tiempo real con SSE
const es = new EventSource("/api/telemetry-stream");
es.onmessage = msg => {
  try {
    const event = JSON.parse(msg.data);
    if (event.type === "PIPELINE_STAGE") {
      events.push(event);
      // Limita el buffer a los últimos 200 eventos
      if (events.length > 200) events = events.slice(-200);
      renderPerformancePanel(events);
    }
  } catch {}
};
