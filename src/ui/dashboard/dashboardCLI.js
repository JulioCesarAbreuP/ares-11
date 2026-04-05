import { telemetryBus } from "../../utils/telemetryBus.js";

console.log("🖥️ Dashboard ARES‑11 iniciado...\n");

telemetryBus.on("metric", (m) => {
  console.log("📊 Métrica:", m.type);
  console.log("   Valor:", m.value);
  console.log("   Timestamp:", m.timestamp);
  console.log("-------------------------------");
});
