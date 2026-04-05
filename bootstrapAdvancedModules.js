// ARES‑11 — Advanced Modules Bootstrap
// Crea todos los módulos faltantes para subir de 20/40 a 40/40 en IRP‑02

import fs from "fs";
import path from "path";

const root = path.resolve("src");

function ensureDir(p) {
  if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
}

function writeIfMissing(relPath, content) {
  const full = path.join(root, relPath);
  ensureDir(path.dirname(full));
  if (!fs.existsSync(full)) {
    fs.writeFileSync(full, content.trimStart() + "\n");
    console.log(`✔️ Creado: ${relPath}`);
  } else {
    console.log(`ℹ️ Ya existe, no se modifica: ${relPath}`);
  }
}

/* =========================
   ADR‑004 — Risk Engine
   ========================= */
writeIfMissing(
  "core/risk-engine/riskEngine.js",
  `
  import { buildMitreHeatmap } from "../threat-mapper/threat-mapper.js";

  // Modelo simple de riesgo: combina número de técnicas y criticidad
  export function riskScore(techniques) {
    if (!Array.isArray(techniques)) return 0;
    const base = techniques.length;
    const high = techniques.filter(t => t.severity === "high").length;
    const medium = techniques.filter(t => t.severity === "medium").length;
    return base + high * 3 + medium * 2;
  }

  export function computeRisk(assets, mitreTechniques) {
    const heatmap = buildMitreHeatmap(mitreTechniques, assets || []);
    const score = riskScore(heatmap);
    return {
      score,
      level: score > 50 ? "HIGH" : score > 20 ? "MEDIUM" : "LOW",
      techniques: heatmap
    };
  }
  `
);

/* =========================
   ADR‑005 — Remediation Engine
   ========================= */
writeIfMissing(
  "core/remediation-engine/remediationEngine.js",
  `
  const cisMap = {
    "T1059": {
      control: "CIS 8.2 - Inventory and Control of Software Assets",
      IG1: "Inventariar software crítico",
      IG2: "Aplicar listas blancas",
      IG3: "Automatizar control de ejecución"
    }
  };

  export function remediationForTechnique(techniqueId) {
    const base = cisMap[techniqueId] || {
      control: "CIS 1.1 - Inventory of Assets",
      IG1: "Identificar activos afectados",
      IG2: "Aplicar endurecimiento básico",
      IG3: "Automatizar verificación continua"
    };

    return {
      technique: techniqueId,
      control: base.control,
      IG1: base.IG1,
      IG2: base.IG2,
      IG3: base.IG3
    };
  }

  export function remediationPlan(techniques) {
    if (!Array.isArray(techniques)) return [];
    return techniques.map(t => remediationForTechnique(t.id || t.techniqueId || "UNKNOWN"));
  }
  `
);

/* =========================
   CISA KEV Client
   ========================= */
writeIfMissing(
  "core/kev/kevClient.js",
  `
  // Cliente KEV simplificado: en producción, aquí se haría fetch a CISA
  export async function loadKEV() {
    // Placeholder estático
    return [
      { cve: "CVE-2023-12345", exploited: true, vendor: "Example", product: "ExampleApp" },
      { cve: "CVE-2024-00001", exploited: true, vendor: "Example", product: "ExampleService" }
    ];
  }

  export function matchKevByCve(cveList, kevEntries) {
    const kevSet = new Set(kevEntries.map(k => k.cve));
    return cveList.filter(c => kevSet.has(c));
  }
  `
);

/* =========================
   CIS Panel (UI)
   ========================= */
writeIfMissing(
  "ui/dashboard/cisPanel.js",
  `
  export function renderCisPanel(data) {
    const el = document.getElementById("cis-panel");
    if (!el) return;
    if (!Array.isArray(data)) {
      el.innerHTML = "<em>No CIS data available</em>";
      return;
    }

    el.innerHTML = data
      .map(function(c) {
        return (
          '<div class="cis-item">' +
            '<div class="cis-control">' + (c.control || '') + '</div>' +
            '<div class="cis-ig">' +
              '<span>IG1: ' + (c.IG1 || '') + '</span>' +
              '<span>IG2: ' + (c.IG2 || '') + '</span>' +
              '<span>IG3: ' + (c.IG3 || '') + '</span>' +
            '</div>' +
          '</div>'
        );
      })
      .join("");
  }
  `
);

/* =========================
   CIS CSS
   ========================= */
writeIfMissing(
  "ui/styles/cis.css",
  `
  #cis-panel {
    padding: 12px;
    border: 1px solid #333;
    border-radius: 6px;
    background: #111827;
    color: #e5e7eb;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .cis-item {
    padding: 8px 0;
    border-bottom: 1px solid #1f2933;
  }

  .cis-item:last-child {
    border-bottom: none;
  }

  .cis-control {
    font-weight: 600;
    margin-bottom: 4px;
  }

  .cis-ig {
    display: flex;
    gap: 12px;
    font-size: 0.85rem;
    color: #9ca3af;
  }
  `
);

/* =========================
   CIS JSON
   ========================= */
writeIfMissing(
  "ui/dashboard/dashboard-cis.json",
  `
  [
    {
      "control": "CIS 1.1 - Inventory of Authorized and Unauthorized Devices",
      "IG1": "Mantener inventario básico de dispositivos",
      "IG2": "Correlacionar inventario con vulnerabilidades",
      "IG3": "Automatizar descubrimiento y reconciliación"
    },
    {
      "control": "CIS 4.1 - Establish and Maintain a Secure Configuration Process",
      "IG1": "Definir configuraciones seguras base",
      "IG2": "Aplicar configuraciones mediante herramientas centralizadas",
      "IG3": "Monitorizar desviaciones en tiempo casi real"
    }
  ]
  `
);

/* =========================
   Tactical Terminal
   ========================= */
writeIfMissing(
  "ui/dashboard/tacticalTerminal.js",
  `
  export function renderTerminal(events = []) {
    const el = document.getElementById("tactical-terminal");
    if (!el) return;

    if (!Array.isArray(events) || events.length === 0) {
      el.innerHTML = "<em>No events yet. Waiting for telemetry...</em>";
      return;
    }

    el.innerHTML = events
      .map(function(e) {
        return (
          '<div class="tt-event">' +
            '<span class="tt-ts">' + (e.timestamp || '') + '</span>' +
            '<span class="tt-type">' + (e.type || 'INFO') + '</span>' +
            '<span class="tt-msg">' + (e.message || '') + '</span>' +
          '</div>'
        );
      })
      .join("");
  }
  `
);

console.log("\n✅ Bootstrap completado. Ahora añade en tu index.html:");
console.log('- <div id="risk-panel"></div>');
console.log('- <div id="remediation-panel"></div>');
console.log('- <div id="kev-panel"></div>');
console.log('- <div id="cis-panel"></div>');
console.log('- <div id="tactical-terminal"></div>');
console.log('\nY asegúrate de importar: cisPanel.js y tacticalTerminal.js donde corresponda.\n');
