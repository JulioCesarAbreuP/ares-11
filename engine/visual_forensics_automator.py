# visual_forensics_automator.py
# Automatiza la integración de hallazgos visuales en el dashboard y reportes, y ejecuta remediación inmediata según IA

import json
import os
from datetime import datetime
from visual_forensics import analyze_visual_evidence

REPORT_PATH = '../reports/FORENSIC_SUMMARY.md'
ACTIONS_LOG = '../ares_omni_log.txt'

# Ejecuta análisis visual y toma acción según IA

def process_visual_evidence(image_path):
    print(f"[*] Analizando evidencia visual: {image_path}")
    ia_result = analyze_visual_evidence(image_path)
    try:
        result_json = json.loads(ia_result)
    except Exception as e:
        print("[!] Error interpretando respuesta IA:", e)
        result_json = {}
    # Integra hallazgo en reporte forense
    update_forensic_report(image_path, result_json)
    # Ejecuta remediación inmediata si IA lo recomienda
    if result_json.get('accion'):
        log_action(f"Remediación visual: {result_json['accion']}")
        execute_remediation(result_json['accion'])

# Actualiza el reporte forense con hallazgos visuales
def update_forensic_report(image_path, result_json):
    if not os.path.exists(REPORT_PATH):
        return
    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        f.write(f"\n## Evidencia Visual Analizada ({datetime.now()})\n")
        f.write(f"- Imagen: {image_path}\n")
        if 'hallazgo' in result_json:
            f.write(f"- Hallazgo: {result_json['hallazgo']}\n")
        if 'accion' in result_json:
            f.write(f"- Acción Recomendada: {result_json['accion']}\n")

# Log de acciones ejecutadas
def log_action(msg):
    ts = datetime.utcnow().isoformat() + "Z"
    with open(ACTIONS_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [VISUAL-REMEDIATION] {msg}\n")

# Ejecuta remediación inmediata (ejemplo: aislamiento, bloqueo, rotación de claves)
def execute_remediation(accion):
    # Aquí puedes integrar scripts de PowerShell, Azure CLI, etc.
    print(f"[!] Ejecutando acción de remediación: {accion}")
    # Ejemplo: si la acción es 'aislar', podrías llamar a un script de aislamiento
    # subprocess.run([...])

if __name__ == "__main__":
    # Ejemplo de uso:
    # process_visual_evidence('../reports/evidence_192.168.1.101.png')
    pass
