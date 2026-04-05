
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Terminal Táctico de Telemetría
//  Arquitectura: Buffer persistente y renderizador de eventos recientes
//  Extensible: Permite integración con nuevos paneles y fuentes de eventos
// ────────────────────────────────────────────────────────────────────────────────
let buffer = [];

/**
 * Renderiza el terminal táctico con los eventos más recientes
 * @param {Array} events - Lista de eventos (opcional)
 */
export function renderTerminal(events = []) {
  const el = document.getElementById("tactical-terminal");
  if (!el) return;
  const list = events && events.length ? events : buffer;
  if (!Array.isArray(list) || list.length === 0) {
    el.innerHTML = "<em>No events yet. Waiting for telemetry...</em>";
    return;
  }
  el.innerHTML = list
    .slice(-50)
    .map(
      e => `
      <div class="tt-event tt-${(e.status || e.type || "info").toLowerCase()}">
        <span class="tt-ts">${e.timestamp || ""}</span>
        <span class="tt-type">${e.type || e.status || ""}</span>
        <span class="tt-msg">${e.stage ? `[${e.stage}]` : ""} ${e.message || ""}${e.durationMs ? ` (${e.durationMs}ms)` : ""}${e.error ? ` ⚠️ ${e.error}` : ""}</span>
      </div>
    `
    )
    .join("");
}

/**
 * Agrega un evento al buffer y actualiza el terminal táctico
 * @param {object} event - Evento de telemetría
 */
export function pushTerminalEvent(event) {
  buffer.push(event);
  renderTerminal();
}

/**
 * Permite suscribirse a eventos de telemetría y mostrarlos en tiempo real
 * @param {Function} subscribeFn - función subscribe del bus de telemetría
 */
export function subscribeTerminalToTelemetry(subscribeFn) {
  return subscribeFn(ev => {
    pushTerminalEvent(ev);
  });
}
  
