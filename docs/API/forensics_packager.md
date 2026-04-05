------------------------------------------------------------
1. Nombre del Módulo / Herramienta
------------------------------------------------------------
Forensics Packager (Empaquetador Forense)

------------------------------------------------------------
2. Objetivo Técnico
------------------------------------------------------------
Empaquetar y preservar evidencia técnica (logs, hallazgos, capturas) en un archivo ZIP para análisis forense, cumplimiento o entrega legal.

------------------------------------------------------------
3. Arquitectura Interna
------------------------------------------------------------
- Componente principal: package_forensics(evidence_paths, output_zip)
- Flujo de datos: Recibe rutas de evidencia, crea ZIP
- Entradas: Lista de rutas de archivos o carpetas
- Salidas: Archivo ZIP
- Dependencias: zipfile, os
- Estándares: Preservación de evidencia, cadena de custodia

------------------------------------------------------------
4. Uso Técnico
------------------------------------------------------------
- Parámetros: evidence_paths (list[str]), output_zip (str)
- Entrada esperada: Rutas válidas
- Salida: ZIP con evidencia
- Comportamiento: Empaqueta todo el contenido
- Limitaciones: No comprime archivos abiertos o bloqueados

------------------------------------------------------------
5. Ejemplos Prácticos
------------------------------------------------------------
# Pseudocódigo
from engine.forensics_packager import package_forensics
package_forensics(['logs/', 'reports/'], 'evidencia.zip')

------------------------------------------------------------
6. Integración con ARES‑11
------------------------------------------------------------
- Se conecta al pipeline de cierre de auditoría o incidentes
- Puede ser invocado manual o automáticamente

------------------------------------------------------------
7. Flujo Táctico
------------------------------------------------------------
Descubrimiento → Evaluación → Correlación → Evidencia → Recomendación → Visualización

------------------------------------------------------------
8. Controles y Estándares Asociados
------------------------------------------------------------
- CIS Controls: 8, 16
- NIST 800‑53: IR-5, AU-9
- MITRE ATT&CK: T1560 (defensivo)
- SABSA: Capa de Evidencia y Cumplimiento

------------------------------------------------------------
9. Ejemplo de Regla del Orquestador
------------------------------------------------------------
rule:
  name: package_evidence
  when: audit_completed
  action: package_forensics(['logs/', 'reports/'], 'evidencia.zip')

------------------------------------------------------------
10. Recomendaciones Técnicas
------------------------------------------------------------
- Usar tras auditorías o incidentes críticos
- Validar integridad del ZIP generado

------------------------------------------------------------
11. Métricas y Señales
------------------------------------------------------------
- Mide: Volumen de evidencia preservada
- Indicadores: Tamaño del ZIP, número de archivos

------------------------------------------------------------
12. Resumen Ejecutivo
------------------------------------------------------------
Forensics Packager asegura la preservación y entrega profesional de evidencia técnica, facilitando el cumplimiento y la respuesta ante incidentes en auditorías de alto nivel.

------------------------------------------------------------
