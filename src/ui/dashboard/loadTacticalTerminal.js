import { renderTerminal, pushTerminalEvent } from "./tacticalTerminal.js";

export function loadTacticalTerminal(events = []) {
  renderTerminal(events);
}

export function startTerminalStream() {
  const es = new EventSource("/api/telemetry-stream");
  es.onmessage = msg => {
    try {
      const event = JSON.parse(msg.data);
      pushTerminalEvent(event);
    } catch {}
  };
}

// Ejemplo de uso:
// loadTacticalTerminal([{timestamp: "2026-04-05 12:00", type: "INFO", message: "Terminal inicializado."}]);
