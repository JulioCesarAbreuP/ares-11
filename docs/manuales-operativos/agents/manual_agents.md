# 1. Agentes Distribuidos

## 1. Descripción Operativa
Los agentes distribuidos son los sensores y ejecutores tácticos de ARES‑11. Se despliegan en hosts, endpoints y dispositivos IoT para recolectar señales, ejecutar acciones y ampliar la cobertura de seguridad ofensiva y defensiva.

## 2. Propósito Operativo
- Supervisan la actividad local y de red en cada host.
- Procesan señales de eventos, anomalías y comandos del Core.
- Ejecutan acciones de remediación, aislamiento o simulación ofensiva.
- Alimentan el motor de razonamiento con telemetría y hallazgos.

## 3. Procedimientos Operativos Estándar (SOP)
- Iniciar: Desplegar el agente y registrar con el Core.
- Interpretar salidas: Revisar logs de actividad y reportes de señales.
- Validar: Confirmar comunicación con el Core y Cognitive Engine.
- Anomalías: Si el agente no reporta, reiniciar o reinstalar.
- Buenas prácticas: Mantener agentes actualizados y monitoreados.

## 4. Flujo Operativo
- Entradas: Eventos del host, comandos del Core, señales de red.
- Procesamiento: Análisis local, filtrado, ejecución de acciones.
- Salidas: Señales, logs, resultados de acciones.
- Integración: Core, Cognitive Engine, Remediation.
- Dependencias: Configuración local, canal seguro.

## 5. KPIs y Señales Clave
- Estado del agente (Activo, Inactivo, Error)
- Número de señales enviadas
- Acciones ejecutadas
- Alertas recibidas
- Umbral: 100% agentes reportando

## 6. Integración con el Dashboard Táctico
- Visualiza estado y cobertura de agentes.
- Muestra logs y acciones recientes.
- KPIs: Disponibilidad, actividad, integridad.

## 7. Integración con el Orquestador
- Genera señales de actividad y hallazgos.
- Reglas YAML ejemplo:
```yaml
rule:
  name: "Aislamiento automático de host"
  condition: "agent.signal == 'compromised'"
  action: "remediation.isolate(agent.host)"
  severity: "critical"
  recommendation: "Validar integridad del host"
```

## 8. Escenarios Operativos
- Estado normal: Agente activo y reportando.
- Estado degradado: Agente con errores de comunicación.
- Señal de riesgo: Detección de actividad sospechosa.
- Recomendación: Aislar host y escalar a SOC.

## 9. Relación con Estándares
- CIS Control 8, NIST SI-4, MITRE ATT&CK (defensivo: T1021), SABSA Service Layer.

## 10. Resumen Ejecutivo Operativo
Los agentes distribuidos extienden la visibilidad y capacidad de respuesta de ARES‑11, mejorando la detección y mitigación de amenazas en toda la infraestructura.

[Volver al índice maestro](../index.md)
