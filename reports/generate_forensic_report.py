# generate_forensic_report.py
# Genera un reporte forense automatizado en Markdown para CISO

import pandas as pd
from datetime import datetime
import os

forensic_log = "../logs/forensic_evidence.csv"
report_path = "FORENSIC_SUMMARY.md"

def generate_forensic_report():
    if not os.path.exists(forensic_log):
        print("No hay evidencia forense para reportar.")
        return
    data = pd.read_csv(forensic_log)
    summary = data.groupby('os_detected').size()
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# ARES-11: Reporte Forense de Infraestructura\n\n")
        f.write(f"**Fecha de Auditoría:** {datetime.now()}\n\n")
        f.write("## Resumen de Dispositivos Detectados\n")
        f.write(summary.to_markdown())
        f.write("\n\n## Alertas Críticas\n")
        f.write("- (Aquí la IA inserta las anomalías detectadas)\n")
        f.write("\n---\n\n_Este reporte se genera automáticamente por el sensor forense y el módulo de análisis de ARES-11._\n")
    print(f"Reporte generado en {report_path}")

if __name__ == "__main__":
    generate_forensic_report()
