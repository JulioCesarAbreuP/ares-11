/**
 * ARES—11 — PRO ARCHITECTURE VALIDATOR
 * Nivel: Staff/Lead Architect
 *
 * Validador PRO:
 *  - Estructura, camelCase, imports, archivos huérfanos, JSON, rutas, ciclos, dependencias, árbol visual, reporte HTML, badge
 *
 * Uso:
 *   node src/utils/validateProjectPRO.js
 *
 * Extensible: Añadir nuevas reglas y métricas en funciones auxiliares.
 */

import { validateObservability } from "./validateObservability.js";

/**
 * Ejecuta la validación IRP—03 de observabilidad y muestra el resultado.
 * @function
 */
export function runIRP03() {
  const projectRoot = process.cwd();
  const result = validateObservability(projectRoot);

  console.log("\n=== IRP—03 Observability ===");
  console.log(`Score: ${result.score}/${result.total}`);
  console.log(`Coverage: ${result.percentage}%\n`);

  result.results.forEach(r => {
    console.log(
      `${r.status === "OK" ? "✔" : "❌"}  ${r.check}  (${r.file})`
    );
  });

  console.log("\n============================\n");
}

runIRP03();
