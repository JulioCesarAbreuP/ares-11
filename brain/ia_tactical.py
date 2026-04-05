# ia_tactical.py
# Motor de IA Táctica Local (Ollama + Python)
# No envía datos a la nube. Analiza JSON de escaneo y ejecuta defensa ofensiva/defensiva.

import ollama
import json
import subprocess
import os
from datetime import datetime

LOG_FILE = "../ares_omni_log.txt"

def ia_tactical_analysis(scan_data):
    prompt = f"""
    Analiza estos datos de red: {scan_data}
    1. Identifica el dispositivo más vulnerable (Cafetera, PC, Router).
    2. Explica cómo un atacante saltaría de ese dispositivo al Domain Controller (SC-300).
    3. Genera el script de PowerShell para bloquear ese vector de ataque inmediatamente.
    Responde solo en formato JSON técnico.
    """
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

def log(fase, mensaje):
    ts = datetime.utcnow().isoformat() + "Z"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [{fase}] {mensaje}\n")

def ejecutar_vacuna(script_powershell):
    # Ejecuta el script de PowerShell generado por la IA
    vacuna_path = os.path.join("vaccines", "vacuna.ps1")
    with open(vacuna_path, "w", encoding="utf-8") as f:
        f.write(script_powershell)
    log("DEFENSE", "Vacuna generada y ejecutada por IA")
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", vacuna_path])

def main():
    with open("scan_result.json", encoding="utf-8") as f:
        scan_data = f.read()
    resultado_ia = ia_tactical_analysis(scan_data)
    print("Respuesta IA:", resultado_ia)
    try:
        resultado_json = json.loads(resultado_ia)
        vulnerable = resultado_json.get("dispositivo_mas_vulnerable") or resultado_json.get("vulnerable")
        if vulnerable:
            log("AI", f"Dispositivo más vulnerable: {vulnerable}")
        if "powershell" in resultado_json:
            log("AI", f"Script generado por IA: {resultado_json['powershell'][:100]}...")
        if resultado_json.get("riesgo", 0) >= 8:
            ejecutar_vacuna(resultado_json["powershell"])
    except Exception as e:
        print("Error interpretando la respuesta de la IA:", e)
        log("AI", f"Error interpretando respuesta IA: {e}")

if __name__ == "__main__":
    main()
