# Módulos de ARES‑11

## Lista de módulos
1. Fingerprinting Engine
2. CIS Auditor
3. TAXII Client
4. Threat Mapper
5. Risk Engine
6. Remediation Engine
7. Tactical Dashboard

## Descripción técnica
- **Fingerprinting Engine**: Descubrimiento determinista de activos y superficies.
- **CIS Auditor**: Validación de controles CIS IG1/IG2/IG3 y generación de evidencia.
- **TAXII Client**: Ingesta y procesamiento de inteligencia viva.
- **Threat Mapper**: Correlación MITRE ↔ CIS ↔ NIST y priorización táctica.
- **Risk Engine**: Cálculo de riesgo real y ponderado.
- **Remediation Engine**: Sugerencias técnicas y priorización de acciones.
- **Tactical Dashboard**: Visualización táctica y mapa de riesgo.

## Flujo entre módulos
1. Fingerprinting → 2. CIS Auditor → 3. TAXII Client → 4. Threat Mapper → 5. Risk Engine → 6. Remediation Engine → 7. Tactical Dashboard

## Dependencias internas
- Todos los módulos reportan al orchestrator y comparten telemetría.
- El pipeline es configurable y desacoplado.
