import ollama
import json
import subprocess
import os
from datetime import datetime
from core.events import EventBus
from core.contracts import DecisionOutput

LOG_FILE = "../ares_omni_log.txt"

def ia_tactical_analysis(scan_data) -> DecisionOutput:
    prompt = f"""
    Analiza estos datos de red: {scan_data}
    1. Identifica el dispositivo más vulnerable (Cafetera, PC, Router).
    2. Explica cómo un atacante saltaría de ese dispositivo al Domain Controller (SC-300).
    3. Genera el script de PowerShell para bloquear ese vector de ataque inmediatamente.
    Responde solo en formato JSON técnico.
    """
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    content = response['message']['content']
    try:
        resultado_json = json.loads(content)
        vulnerable = resultado_json.get("dispositivo_mas_vulnerable") or resultado_json.get("vulnerable")
        justification = resultado_json.get("explicacion", "")
        confidence = resultado_json.get("riesgo", 0) / 10.0
        action = "block" if confidence >= 0.8 else "monitor"
        EventBus().publish("tactical_ai.analyzed", resultado_json)
        return DecisionOutput(action=action, confidence=confidence, justification=justification, metadata=resultado_json)
    except Exception as e:
        print("Error interpretando la respuesta de la IA:", e)
        EventBus().publish("tactical_ai.error", {"error": str(e)})
        return DecisionOutput(action="error", confidence=0.0, justification=str(e), metadata={})

def log(fase, mensaje):
    ts = datetime.utcnow().isoformat() + "Z"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [{fase}] {mensaje}\n")

def ejecutar_vacuna(script_powershell):
    vacuna_path = os.path.join("vaccines", "vacuna.ps1")
    with open(vacuna_path, "w", encoding="utf-8") as f:
        f.write(script_powershell)
    log("DEFENSE", "Vacuna generada y ejecutada por IA")
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", vacuna_path])