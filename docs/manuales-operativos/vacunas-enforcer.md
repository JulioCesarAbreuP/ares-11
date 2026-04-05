# 1. Vacunas / Enforcer (Hardening Automático)

## 2. Propósito Operativo
Automatizar el endurecimiento, bloqueo y aislamiento de hosts y vectores de ataque mediante scripts generados por IA y reglas tácticas.

## 3. Procedimientos Operativos Estándar (SOP)
- Ejecutar scripts de vacuna (`vacuna.ps1`, `vacuna_isolator.ps1`).
- Validar logs de ejecución y estado del host.
- Ante fallos, reintentar o escalar a soporte.
- Buenas prácticas: Mantener scripts y reglas actualizados.

## 4. Flujo Operativo
- Entradas: Alertas, recomendaciones, comandos de remediación.
- Procesamiento: Validación, ejecución de scripts, registro de acciones.
- Salidas: Logs, estado de acciones, alertas de éxito/fallo.
- Integración: Remediation, Cognitive Engine, Forense.
- Dependencias: PowerShell, permisos, canal seguro.

## 5. KPIs y Señales Clave
- Scripts ejecutados
- Hosts aislados
- Éxito/fracaso de acciones
- Umbral: 100% acciones exitosas

## 6. Integración con el Dashboard Táctico
- Visualiza acciones recientes, estado y logs de hardening.
- Estado: Activo, Degradado, Crítico.
- Métricas: Acciones, éxito, fallos.

## 7. Integración con el Orquestador
- Genera logs y señales de acción.
- Reglas YAML ejemplo:
```yaml
rule:
  name: "Vacuna automática por compromiso"
  condition: "alert.type == 'compromised'"
  action: "enforcer.block(alert.host)"
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
Vacunas y Enforcer automatizan el hardening y la respuesta, reduciendo el tiempo de mitigación y mejorando la resiliencia operativa.

## 11. Enlace al Index Maestro
[Volver al índice maestro](index.md)
