# engine/exporter.py
"""
Exporta hallazgos y rutas de ataque a CSV/Excel.
"""
import csv

def export_findings_csv(findings, filename='ares11_findings.csv'):
    if not findings:
        print("[EXPORT] No hay hallazgos para exportar.")
        return
    keys = findings[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(findings)
    print(f"[EXPORT] Hallazgos exportados a {filename}")
