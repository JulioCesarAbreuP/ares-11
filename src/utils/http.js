
// ────────────────────────────────────────────────────────────────────────────────
//  ARES-11 — Cliente HTTP
//  Arquitectura: Adaptador para peticiones HTTP (fetch)
//  Extensible: Añadir métodos (post, put, etc.) según necesidades
// ────────────────────────────────────────────────────────────────────────────────
import fetch from "node-fetch";

/**
 * Cliente HTTP para peticiones externas
 * @namespace http
 * @property {Function} get - Realiza petición GET y parsea JSON
 */
export const http = {
  /**
   * Realiza una petición GET y retorna JSON
   * @param {string} url - URL destino
   * @returns {Promise<object>} Respuesta JSON
   */
  get: async (url) => {
    const res = await fetch(url);
    return res.json();
  }
};
