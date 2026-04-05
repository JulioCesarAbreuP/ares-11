# 1. Remediation

## 1. Descripción Operativa
Remediation es el módulo de respuesta automática y defensiva de ARES‑11. Ejecuta acciones de bloqueo, aislamiento y endurecimiento ante amenazas detectadas, integrando scripts generados por IA y reglas tácticas.

## 2. Propósito Operativo
- Supervisa alertas y recomendaciones del Cognitive Engine y agentes.
- Procesa señales de riesgo, compromiso y anomalía.
- Toma decisiones de acción defensiva u ofensiva controlada.
- Alimenta el dashboard y el orquestador con el estado de remediación.

## 3. Procedimientos Operativos Estándar (SOP)
- Iniciar: Configurar y habilitar el módulo desde el Core.
- Interpretar salidas: Revisar logs de acciones ejecutadas.
- Validar: Confirmar que las acciones se reflejan en el entorno.
- Anomalías: Si una acción falla, reintentar o escalar a soporte.
- Buenas prácticas: Mantener scripts y reglas actualizados.

## 4. Flujo Operativo
- Entradas: Alertas, recomendaciones, comandos de orquestador.
- Procesamiento: Validación, ejecución de scripts, registro de acciones.
- Salidas: Logs, estado de acciones, alertas de éxito/fallo.
- Integración: Core, Cognitive Engine, agentes, dashboard.
- Dependencias: Scripts, permisos, canal seguro.

## 5. KPIs y Señales Clave
- Acciones ejecutadas
- Tiempo de respuesta
- Éxito/fracaso de acciones
- Alertas de bloqueo/aislamiento
- Umbral: 100% acciones exitosas

## 6. Integración con el Dashboard Táctico
- Visualiza acciones recientes, estado y logs de remediación.
- Métricas: Tiempo de respuesta, éxito, fallos.

## 7. Integración con el Orquestador
- Genera logs y señales de acción.
- Reglas YAML ejemplo:
```yaml
rule:
  name: "Remediación automática ante compromiso"
  condition: "alert.type == 'compromised'"
  action: "remediation.block(alert.host)"
  severity: "critical"
  recommendation: "Validar aislamiento y revisar logs"
```

## 8. Escenarios Operativos
- Estado normal: Sin acciones pendientes.
- Estado degradado: Acción fallida, alerta generada.
- Señal de riesgo: Compromiso detectado, acción ejecutada.
- Recomendación: Escalar si falla repetidamente.

## 9. Relación con Estándares
- CIS 10, NIST IR-4, MITRE ATT&CK (defensivo: T1562), SABSA Service Layer.

## 10. Resumen Ejecutivo Operativo
Remediation automatiza la respuesta táctica y defensiva, reduciendo el tiempo de mitigación y mejorando la resiliencia operativa de ARES‑11.

[Volver al índice maestro](../index.md)
