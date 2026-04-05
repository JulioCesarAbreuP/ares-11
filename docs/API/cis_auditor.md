====================================================================
1. Nombre del Módulo / Herramienta
====================================================================
CIS Auditor

====================================================================
2. Propósito dentro del Motor
====================================================================
Evalúa el cumplimiento de controles CIS (IG1/IG2/IG3) en los activos descubiertos, identificando brechas y priorizando acciones correctivas en el ciclo: Descubrimiento → Evaluación → Correlación → Riesgo → Recomendación → Visualización.

====================================================================
3. Uso Detallado
====================================================================
- Entradas: Lista de activos, configuraciones, políticas.
- Salidas: Reporte de cumplimiento, hallazgos por control.
- Parámetros: Nivel de CIS, alcance, profundidad.
- Comportamiento: Valida configuraciones y presencia de controles.
- Limitaciones: Requiere acceso a configuraciones y políticas.

====================================================================
4. Ejemplos Prácticos
====================================================================
Invocación:
```python
from core.cis_auditor import run_cis_audit
report = run_cis_audit(assets, level='IG1')
```
Salida:
```json
{"CIS-4.1": "No cumple", "CIS-8.1": "Cumple"}
```
Integración:
- Alimenta el Risk Engine y Remediation Engine.

====================================================================
5. Flujo Interno
====================================================================
- Componentes: Validador de controles, generador de reportes.
- Flujo: Entrada de activos → Validación → Reporte.
- Señales: Brechas de cumplimiento, controles ausentes.
- Controles: CIS Controls.
- Interacción: Provee hallazgos al motor de razonamiento.

====================================================================
6. Integración con Otros Módulos
====================================================================
- Motor de razonamiento: Provee hallazgos de cumplimiento.
- Orquestador: Dispara reglas de remediación.
- Dashboard: Visualiza estado de cumplimiento.
- Modelo de riesgo: Ajusta scoring según brechas.
- Telemetría: Registra eventos de auditoría.

====================================================================
7. Controles y Estándares Asociados
====================================================================
- CIS Controls: 1-18
- NIST 800‑53: CA-7, SI-2
- MITRE ATT&CK: T1556, T1087 (defensivo)
- SABSA: Capa de Control y Cumplimiento

====================================================================
8. Ejemplo de Regla del Orquestador
====================================================================
```yaml
rule:
  name: cis_audit
  when: assets_discovered
  action: run_cis_audit(assets, level)
```

====================================================================
9. Métricas y Señales
====================================================================
- Mide: Porcentaje de cumplimiento, número de brechas.
- Indicadores: Controles cumplidos/no cumplidos.
- Scoring: Ajusta el riesgo residual.

====================================================================
10. Diseño de Interfaz (UI)
====================================================================
- Sección: “Cumplimiento CIS”
- Componentes: Tabla de controles, gráficos de barras, filtros por nivel.
- Indicadores: % cumplimiento, controles críticos.
- Integración: Dashboard táctico, alertas visuales.
- Estilo: Empresarial, colores de cumplimiento.

====================================================================
11. Resumen Ejecutivo
====================================================================
El CIS Auditor de ARES‑11 permite a las organizaciones medir y mejorar su postura de seguridad, alineando la operación con los estándares internacionales y facilitando la toma de decisiones basada en evidencia.

====================================================================
