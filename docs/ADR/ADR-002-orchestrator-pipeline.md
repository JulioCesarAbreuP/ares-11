# ADR-002 Orchestrator & Pipeline

## Contexto y motivación
El orchestrator y el pipeline son el núcleo operativo y de control de ARES-11, diseñados para garantizar ejecución coherente, trazable, auditable y resiliente de flujos de ciberseguridad. La complejidad de amenazas y la necesidad de cumplimiento exigen flujos adaptativos, validables y con defensa en profundidad.

## Decisión arquitectónica reforzada
Se implementa un orchestrator central robusto que controla la secuencia, integración y coordinación de módulos a través de un pipeline configurable y validable. El orchestrator gestiona dependencias, sincronización, manejo de errores, telemetría avanzada y puntos de control, permitiendo flujos dinámicos, auditables y recuperables.

## Flujo de ejecución endurecido
1. Carga y validación estricta de configuración y parámetros iniciales
2. Inicialización, chequeo de salud y control de acceso de módulos requeridos
3. Orquestación dinámica y validable del pipeline según dependencias, prioridades y contexto
4. Manejo estructurado y centralizado de errores, eventos y telemetría avanzada
5. Recolección de resultados, generación de reportes, emisión de evidencia técnica y triggers de auditoría

## Entradas y salidas
- **Entradas**: Configuración, datos de inteligencia (TAXII, archivos, API), reglas, mapeos, parámetros de usuario, contexto de ejecución, triggers externos.
- **Salidas**: Reportes, dashboards, métricas, logs, eventos de telemetría, alertas, evidencia técnica, artefactos de auditoría.

## Integración con módulos
El orchestrator invoca módulos core y externos mediante interfaces y contratos explícitos, versionados y auditables. Cada módulo expone funciones, métricas y estados, reportando resultados y eventos al orchestrator para trazabilidad, auditoría y manejo centralizado de errores y telemetría.

## Telemetría Avanzada
- **Eventos clave**: inicio/fin de pipeline, fallos de módulos, cambios de configuración, integración/desacople de módulos, generación de evidencia, alertas de seguridad, triggers de auditoría.
- **Métricas críticas**: tiempos de ejecución por etapa y módulo, número de eventos procesados, errores y advertencias por tipo, uso de recursos, latencia, disponibilidad, cobertura de pruebas, integridad de artefactos.
- **Trazabilidad**: identificadores únicos de ejecución, correlación de eventos, historial completo de decisiones, resultados y auditorías, relación entradas-módulos-salidas-evidencia.
- **Puntos de observabilidad**: hooks y checkpoints en cada transición de etapa, logging estructurado, auditoría de cambios, exportación de telemetría y artefactos para análisis externo.

## Consecuencias
### Positivas
- Flujos adaptativos, auditables y recuperables
- Trazabilidad, control centralizado de errores y telemetría avanzada
- Facilidad de integración, extensión y certificación de módulos
### Negativas
- Complejidad en la gestión de dependencias, sincronización y telemetría
- Riesgo de acoplamiento si no se respetan interfaces, modularidad y contratos

## Estado
Adoptado, endurecido y en mejora continua, alineado con la arquitectura, visión de producto y hardening ARES-11.