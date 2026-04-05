# 1. Sniffers / Forense Defensivo

## 2. Propósito Operativo
Capturar, analizar y reportar evidencia de tráfico, fingerprints y anomalías en la red, integrando análisis forense y detección de amenazas avanzadas.

## 3. Procedimientos Operativos Estándar (SOP)
- Ejecutar `forensic_eye.py` para captura pasiva.
- Ejecutar `forensic_analyst.py` para análisis y remediación.
- Generar reporte con `generate_forensic_report.py`.
- Validar logs y evidencia generada.
- Buenas prácticas: Mantener sensores y scripts actualizados.

## 4. Flujo Operativo
- Entradas: Paquetes, fingerprints, logs de red.
- Procesamiento: Análisis, detección de beaconing, exfiltración, spoofing.
- Salidas: Evidencia, alertas, vacunas automáticas.
- Integración: Dashboard, Compliance, Remediation.
- Dependencias: Scapy, pandas, permisos de red.

## 5. KPIs y Señales Clave
- Evidencias capturadas
- Alertas generadas
- Vacunas ejecutadas
- Umbral: 0 falsos negativos

## 6. Integración con el Dashboard Táctico
- Visualiza alertas forenses, evidencia y acciones tomadas.
- Estado: Activo, Degradado, Crítico.
- Métricas: Evidencia, alertas, integridad.

## 7. Integración con el Orquestador
- Genera señales de hallazgo y remediación.
- Reglas YAML ejemplo:
```yaml
rule:
  name: "Vacuna automática por MAC spoofing"
  condition: "forense.alert == 'mac_spoofing'"
  action: "remediation.isolate(forense.host)"
  severity: "critical"
  recommendation: "Validar aislamiento y revisar logs"
```

## 8. Escenarios Operativos
- Estado normal: Captura pasiva sin alertas.
- Estado degradado: Sensor sin datos, alerta generada.
- Señal de riesgo: MAC spoofing detectado, vacuna ejecutada.
- Recomendación: Escalar a forense avanzado.

## 9. Relación con Estándares
- CIS 6, NIST SI-4, MITRE ATT&CK (defensivo: T1592), SABSA Service Layer.

## 10. Resumen Ejecutivo Operativo
Sniffers y Forense Defensivo elevan la visibilidad y capacidad de respuesta ante amenazas avanzadas en la red.

## 11. Enlace al Index Maestro
[Volver al índice maestro](index.md)
