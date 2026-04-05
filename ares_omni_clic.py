# ares_omni_clic.py
# Botón de un solo clic: ejecuta escaneo, IA táctica y defensa adaptativa

import subprocess
import sys
from datetime import datetime

LOG_FILE = "ares_omni_log.txt"

def run_scan():
    print("[+] Ejecutando escaneo de red simulado...")
    log("SCAN", "Escaneo de red iniciado")
    result = subprocess.run([sys.executable, "sniffers/network_scan.py"])
    if result.returncode != 0:
        print("[!] Error en el escaneo de red.")
        sys.exit(1)
    log("SCAN", "Escaneo completado")

def run_ia():
    print("[+] Ejecutando IA táctica local (Ollama + Python)...")
    log("AI", "Análisis IA iniciado")
    result = subprocess.run([sys.executable, "brain/ia_tactical.py"])
    if result.returncode != 0:
        print("[!] Error en la IA táctica.")
        sys.exit(1)
    log("AI", "Análisis IA completado")

def main():
    print("=== ARES-11 OMNI: Defensa y Ataque Autónomo ===")
    log("START", "Ciclo iniciado")
    run_scan()
    run_ia()
    print("[✓] Ciclo completo: Escaneo + IA + Defensa ejecutados.")
    log("END", "Ciclo completo ejecutado")

if __name__ == "__main__":
    main()
def log(fase, mensaje):
    ts = datetime.utcnow().isoformat() + "Z"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [{fase}] {mensaje}\n")
