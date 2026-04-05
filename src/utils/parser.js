
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Parser de Inteligencia (STIX → Modelo Interno)
//  Arquitectura: Adaptador para normalizar objetos STIX a modelo propio
//  Extensible: Añadir nuevos normalizadores según fuentes de inteligencia
// ────────────────────────────────────────────────────────────────────────────────

/**
 * Parser de objetos STIX a modelo interno ARES-11
 * @namespace parser
 * @property {Function} normalizeSTIX - Normaliza un objeto STIX
 */
export const parser = {
  /**
   * Normaliza un objeto STIX a formato interno
   * @param {object} obj - Objeto STIX
   * @returns {object} Objeto normalizado
   */
  normalizeSTIX: (obj) => ({
    id: obj.id,
    type: obj.type,
    name: obj.name,
    external_id: obj.external_references?.[0]?.external_id || null
  })
};
