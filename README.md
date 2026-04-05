
## 🛰️ Propósito
ARES‑11 es un motor de auditoría táctica diseñado para transformar cualquier red en un mapa de riesgo basado en:

No es un escáner. Es un **motor de razonamiento de seguridad**.


## 🧩 Arquitectura (SABSA‑aligned)
ARES‑11 se compone de siete módulos:

1. **Fingerprinting Engine** — Descubrimiento determinista  
2. **CIS Auditor** — Validación IG1/IG2/IG3  
3. **TAXII Client** — Inteligencia viva  
4. **Threat Mapper** — Correlación MITRE ↔ CIS ↔ NIST  
5. **Risk Engine** — Cálculo de riesgo real  
6. **Remediation Engine** — Sugerencias técnicas  
7. **Tactical Dashboard** — Visualización D3.js  


# ARES-11
ARES-11 permite a equipos de seguridad automatizar auditorías, integrar inteligencia, correlacionar amenazas y generar evidencia técnica verificable, alineada con estándares internacionales (CIS, MITRE ATT&CK, NIST CSF).

## Arquitectura general
Orchestrator central endurecido, pipeline configurable y validable, módulos core desacoplados y telemetría avanzada. Todo el sistema está orientado a la observabilidad, la trazabilidad y la defensa en profundidad.

### Diagrama textual del pipeline

```
[Entrada] → [Orchestrator] → [Pipeline]
	├─► [CIS Auditor]
	├─► [KEV]
	├─► [Remediation]
	├─► [Risk Engine]
	├─► [Threat Mapper]
	├─► [Taxii Client]
	└─► [Telemetría]
		↓
	[Reportes] → [UI/Dashboards]
```

## Instrucciones de instalación y uso

Requisitos: Node.js >= 18, npm >= 9

```bash
git clone https://github.com/JulioCesarAbreuP/ares-11.git
cd ares-11
npm install
npm start
```

## Casos de uso
- Auditoría automatizada de controles CIS
### Documentación Doctrinal (API)

La documentación doctrinal de ARES‑11 describe en detalle cada módulo, herramienta y componente del motor de razonamiento de seguridad, alineando la operación con estándares internacionales y mejores prácticas empresariales.

- [Acceso al índice doctrinal de la API](docs/API/index.md)
- [Paneles UI avanzados](docs/API/ui-panels.md)

Esta sección permite navegar la arquitectura, los módulos y la interfaz empresarial de ARES‑11, facilitando la auditoría basada en evidencia y la toma de decisiones táctica.
- Correlación de amenazas con MITRE ATT&CK
- Generación de planes NIST CSF y evidencia técnica
- Integración de inteligencia vía TAXII/STIX
- Visualización de riesgos y remediación

## Buenas prácticas
- Modularizar nuevas funcionalidades y documentar cada módulo
- Usar logs estructurados, métricas y eventos normalizados
- Versionar configuraciones, reglas y esquemas
- Revisar y actualizar dashboards y documentación periódicamente
- Validar la cobertura y calidad mediante pruebas, auditoría y telemetría avanzada

## Advertencias técnicas
- Respetar interfaces, contratos y modularidad estricta
- Validar entradas, salidas y evidencia técnica
- No acoplar lógica de negocio al orchestrator
- Mantener trazabilidad, telemetría y observabilidad avanzada de extremo a extremo

## Roadmap público
- Integración avanzada y validación de fuentes TAXII/STIX
- Motor de remediación automatizada y trazable
- Dashboards personalizables y exportables
- Soporte para ejecución distribuida y escalabilidad horizontal
- API REST y CLI para integración externa
- Certificación de evidencias y auditoría forense
- Módulo de correlación avanzada MITRE/NIST
- Generación automática de reportes y planes NIST CSF
- Integración de autenticación y control de acceso basado en roles
- Pruebas automatizadas de extremo a extremo y cobertura de seguridad
- Telemetría avanzada y exportación a sistemas SIEM

## Glosario técnico consolidado
- **Orchestrator**: Componente central de control, integración y coordinación de flujos y módulos, con gestión de errores y dependencias.
- **Pipeline**: Secuencia configurable y validable de etapas de análisis, enriquecimiento y reporte, con puntos de control y rollback.
- **CIS**: Center for Internet Security, estándar de controles de ciberseguridad.
- **KEV**: Known Exploited Vulnerabilities, catálogo de vulnerabilidades explotadas activamente.
- **TAXII**: Trusted Automated eXchange of Indicator Information, protocolo de intercambio de inteligencia.
- **STIX**: Structured Threat Information Expression, estándar de modelado de inteligencia.
- **MITRE ATT&CK**: Marco de referencia para tácticas y técnicas de adversarios.
- **NIST CSF**: Cybersecurity Framework, marco de referencia para gestión de riesgos.
- **Remediation**: Proceso de corrección y mitigación de riesgos y vulnerabilidades, con trazabilidad y auditoría.
- **Telemetría**: Registro estructurado de métricas, logs, eventos y evidencia técnica, con exportación y defensa en profundidad.
- **Evidencia técnica**: Artefactos verificables generados por el sistema para auditoría y certificación.
- **Contrato explícito**: Definición formal y documentada de las interfaces, entradas y salidas de cada módulo, versionada y auditable.

## Filosofía y estructura editorial
ARES-11 prioriza la modularidad, la transparencia, la trazabilidad, la defensa en profundidad y la extensibilidad. La documentación es clara, progresiva, orientada a la certificación, la auditoría y la transferencia de conocimiento. El sistema está diseñado para evolucionar, adaptarse y cumplir con los más altos estándares de calidad, seguridad y observabilidad avanzada.
