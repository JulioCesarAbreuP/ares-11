------------------------------------------------------------
1. Nombre del Módulo / Herramienta
------------------------------------------------------------
Quick Triage (Análisis Rápido)

------------------------------------------------------------
2. Objetivo Técnico
------------------------------------------------------------
Detectar y reportar de forma inmediata los 5 riesgos más críticos identificados en la red, permitiendo una respuesta táctica rápida y priorización de acciones.

------------------------------------------------------------
3. Arquitectura Interna
------------------------------------------------------------
- Componente principal: quick_triage(scan_results)
- Flujo de datos: Recibe lista de hallazgos, ordena por severidad, retorna los 5 principales.
- Entradas: Lista de hallazgos (dicts)
- Salidas: Lista de los 5 hallazgos más críticos
- Dependencias: Motor de escaneo, pipeline de hallazgos
- Estándares: CIS, NIST, MITRE (priorización de riesgos)

------------------------------------------------------------
4. Uso Técnico
------------------------------------------------------------
- Parámetros: scan_results (list[dict])
- Entrada esperada: Lista de hallazgos con campo 'risk_level'
- Salida: Lista de 5 dicts de hallazgos críticos
- Comportamiento: Ordena y filtra automáticamente
- Limitaciones: Depende de la calidad de los hallazgos previos

------------------------------------------------------------
5. Ejemplos Prácticos
------------------------------------------------------------
# Pseudocódigo
from engine.quick_triage import quick_triage
critical = quick_triage(scan_results)
for finding in critical:
    print(finding)

------------------------------------------------------------
6. Integración con ARES‑11
------------------------------------------------------------
- Se conecta al pipeline de hallazgos tras el escaneo
- Puede ser invocado por el orquestador para reportes rápidos
- Sus resultados pueden visualizarse en el dashboard táctico

------------------------------------------------------------
7. Flujo Táctico
------------------------------------------------------------
Descubrimiento → Evaluación → Quick Triage → Correlación → Recomendación → Visualización

------------------------------------------------------------
8. Controles y Estándares Asociados
------------------------------------------------------------
- CIS Controls: 1, 4, 16
- NIST 800‑53: RA-5, SI-2
- MITRE ATT&CK: T1589, T1590 (defensivo)
- SABSA: Capa de Operación y Control

------------------------------------------------------------
9. Ejemplo de Regla del Orquestador
------------------------------------------------------------
rule:
  name: quick_triage_top5
  when: scan_completed
  action: quick_triage(scan_results)
  output: critical_findings

------------------------------------------------------------
10. Recomendaciones Técnicas
------------------------------------------------------------
- Usar tras cada escaneo para priorizar acciones
- Integrar en reportes ejecutivos
- Revisar hallazgos para evitar falsos positivos

------------------------------------------------------------
11. Métricas y Señales
------------------------------------------------------------
- Mide: Severidad y frecuencia de riesgos críticos
- Indicadores: Top 5 riesgos actuales
- Contribuye al scoring de riesgo global

------------------------------------------------------------
12. Resumen Ejecutivo
------------------------------------------------------------
Quick Triage permite a los equipos de seguridad identificar y actuar sobre los riesgos más críticos en minutos, optimizando la toma de decisiones y la respuesta táctica en auditorías de alto impacto.

------------------------------------------------------------
