/**
 * ARES—11 — ULTRA ARCHITECTURE RADAR
 * Nivel: Staff/Lead Architect
 *
 * Validador arquitectónico avanzado:
 *  - camelCase, imports, JSON, ciclos, dependencias, métricas, fan-in/fan-out, God Files
 *  - Radar de arquitectura (JSON/Markdown)
 *  - Reporte HTML ULTRA
 *
 * Uso:
 *   node src/utils/validateProjectULTRA.js
 *
 * Extensible: Añadir nuevas métricas y reglas en las funciones auxiliares.
 */

import fs from "fs";
import path from "path";

const root = path.resolve("src");
const reportHtmlPath = path.resolve("validation-report-ULTRA.html");
const radarJsonPath = path.resolve("architecture-radar.json");
const radarMdPath = path.resolve("architecture-radar.md");

let report = [];
let totalErrors = 0;

// Métricas globales: líneas, complejidad, fan-in/fan-out
const metrics = {
  files: {}, // file -> { lines, complexity, fanIn, fanOut }
};

/**
 * Log auxiliar para reporte HTML
 * @param {string} msg
 */
function log(msg) {
  console.log(msg);
  report.push(`<p>${msg}</p>`);
}

/**
 * Marca OK en el reporte
 * @param {string} msg
 */
function ok(msg) {
  console.log(`✔️ ${msg}`);
  report.push(`<p style="color: #2ecc71">✔️ ${msg}</p>`);
}

/**
 * Marca error en el reporte
 * @param {string} msg
 */
function error(msg) {
  console.log(`❌ ${msg}`);
  report.push(`<p style="color: #e74c3c">❌ ${msg}</p>`);
  totalErrors++;
}

/**
 * Obtiene todos los archivos recursivamente
 * @param {string} dir
 * @param {string|null} extFilter
 * @returns {string[]}
 */
function getAllFiles(dir, extFilter = null) {
  let results = [];
  const list = fs.readdirSync(dir);

  list.forEach(file => {
    const full = path.join(dir, file);
    const stat = fs.statSync(full);

    if (stat.isDirectory()) {
      results = results.concat(getAllFiles(full, extFilter));
    } else {
      if (!extFilter || file.endsWith(extFilter)) {
        results.push(full);
      }
    }
  });

  return results;
}

/**
 * Valida convención camelCase en archivos
 */
function validateCamelCase() {
  log("<h2>Validación camelCase</h2>");

  const files = getAllFiles(root);
  const camelCaseRegex = /^[a-z][A-Za-z0-9]*\.(js|json|css|go|html)$/;

  files.forEach(file => {
    const name = path.basename(file);

    if (!camelCaseRegex.test(name)) {
      error(`No camelCase: ${file.replace(root + "/", "")}`);
    } else {
      ok(`camelCase OK: ${file.replace(root + "/", "")}`);
    }
  });
}

function analyzeJsMetrics() {
  log("<h2>Métricas de complejidad y tamaño</h2>");

  const jsFiles = getAllFiles(root, ".js");

  jsFiles.forEach(file => {
    const rel = file.replace(root + "/", "");
    const content = fs.readFileSync(file, "utf8");
    const lines = content.split("\n").length;

    // Complejidad aproximada: cuenta if, for, while, switch, case, &&, ||, ?:
    const complexity =
      (content.match(/\bif\b/g) || []).length +
      (content.match(/\bfor\b/g) || []).length +
      (content.match(/\bwhile\b/g) || []).length +
      (content.match(/\bswitch\b/g) || []).length +
      (content.match(/\bcase\b/g) || []).length +
      (content.match(/&&/g) || []).length +
      (content.match(/\|\|/g) || []).length +
      (content.match(/\?/g) || []).length;

    metrics.files[rel] = metrics.files[rel] || {
      lines: 0,
      complexity: 0,
      fanIn: 0,
      fanOut: 0
    };

    metrics.files[rel].lines = lines;
    metrics.files[rel].complexity = complexity;

    ok(`Métricas: ${rel} — líneas=${lines}, complejidad≈${complexity}`);
  });
}

function validateImportsAndBuildGraph() {
  log("<h2>Validación de imports + grafo de dependencias</h2>");

  const jsFiles = getAllFiles(root, ".js");
  const graph = {};

  jsFiles.forEach(file => {
    const content = fs.readFileSync(file, "utf8");
    const importRegex = /import\s+.*?from\s+["'](.+?)["']/g;

    const from = file.replace(root + "/", "");
    graph[from] = graph[from] || [];
    metrics.files[from] = metrics.files[from] || {
      lines: 0,
      complexity: 0,
      fanIn: 0,
      fanOut: 0
    };

    let match;
    while ((match = importRegex.exec(content)) !== null) {
      const importPath = match[1];
      if (!importPath.startsWith(".")) continue;

      const resolved = path.resolve(path.dirname(file), importPath);
      let target = null;

      if (fs.existsSync(resolved)) target = resolved;
      else if (fs.existsSync(resolved + ".js")) target = resolved + ".js";
      else if (fs.existsSync(resolved + ".json")) target = resolved + ".json";

      if (!target) {
        error(`Import roto en ${from}: ${importPath}`);
      } else {
        const to = target.replace(root + "/", "");
        graph[from].push(to);

        metrics.files[from].fanOut++;
        metrics.files[to] = metrics.files[to] || {
          lines: 0,
          complexity: 0,
          fanIn: 0,
          fanOut: 0
        };
        metrics.files[to].fanIn++;

        ok(`Import OK: ${from} → ${to}`);
      }
    }
  });

  return graph;
}

function validateJSON() {
  log("<h2>Validación de JSON</h2>");

  const jsonFiles = getAllFiles(root, ".json");

  jsonFiles.forEach(file => {
    try {
      JSON.parse(fs.readFileSync(file, "utf8"));
      ok(`JSON válido: ${file.replace(root + "/", "")}`);
    } catch {
      error(`JSON corrupto: ${file.replace(root + "/", "")}`);
    }
  });
}

function detectCycles(graph) {
  log("<h2>Detección de ciclos de dependencias</h2>");

  const visited = new Set();
  const stack = new Set();

  function dfs(node, pathStack) {
    if (stack.has(node)) {
      error(`Ciclo detectado: ${[...pathStack, node].join(" → ")}`);
      return;
    }

    if (visited.has(node)) return;

    visited.add(node);
    stack.add(node);

    (graph[node] || []).forEach(child => dfs(child, [...pathStack, child]));

    stack.delete(node);
  }

  Object.keys(graph).forEach(node => dfs(node, [node]));
}

function generateMermaidGraph(graph) {
  log("<h2>Mapa de dependencias (Mermaid)</h2>");

  let mermaid = "graph TD\n";

  Object.entries(graph).forEach(([from, tos]) => {
    tos.forEach(to => {
      mermaid += `  "${from}" --> "${to}"\n`;
    });
  });

  report.push(`<pre class="mermaid">${mermaid}</pre>`);
}

function detectGodFiles() {
  log("<h2>Detección de God Files</h2>");

  // Umbrales heurísticos
  const LINE_THRESHOLD = 300;
  const COMPLEXITY_THRESHOLD = 40;
  const FANOUT_THRESHOLD = 10;

  Object.entries(metrics.files).forEach(([file, m]) => {
    const isBig = m.lines >= LINE_THRESHOLD;
    const isComplex = m.complexity >= COMPLEXITY_THRESHOLD;
    const isHighlyCoupled = m.fanOut >= FANOUT_THRESHOLD;

    if (isBig || isComplex || isHighlyCoupled) {
      error(
        `God file candidato: ${file} — líneas=${m.lines}, complejidad≈${m.complexity}, fanOut=${m.fanOut}, fanIn=${m.fanIn}`
      );
    } else {
      ok(
        `Módulo sano: ${file} — líneas=${m.lines}, complejidad≈${m.complexity}, fanOut=${m.fanOut}, fanIn=${m.fanIn}`
      );
    }
  });
}

function generateRadarArtifacts() {
  log("<h2>Generando Architecture Radar (JSON + Markdown)</h2>");

  const radar = Object.entries(metrics.files).map(([file, m]) => ({
    file,
    lines: m.lines,
    complexity: m.complexity,
    fanIn: m.fanIn,
    fanOut: m.fanOut
  }));

  fs.writeFileSync(radarJsonPath, JSON.stringify(radar, null, 2));

  let md = "# ARES‑11 — Architecture Radar\n\n";
  md += "| File | Lines | Complexity≈ | FanIn | FanOut |\n";
  md += "|------|-------|------------|-------|--------|\n";

  radar.forEach(r => {
    md += `| ${r.file} | ${r.lines} | ${r.complexity} | ${r.fanIn} | ${r.fanOut} |\n`;
  });

  fs.writeFileSync(radarMdPath, md);

  ok(`Radar JSON: ${radarJsonPath}`);
  ok(`Radar Markdown: ${radarMdPath}`);
}

function generateHTMLReport() {
  const badge =
    totalErrors === 0
      ? `<div style="background:#2ecc71;color:white;padding:10px;border-radius:6px;width:120px;text-align:center">STATUS: OK</div>`
      : `<div style="background:#e74c3c;color:white;padding:10px;border-radius:6px;width:120px;text-align:center">STATUS: FAIL</div>`;

  const html = `
  <html>
  <head>
    <title>ARES‑11 ULTRA Validation Report</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({ startOnLoad: true, theme: "dark" });</script>
    <style>
      body { font-family: Arial; padding: 20px; background: #111; color: #ddd; }
      h1, h2 { color: #fff; }
      p { margin: 4px 0; }
      pre { background: #222; padding: 10px; border-radius: 6px; }
    </style>
  </head>
  <body>
    <h1>ARES‑11 — ULTRA Validation Report</h1>
    ${badge}
    ${report.join("\n")}
  </body>
  </html>
  `;

  fs.writeFileSync(reportHtmlPath, html);
  console.log(`📄 Reporte ULTRA generado: ${reportHtmlPath}`);
}

function run() {
  console.log("==============================================");
  console.log("   🛡️ ARES‑11 — VALIDACIÓN ULTRA");
  console.log("==============================================");

  validateCamelCase();
  analyzeJsMetrics();
  const graph = validateImportsAndBuildGraph();
  validateJSON();
  detectCycles(graph);
  detectGodFiles();
  generateMermaidGraph(graph);
  generateRadarArtifacts();
  generateHTMLReport();

  console.log("\n==============================================");

  if (totalErrors === 0) {
    console.log("✅ TODO CORRECTO — Proyecto íntegro, coherente y listo para producción.");
  } else {
    console.log(`⚠️ VALIDACIÓN COMPLETADA CON ${totalErrors} ERRORES.`);
  }

  console.log("==============================================\n");
}

run();
