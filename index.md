# ARES‑11: Motor de Razonamiento de Seguridad

---

## 🛰️ Propósito
ARES‑11 es un motor de auditoría táctica diseñado para transformar cualquier red en un mapa de riesgo basado en evidencia.

> “No es un escáner. Es un motor de razonamiento de seguridad.”

---

## 🧩 Arquitectura (SABSA‑aligned)
ARES‑11 se compone de módulos empresariales y tácticos:

1. **Fingerprinting Engine** — Descubrimiento determinista
2. **CIS Auditor** — Validación IG1/IG2/IG3
3. **TAXII Client** — Inteligencia viva
4. **Threat Mapper** — Correlación MITRE ↔ CIS ↔ NIST
5. **Risk Engine** — Cálculo de riesgo real
6. **Remediation Engine** — Sugerencias técnicas
7. **Tactical Dashboard** — Visualización D3.js
8. **Quick Triage** — Priorización táctica
9. **Exporter** — Exportación de hallazgos
10. **Notifier** — Notificaciones críticas
11. **Live Monitor** — Monitoreo en tiempo real
12. **Remediation Script Generator** — Scripts personalizados
13. **Whitelist** — Gestión de dispositivos confiables
14. **Shodan Check** — Verificación de exposición pública
15. **Forensics Packager** — Preservación de evidencia

---

## Filosofía y Mensaje Doctrinal
ARES‑11 prioriza la trazabilidad, la defensa en profundidad y la gobernanza sobre cada función del motor. Está alineado con SABSA, CIS Controls, NIST 800‑53 y MITRE ATT&CK (defensivo).

> “No es un escáner. Es un motor de razonamiento de seguridad.”

---

## Menú Empresarial (Hamburguesa)

- **Inicio**
- **Arquitectura**
- **Módulos**
- **Dashboard táctico**
- **Documentación doctrinal**
- **Interfaz (UI)**
	- CIS Auditor
	- TAXII Client
	- Risk Engine
	- Remediation Engine
	- Tactical Dashboard
	- Quick Triage
	- Exporter
	- Notifier
	- Live Monitor
	- Remediation Script Generator
	- Whitelist
	- Shodan Check
	- Forensics Packager

---


## Manuales Operativos y AI Assistant
Accede a la colección completa de manuales operativos, flujos doctrinales y la integración del AI Assistant:
- [Índice Maestro de Manuales Operativos](docs/manuales-operativos/index.md)
- [Manual AI Assistant (IA Local/Online)](docs/manuales-operativos/ai-assistant.md)
- [Integración doctrinal del AI Assistant](docs/manuales-operativos/integracion-ai-assistant.md)

Los manuales cubren cada módulo, flujo y panel de ARES‑11, con ejemplos, diagramas y requisitos. El AI Assistant está documentado y enlazado para consulta rápida.

---

## Interfaz Empresarial (UI)
Accede a la interfaz visual y navega todas las herramientas desde:
- [Interfaz Empresarial de ARES‑11 (UI)](docs/API/UI/index.md)

La UI permite visualizar, gestionar y navegar todos los módulos, paneles y componentes alineados a la doctrina y arquitectura táctica de la plataforma.

---

## Documentación Doctrinal (API)
Accede a la documentación doctrinal y técnica de todos los módulos, herramientas y paneles de ARES‑11:
- [Índice doctrinal de la API](docs/API/index.md)

La documentación proporciona transparencia, trazabilidad y gobernanza sobre cada función del motor, permitiendo comprender el ciclo completo de auditoría basada en evidencia.

---

## Instalación y Uso

Requisitos: Node.js >= 18, npm >= 9

```bash
git clone https://github.com/JulioCesarAbreuP/ares-11.git
cd ares-11
npm install
npm start
```

---

## Casos de Uso
- Auditoría automatizada de controles CIS
- Correlación de amenazas con MITRE ATT&CK
- Generación de planes NIST CSF y evidencia técnica
- Integración de inteligencia vía TAXII/STIX
- Visualización de riesgos y remediación

---

## Buenas Prácticas
- Modularizar nuevas funcionalidades y documentar cada módulo
- Usar logs estructurados, métricas y eventos normalizados
- Versionar configuraciones, reglas y esquemas
- Revisar y actualizar dashboards y documentación periódicamente
- Validar la cobertura y calidad mediante pruebas, auditoría y telemetría avanzada

---

## Advertencias Técnicas
- Respetar interfaces, contratos y modularidad estricta
- Validar entradas, salidas y evidencia técnica
- No acoplar lógica de negocio al orchestrator
- Mantener trazabilidad, telemetría y observabilidad avanzada de extremo a extremo

---

> “No es un escáner. Es un motor de razonamiento de seguridad.”
