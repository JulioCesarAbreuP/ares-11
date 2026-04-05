/**
 * ARES—11 — Extended Project Integrity Validator
 * Nivel: Staff/Lead Architect
 *
 * Validador extendido:
 *  - Estructura, camelCase, imports, archivos huérfanos, JSON, rutas, reporte HTML, badge
 *
 * Uso:
 *   node src/utils/validateProjectExtended.js
 *
 * Extensible: Añadir nuevas reglas y métricas en funciones auxiliares.
 */

import fs from "fs";
import path from "path";

const root = path.resolve("src");
const reportPath = path.resolve("validation-report.html");

const expectedStructure = {
  "core/fingerprint": ["fingerprint.go"],
  "core/taxii-client": ["taxiiClient.js", "parser.js"],
  "core/threat-mapper": ["threat-mapper.js"],
  "orchestrator": ["pipeline.js"],
  "ui/dashboard": [
    "index.html",
    "mitreHeatmap.js",
    "renderNistPanel.js",
    "loadDashboardData.js",
    "dashboard-mitre.json",
    "dashboard-nist.json",
    "sample-technique.json"
  ],
  "ui/styles": ["dashboard-theme.css", "nist-panel.css"]
};

const camelCaseRegex = /^[a-z][A-Za-z0-9]*\.(js|json|css|go|html)$/;

let report = [];
let totalErrors = 0;

/**
 * Log auxiliar para reporte HTML
 * @param {string} msg
 */
function log(msg) {
  console.log(msg);
  report.push(`<p>${msg}</p>`);
}

/**
 * Marca error en el reporte
 * @param {string} msg
 */
function error(msg) {
  console.log(`❌ ${msg}`);
  report.push(`<p style="color:red">❌ ${msg}</p>`);
  totalErrors++;
}

/**
 * Marca OK en el reporte
 * @param {string} msg
 */
function ok(msg) {
  console.log(`✔️ ${msg}`);
  report.push(`<p style="color:green">✔️ ${msg}</p>`);
}

/**
 * Valida estructura esperada
 */
function validateStructure() {
  log("<h2>Validación de estructura</h2>");

  for (const folder in expectedStructure) {
    const files = expectedStructure[folder];

    files.forEach(file => {
      const fullPath = path.join(root, folder, file);
      if (!fs.existsSync(fullPath)) {
        error(`Falta archivo: ${folder}/${file}`);
      } else {
        ok(`Existe: ${folder}/${file}`);
      }
    });
  }
}

/**
 * Valida convención camelCase en archivos
 */
function validateCamelCase() {
  log("<h2>Validación camelCase</h2>");

  for (const folder in expectedStructure) {
    expectedStructure[folder].forEach(file => {
      if (!camelCaseRegex.test(file)) {
        error(`No camelCase: ${folder}/${file}`);
      } else {
        ok(`camelCase OK: ${folder}/${file}`);
      }
    });
  }
}

function getAllJsFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);

  list.forEach(file => {
    const full = path.join(dir, file);
    const stat = fs.statSync(full);

    if (stat.isDirectory()) {
      results = results.concat(getAllJsFiles(full));
    } else if (file.endsWith(".js")) {
      results.push(full);
    }
  });

  return results;
}

function validateImports() {
  log("<h2>Validación de imports</h2>");

  const jsFiles = getAllJsFiles(root);

  jsFiles.forEach(file => {
    const content = fs.readFileSync(file, "utf8");
    const importRegex = /import\s+.*?from\s+["'](.+?)["']/g;

    let match;
    while ((match = importRegex.exec(content)) !== null) {
      const importPath = match[1];

      if (importPath.startsWith(".")) {
        const resolved = path.resolve(path.dirname(file), importPath);

        if (!fs.existsSync(resolved) && !fs.existsSync(resolved + ".js") && !fs.existsSync(resolved + ".json")) {
          error(`Import roto en ${file}: ${importPath}`);
        } else {
          ok(`Import OK en ${file}: ${importPath}`);
        }
      }
    }
  });
}

function validateJSON() {
  log("<h2>Validación de JSON</h2>");

  const jsonFiles = [
    "ui/dashboard/dashboard-mitre.json",
    "ui/dashboard/dashboard-nist.json"
  ];

  jsonFiles.forEach(file => {
    const full = path.join(root, file);

    if (!fs.existsSync(full)) {
      error(`Falta JSON: ${file}`);
      return;
    }

    try {
      JSON.parse(fs.readFileSync(full, "utf8"));
      ok(`JSON válido: ${file}`);
    } catch {
      error(`JSON corrupto: ${file}`);
    }
  });
}

function detectOrphans() {
  log("<h2>Detección de archivos huérfanos</h2>");

  const expectedFiles = new Set();

  for (const folder in expectedStructure) {
    expectedStructure[folder].forEach(file => {
      expectedFiles.add(path.join(root, folder, file));
    });
  }

  const allFiles = getAllJsFiles(root).concat(
    fs.readdirSync(path.join(root, "ui/styles")).map(f => path.join(root, "ui/styles", f))
  );

  allFiles.forEach(file => {
    if (!expectedFiles.has(file)) {
      error(`Archivo huérfano: ${file.replace(root + "/", "")}`);
    }
  });
}

function generateHTMLReport() {
  const badge = totalErrors === 0
    ? `<div style="background:#2ea043;color:white;padding:10px;border-radius:6px;width:120px;text-align:center">STATUS: OK</div>`
    : `<div style="background:#ff3e3e;color:white;padding:10px;border-radius:6px;width:120px;text-align:center">STATUS: FAIL</div>`;

  const html = `
  <html>
  <head>
    <title>ARES‑11 Validation Report</title>
    <style>
      body { font-family: Arial; padding: 20px; background: #111; color: #ddd; }
      h1, h2 { color: #fff; }
      p { margin: 4px 0; }
    </style>
  </head>
  <body>
    <h1>ARES‑11 — Validation Report</h1>
    ${badge}
    ${report.join("\n")}
  </body>
  </html>
  `;

  fs.writeFileSync(reportPath, html);
  console.log(`\n📄 Reporte generado: ${reportPath}`);
}

function run() {
  console.log("==============================================");
  console.log("   🛡️ ARES‑11 — VALIDACIÓN EXTENDIDA");
  console.log("==============================================");

  validateStructure();
  validateCamelCase();
  validateImports();
  validateJSON();
  detectOrphans();
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
