# scripts/generate_module_docs.py
"""
Script para generación automática de documentación técnica de módulos ARES-11.
Cada vez que se detecta un nuevo módulo en /engine, genera su ficha en docs/API/ siguiendo el formato doctrinal.
"""
import os
import importlib.util

MODULE_DOC_TEMPLATE = '''
------------------------------------------------------------
1. Nombre del Módulo / Herramienta
------------------------------------------------------------
{mod_name}

------------------------------------------------------------
2. Objetivo Técnico
------------------------------------------------------------
[Completar: objetivo técnico del módulo]

------------------------------------------------------------
3. Arquitectura Interna
------------------------------------------------------------
[Completar: arquitectura interna, componentes, flujo de datos, dependencias]

------------------------------------------------------------
4. Uso Técnico
------------------------------------------------------------
[Completar: uso técnico, parámetros, entradas, salidas, limitaciones]

------------------------------------------------------------
5. Ejemplos Prácticos
------------------------------------------------------------
# Pseudocódigo
from engine.{mod_name} import ...

------------------------------------------------------------
6. Integración con ARES‑11
------------------------------------------------------------
[Completar: integración con motor, orquestador, dashboard, modelo de riesgo, telemetría]

------------------------------------------------------------
7. Flujo Táctico
------------------------------------------------------------
[Completar: rol en el ciclo de auditoría]

------------------------------------------------------------
8. Controles y Estándares Asociados
------------------------------------------------------------
[Completar: CIS, NIST, MITRE, SABSA]

------------------------------------------------------------
9. Ejemplo de Regla del Orquestador
------------------------------------------------------------
rule:
  name: {mod_name}_rule
  when: [evento]
  action: [acción]

------------------------------------------------------------
10. Recomendaciones Técnicas
------------------------------------------------------------
[Completar: buenas prácticas, riesgos mitigados, señales]

------------------------------------------------------------
11. Métricas y Señales
------------------------------------------------------------
[Completar: métricas, indicadores, scoring]

------------------------------------------------------------
12. Resumen Ejecutivo
------------------------------------------------------------
[Completar: resumen ejecutivo para CISO, auditor, gerente]

------------------------------------------------------------
'''

def generate_docs_for_engine_modules():
    engine_dir = os.path.join(os.path.dirname(__file__), '../engine')
    docs_dir = os.path.join(os.path.dirname(__file__), '../docs/API')
    os.makedirs(docs_dir, exist_ok=True)
    for fname in os.listdir(engine_dir):
        if fname.endswith('.py') and not fname.startswith('__'):
            mod_name = fname[:-3]
            doc_path = os.path.join(docs_dir, f'{mod_name}.md')
            if not os.path.exists(doc_path):
                with open(doc_path, 'w', encoding='utf-8') as f:
                    f.write(MODULE_DOC_TEMPLATE.format(mod_name=mod_name))
                print(f"[DOCS] Documentación generada para {mod_name}")

if __name__ == '__main__':
    generate_docs_for_engine_modules()
