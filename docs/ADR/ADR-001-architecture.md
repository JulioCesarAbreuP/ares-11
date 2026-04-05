# ADR‑001 — Arquitectura General de ARES‑11

## 1. Contexto
ARES‑11 debe operar como un Tactical Security Probe capaz de:
- Auditar redes IG1–IG3
- Correlacionar hallazgos con MITRE ATT&CK
- Generar planes NIST CSF
- Producir evidencia técnica verificable

---

## 2. Decisión
Se adopta una arquitectura modular basada en siete motores independientes:

1. **Fingerprinting Engine**
2. **CIS Auditor**
3. **TAXII Intelligence Client**
4. **Threat Correlation Engine**
5. **Risk Engine**
6. **Remediation Engine**
7. **Tactical Dashboard**

Cada módulo es autónomo, testeable y extensible.

---

## 3. Justificación
- CIS v8 requiere separación clara entre descubrimiento y auditoría.  
- MITRE ATT&CK exige normalización STIX 2.1.  
- NIST CSF requiere trazabilidad entre hallazgos y acciones.  
- La modularidad permite reemplazar motores sin afectar el resto.

---

## 4. Consecuencias
### Positivas
- Extensibilidad total  
- Testing granular  
- Integración con pipelines CI/CD  
- Escalabilidad horizontal  

### Negativas
- Mayor número de módulos  
- Necesidad de documentación estricta  

---

## 5. Estado
**Aprobado** — Versión inicial del proyecto.
