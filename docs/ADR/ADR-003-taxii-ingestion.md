# ADR‑003 — TAXII Ingestion Engine

## 1. Contexto
ARES‑11 requiere inteligencia de amenazas **viva**, no estática.  
Para ello debe consumir datos desde:

- MITRE ATT&CK (Enterprise, Mobile, ICS)
- CISA Known Exploited Vulnerabilities (KEV)
- Cualquier servidor TAXII 2.1 compatible

La inteligencia debe ser:
- Normalizada (STIX 2.1)
- Cacheada localmente
- Correlacionable con activos y hallazgos CIS
- Actualizable en tiempo real

---

## 2. Decisión
Se implementará un **TAXII Ingestion Engine** con las siguientes características:

### 🔹 2.1 Cliente TAXII 2.1
El motor debe:
- Autenticarse si es necesario
- Descubrir endpoints TAXII
- Listar colecciones disponibles
- Descargar objetos STIX (attack-pattern, malware, tool, intrusion-set)

### 🔹 2.2 Normalización STIX 2.1
Cada objeto STIX se transforma a un modelo interno:

```json
{
	"id": "stix-id",
	"external_id": "Txxxx",
	"name": "Technique Name",
	"description": "...",
	"kill_chain": "phase",
	"mitigation_ref": "CIS/NIST mapping"
}
```

### 🔹 2.3 Cache Local
Para evitar saturar el servidor TAXII:
- Se implementa un cache JSON local
- Se actualiza solo si hay cambios (ETag / Last-Modified)
- Se permite operación offline

### 🔹 2.4 Manejo de Errores Robusto
El motor debe:
- Reintentar conexiones
- Detectar timeouts
- Registrar fallos en el logger central
- Continuar operación con datos cacheados

---

## 3. Justificación
- TAXII es el estándar oficial para intercambio de inteligencia estructurada.
- MITRE ATT&CK se actualiza constantemente; no usar TAXII implica quedarse obsoleto.
- CISA KEV es crítico para priorizar vulnerabilidades explotadas activamente.
- La correlación con CIS y NIST depende de IDs externos (Txxxx).

---

## 4. Consecuencias

### ✔ Positivas
- Inteligencia siempre actualizada  
- Reducción de falsos positivos  
- Priorización basada en amenazas reales  
- Integración directa con MITRE ATT&CK  

### ✖ Negativas
- Dependencia de red  
- Necesidad de caching y control de versiones  
- Complejidad en parsing STIX  

---

## 5. Estado
**Aprobado** — Cliente inicial implementado en Node.js.
