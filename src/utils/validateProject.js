/**
 * ARES—11 — Project Integrity Validator
 * Objetivo: Validar estructura, imports y coherencia camelCase del proyecto.
 *
 * Uso:
 *   node src/utils/validateProject.js
 *
 * Extensible: Añadir nuevas reglas y métricas en funciones auxiliares.
 */

import fs from "fs";
import path from "path";

const projectRoot = path.resolve("src");

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

/**
 * Verifica existencia de archivo
 * @param {string} base
 * @param {string} file
 * @returns {boolean}
 */
function checkFileExists(base, file) {
  const fullPath = path.join(projectRoot, base, file);
  return fs.existsSync(fullPath);
}

/**
 * Valida estructura esperada
 * @returns {number} Número de errores
 */
function validateStructure() {
  console.log("\n🔍 VALIDANDO ESTRUCTURA DEL PROYECTO...\n");

  let errors = 0;

  for (const folder in expectedStructure) {
    const files = expectedStructure[folder];

    files.forEach(file => {
      const exists = checkFileExists(folder, file);

      if (!exists) {
        console.log(`❌ FALTA: ${folder}/${file}`);
        errors++;
      } else {
        console.log(`✔️ OK: ${folder}/${file}`);
      }
    });
  }

  return errors;
}

/**
 * Valida convención camelCase en archivos
 * @returns {number} Número de errores
 */
function validateCamelCase() {
  console.log("\n🔍 VALIDANDO camelCase...\n");

  let errors = 0;

  for (const folder in expectedStructure) {
    const files = expectedStructure[folder];

    files.forEach(file => {
      if (!camelCaseRegex.test(file)) {
        console.log(`⚠️ NO camelCase: ${folder}/${file}`);
        errors++;
      } else {
        console.log(`✔️ camelCase OK: ${folder}/${file}`);
      }
    });
  }

  return errors;
}

function validateImports() {
  console.log("\n🔍 VALIDANDO IMPORTS...\n");

  const pipelinePath = path.join(projectRoot, "orchestrator/pipeline.js");
  const pipelineContent = fs.readFileSync(pipelinePath, "utf8");

  const importChecks = [
    {
      expected: "../core/taxii-client/taxiiClient.js",
      label: "TAXII Client"
    },
    {
      expected: "../core/threat-mapper/threat-mapper.js",
      label: "Threat Mapper"
    },
    {
      expected: "../utils/logger.js",
      label: "Logger"
    },
    {
      expected: "../config/paths.config.json",
      label: "Paths Config"
    }
  ];

  let errors = 0;

  importChecks.forEach(check => {
    if (pipelineContent.includes(check.expected)) {
      console.log(`✔️ Import OK (${check.label})`);
    } else {
      console.log(`❌ Import roto (${check.label}): falta ${check.expected}`);
      errors++;
    }
  });

  return errors;
}

function validateDashboardJSON() {
  console.log("\n🔍 VALIDANDO JSON DEL DASHBOARD...\n");

  const jsonFiles = [
    "ui/dashboard/dashboard-mitre.json",
    "ui/dashboard/dashboard-nist.json"
  ];

  let errors = 0;

  jsonFiles.forEach(file => {
    const fullPath = path.join(projectRoot, file);

    if (!fs.existsSync(fullPath)) {
      console.log(`❌ Falta JSON: ${file}`);
      errors++;
      return;
    }

    try {
      JSON.parse(fs.readFileSync(fullPath, "utf8"));
      console.log(`✔️ JSON válido: ${file}`);
    } catch {
      console.log(`❌ JSON corrupto: ${file}`);
      errors++;
    }
  });

  return errors;
}

function runValidation() {
  console.log("==============================================");
  console.log("   🛡️ ARES‑11 — VALIDACIÓN DE INTEGRIDAD");
  console.log("==============================================");

  let totalErrors = 0;

  totalErrors += validateStructure();
  totalErrors += validateCamelCase();
  totalErrors += validateImports();
  totalErrors += validateDashboardJSON();

  console.log("\n==============================================");

  if (totalErrors === 0) {
    console.log("✅ TODO CORRECTO — Proyecto íntegro, coherente y listo para producción.");
  } else {
    console.log(`⚠️ VALIDACIÓN COMPLETADA CON ${totalErrors} ERRORES.`);
    console.log("Revisa los puntos marcados arriba.");
  }

  console.log("==============================================\n");
}

runValidation();
