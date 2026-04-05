# 1. Compliance Engine

## 2. Propósito Operativo
Automatizar la auditoría, recolección de evidencia y generación de reportes alineados a estándares CIS, NIST y MITRE.

## 3. Procedimientos Operativos Estándar (SOP)
- Ejecutar auditoría con `Audit()`.
- Validar reportes generados y cobertura de controles.
- Revisar hallazgos y evidencias.
- Ante anomalías, reauditar y revisar configuración.
- Buenas prácticas: Mantener controles y mapeos actualizados.

## 4. Flujo Operativo
- Entradas: Evidencia, señales de agentes, comandos de auditoría.
- Procesamiento: Validación, mapeo a controles, generación de reportes.
- Salidas: Reportes, hallazgos, alertas de cumplimiento.
- Integración: Core, Agentes, Dashboard, Remediation.
- Dependencias: Configuración, estándares, canal seguro.

## 5. KPIs y Señales Clave
- Controles cubiertos
- Evidencias recolectadas
- Hallazgos críticos
- Alertas de incumplimiento
- Umbral: 100% controles cubiertos

## 6. Integración con el Dashboard Táctico
- Visualiza estado de cumplimiento, hallazgos y evidencias.
- Estado: Cumplido, Parcial, Incumplido.
- Métricas: Cobertura, hallazgos, alertas.

## 7. Integración con el Orquestador
- Genera señales de cumplimiento y hallazgos.
- Reglas YAML ejemplo:
```yaml
rule:
  name: "Alerta de incumplimiento"
  condition: "compliance.status == 'Incumplido'"
  action: "dashboard.notify(compliance)"
  severity: "critical"
  recommendation: "Revisar controles y evidencias"
```

## 8. Escenarios Operativos
- Estado normal: Cumplimiento total.
- Estado degradado: Controles parciales.
- Señal de riesgo: Incumplimiento crítico.
- Recomendación: Escalar a auditoría externa.

## 9. Relación con Estándares
- CIS 4, NIST AU-6, MITRE ATT&CK (defensivo: T1589), SABSA Service Layer.

## 10. Resumen Ejecutivo Operativo
Compliance Engine automatiza la auditoría y reporting, fortaleciendo la postura de cumplimiento de ARES‑11.

## 11. Enlace al Index Maestro
[Volver al índice maestro](index.md)
