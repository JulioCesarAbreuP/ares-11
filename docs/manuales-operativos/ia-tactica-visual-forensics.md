# 1. IA Táctica / Visual Forensics

## 2. Propósito Operativo
Integrar IA local (Ollama + Python) para análisis ofensivo/defensivo, predicción de rutas de ataque, generación de vacunas y análisis OCR de evidencia visual.

## 3. Procedimientos Operativos Estándar (SOP)
- Ejecutar `ia_tactical.py` para análisis de escaneos y generación de vacunas.
- Ejecutar `visual_forensics.py` para captura y análisis OCR de evidencia visual.
- Ejecutar `visual_forensics_automator.py` para integración y remediación automática.
- Validar logs y acciones generadas.
- Buenas prácticas: Mantener modelos IA y scripts actualizados.

## 4. Flujo Operativo
- Entradas: JSON de escaneo, imágenes, comandos de remediación.
- Procesamiento: Análisis IA, OCR, generación de scripts, recomendación de acciones.
- Salidas: Vacunas, logs, hallazgos visuales, acciones automáticas.
- Integración: Dashboard, Remediation, Forense, Compliance.
- Dependencias: Ollama, pytesseract, PowerShell.

## 5. KPIs y Señales Clave
- Vacunas generadas
- Hallazgos visuales
- Acciones automáticas
- Umbral: 100% hallazgos procesados

## 6. Integración con el Dashboard Táctico
- Visualiza hallazgos IA, evidencia visual y acciones tomadas.
- Estado: Activo, Degradado, Crítico.
- Métricas: Hallazgos, acciones, integridad.

## 7. Integración con el Orquestador
- Genera señales de hallazgo y remediación.
- Reglas YAML ejemplo:
```yaml
rule:
  name: "Vacuna automática por hallazgo visual"
  condition: "ia_visual.hallazgo == 'high_risk'"
  action: "remediation.block(ia_visual.host)"
  severity: "critical"
  recommendation: "Validar aislamiento y revisar logs"
```

## 8. Escenarios Operativos
- Estado normal: IA procesando hallazgos.
- Estado degradado: Sin señales IA, alerta generada.
- Señal de riesgo: Hallazgo crítico, acción ejecutada.
- Recomendación: Escalar si IA no responde.

## 9. Relación con Estándares
- CIS 16, NIST SI-4, MITRE ATT&CK (defensivo: T1059), SABSA Logical Security Layer.

## 10. Resumen Ejecutivo Operativo
La IA Táctica y Visual Forensics dota a ARES‑11 de capacidades cognitivas y forenses avanzadas, acelerando la respuesta y la documentación de incidentes.

## 11. Enlace al Index Maestro
[Volver al índice maestro](index.md)
