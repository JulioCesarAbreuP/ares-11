# ADR‑002 — Threat Mapper Engine

## 1. Contexto
ARES‑11 necesita un motor capaz de correlacionar:
- Activos descubiertos por el Fingerprinting Engine  
- Hallazgos de configuración del CIS Auditor  
- Técnicas MITRE ATT&CK obtenidas vía TAXII  
- Controles NIST CSF aplicables  

El objetivo es producir un **mapa de riesgo real**, priorizado y accionable, que represente cómo un atacante podría encadenar técnicas para comprometer la red.

---

## 2. Decisión
Se implementará un **Threat Mapper Engine** basado en:

### 🔹 2.1 Modelo de Grafo Interno
Cada entidad se representa como un nodo:
- `Asset`
- `Vulnerability`
- `CIS_Control`
- `MITRE_Technique`
- `NIST_Function`

Las relaciones representan:
- Exposición  
- Dependencia  
- Correlación  
- Rutas de ataque  

### 🔹 2.2 Normalización STIX 2.1
Todas las técnicas MITRE se normalizan a un modelo interno:
- `id`
- `external_id` (Txxxx)
- `name`
- `kill_chain_phase`
- `mitigation_ref`

### 🔹 2.3 Correlación Determinista
El motor cruza:
- Vulnerabilidades ↔ Técnicas MITRE  
- Técnicas MITRE ↔ Controles CIS  
- Controles CIS ↔ Funciones NIST  

### 🔹 2.4 Cálculo de Riesgo
Se adopta un modelo determinista:



\[
Risk = Exposure \cdot ThreatPressure \cdot Impact
\]



Donde:
- **Exposure** = severidad del hallazgo CIS  
- **ThreatPressure** = frecuencia de explotación (MITRE + CISA KEV)  
- **Impact** = función NIST asociada (ID/PR/DE/RS/RC)  

---

## 3. Justificación
- MITRE ATT&CK requiere correlación contextual, no listas planas.  
- CIS v8 exige trazabilidad entre controles y técnicas.  
- NIST CSF requiere priorización basada en impacto.  
- El modelo de grafo permite detectar **cadenas de ataque completas**, no solo hallazgos aislados.  

---

## 4. Consecuencias

### ✔ Positivas
- Correlación precisa y explicable  
- Priorización basada en evidencia  
- Extensibilidad modular  
- Capacidad de detectar rutas de ataque reales  

### ✖ Negativas
- Complejidad mayor  
- Requiere normalización estricta  
- Necesita caching para rendimiento  

---

## 5. Estado
**Aprobado** — Implementación inicial en progreso.
