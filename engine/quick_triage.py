# engine/quick_triage.py
"""
Módulo de Análisis Rápido: Detecta y reporta los 5 riesgos más críticos en minutos.
"""
def quick_triage(scan_results):
    # Ordena por severidad y retorna los 5 principales
    sorted_findings = sorted(scan_results, key=lambda x: x.get('risk_level', 'LOW'), reverse=True)
    return sorted_findings[:5]
