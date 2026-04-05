# 1. Core (Orquestador Principal)

## 1. Descripción Operativa
El Core es el cerebro táctico de ARES‑11. Orquesta, supervisa y coordina todos los módulos, asegurando la comunicación, el ciclo de vida y la integridad doctrinal del sistema. Es responsable de la activación, monitoreo y shutdown seguro de cada componente.

## 2. Propósito Operativo
- Supervisa el estado de todos los módulos.
- Procesa señales de salud, errores y eventos críticos.
- Toma decisiones de reinicio, escalado o aislamiento de módulos.
- Alimenta el motor de razonamiento con el estado global y señales de control.

## 3. Procedimientos Operativos Estándar (SOP)
- Iniciar: Ejecutar `main.go` o el binario principal.
- Interpretar salidas: Revisar logs de inicialización y estado.
- Validar: Confirmar que todos los módulos reportan “OK”.
- Anomalías: Si un módulo no responde, el Core lo reinicia o aísla.
- Buenas prácticas: Mantener logs centralizados y monitoreo activo.

## 4. Flujo Operativo
- Entradas: Señales de módulos, comandos de operador, eventos de error.
- Procesamiento: Validación, correlación, decisión de acción.
- Salidas: Señales de control, logs, alertas.
- Integración: Todos los módulos dependen del Core.
- Dependencias: Configuración global, canal de señales.

## 5. KPIs y Señales Clave
- Estado de módulos (OK, Degradado, Fallo)
- Latencia de respuesta
- Número de reinicios
- Alertas críticas
- Umbral: 100% módulos activos

## 6. Integración con el Dashboard Táctico
- Visualiza el estado global y salud de cada módulo.
- Muestra alertas y logs recientes.
- KPIs: Disponibilidad, errores, reinicios.

## 7. Integración con el Orquestador
- Genera señales de control y salud.
- Reglas YAML ejemplo:
```yaml
rule:
  name: "Reinicio automático de módulo"
  condition: "module.status == 'Fallo'"
  action: "core.restart(module)"
  severity: "high"
  recommendation: "Revisar logs y dependencias"
```

## 8. Escenarios Operativos
- Estado normal: Todos los módulos OK.
- Estado degradado: Un módulo lento, Core alerta y monitorea.
- Señal de riesgo: Módulo no responde, Core lo reinicia.
- Recomendación: Escalar a soporte si falla repetidamente.

## 9. Relación con Estándares
- CIS Control 6, NIST SI-4, MITRE ATT&CK (defensivo: T1078), SABSA Service Layer.

## 10. Resumen Ejecutivo Operativo
El Core garantiza la resiliencia, disponibilidad y control centralizado de ARES‑11, mejorando la auditoría táctica y la gestión del riesgo operativo.

[Volver al índice maestro](../index.md)
