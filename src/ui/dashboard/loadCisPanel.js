import { renderCisPanel } from "./cisPanel.js";

export async function loadCisPanel() {
  const cis = await fetch("./dashboard-cis.json").then(r => r.json());
  renderCisPanel(cis);
}

// Autoejecutar al cargar
loadCisPanel();
