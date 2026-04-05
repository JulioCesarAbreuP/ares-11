# 1. Dashboard

## 2. Propósito Operativo
Visualizar en tiempo real el estado, KPIs, alertas, evidencia forense y acciones de todos los módulos de ARES‑11. Es el centro de mando táctico y ejecutivo.

## 3. Procedimientos Operativos Estándar (SOP)
- Acceder vía navegador o app.
- Validar que los paneles muestran datos actualizados.
- Revisar logs, alertas y evidencia visual.
- Ante anomalías, consultar logs y escalar a soporte.
- Buenas prácticas: Mantener paneles y fuentes de datos sincronizados.

## 4. Flujo Operativo
- Entradas: KPIs, alertas, logs, evidencia visual, señales de módulos.
- Procesamiento: Renderizado, actualización en tiempo real, correlación visual.
- Salidas: Visualización, notificaciones, exportación de reportes.
- Integración: Todos los módulos, especialmente Cognitive Engine, Forense, Remediation.
- Dependencias: API, fuentes de datos, permisos de usuario.

## 5. KPIs y Señales Clave
- Estado global de módulos
- Score de riesgo
- Acciones automáticas
- Evidencia forense visual
- Alertas críticas

## 6. Integración con el Dashboard Táctico
- Paneles: Cognitive Engine, Forensic Alerts, Visual Evidence, KPIs globales.
- Estado: Activo, Degradado, Crítico.
- Métricas: Disponibilidad, integridad, actividad.

## 7. Integración con el Orquestador
- Recibe señales de todos los módulos.
- Muestra reglas activas y recomendaciones.
- Ejemplo YAML:
```yaml
rule:
  name: "Visualización de alerta crítica"
  condition: "alert.severity == 'critical'"
  action: "dashboard.notify(alert)"
  severity: "critical"
  recommendation: "Escalar a SOC"
```

## 8. Escenarios Operativos
- Estado normal: Todos los paneles OK.
- Estado degradado: Panel sin datos, alerta generada.
- Señal de riesgo: Alerta crítica visualizada.
- Recomendación: Exportar reporte y escalar.

## 9. Relación con Estándares
- CIS 6, NIST SI-4, MITRE ATT&CK (defensivo: T1078), SABSA Service Layer.

## 10. Resumen Ejecutivo Operativo
El Dashboard centraliza la visibilidad, acelerando la toma de decisiones y la respuesta táctica en ARES‑11.

## 11. Enlace al Index Maestro
[Volver al índice maestro](index.md)
