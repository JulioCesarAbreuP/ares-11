import fetch from "node-fetch";
import { parser } from "../../utils/parser.js";
import { logger } from "../../utils/logger.js";

export const TaxiiClient = {
  /**
   * Descarga objetos STIX desde una colección TAXII
   */
  async fetchCollection(collectionUrl) {
    logger.info(`Descargando STIX desde: ${collectionUrl}`);
    try {
      const res = await fetch(collectionUrl);
      if (!res.ok) {
        logger.error(`Error HTTP ${res.status} al consultar TAXII`);
        return [];
      }
      const data = await res.json();
      if (!data.objects || !Array.isArray(data.objects)) {
        logger.warn("[TAXII] Respuesta sin objetos válidos.");
        return [];
      }
      return data.objects
        .filter(o => o && o.type === "attack-pattern")
        .map(parser.normalizeSTIX);
    } catch (err) {
      logger.error("Error en TAXII fetch: " + (err?.message || err));
      return [];
    }
  },

  /**
   * Sincroniza técnicas MITRE ATT&CK desde la colección Enterprise
   */
  async sync() {
    const enterpriseCollection =
      "https://cti-taxii.mitre.org/stix/collections/95ecc380-afe9-11e4-9b6c-751b87207931/objects/";
    logger.info("Iniciando sincronización TAXII (MITRE ATT&CK Enterprise)...");
    const techniques = await this.fetchCollection(enterpriseCollection);
    if (!Array.isArray(techniques) || techniques.length === 0) {
      logger.warn("[TAXII] No se descargaron técnicas MITRE.");
    } else {
      logger.info(`Técnicas MITRE descargadas: ${techniques.length}`);
    }
    return techniques;
  }
};
