# forensic_analyst.py
# Analista de Persistencia y Kill-Chain Forense para ARES-11
# Detecta beaconing, exfiltración, MAC spoofing y ejecuta la Vacuna de Aislamiento

import pandas as pd
from datetime import datetime, timedelta
import os
import subprocess

forensic_log = "../logs/forensic_evidence.csv"
vacuna_path = "../vaccines/vacuna_isolator.ps1"
alertas = []

# Detección de beaconing (C2):
def detect_beaconing(df):
    beacon_ips = []
    for ip, group in df.groupby('ip'):
        times = pd.to_datetime(group['timestamp'])
        if len(times) > 3:
            intervals = (times - times.shift()).dropna().dt.total_seconds()
            if (intervals.round().value_counts().get(60, 0) >= 2):
                beacon_ips.append(ip)
    return beacon_ips

# Detección de exfiltración (pico de subida desde IoT)
def detect_exfiltration(df):
    # Simulación: si un IoT (Linux/IoT/Embedded) tiene más de 3 conexiones en 5 min
    exfil_ips = []
    now = datetime.now()
    for ip, group in df[df['os_detected']=='Linux/IoT/Embedded'].groupby('ip'):
        times = pd.to_datetime(group['timestamp'])
        recent = times[times > now - timedelta(minutes=5)]
        if len(recent) > 3:
            exfil_ips.append(ip)
    return exfil_ips

# Detección de MAC spoofing y TTL mismatch
def detect_mac_spoofing(df):
    spoofed = []
    for idx, row in df.iterrows():
        if 'VMware' in str(row['mac']) or (row['os_detected']=='Windows/Azure' and row['ttl']<100):
            spoofed.append(row['ip'])
    return spoofed

# Acción automática: Vacuna de aislamiento
def ejecutar_vacuna_isolator(ip):
    script = f"# Vacuna de aislamiento para {ip}\nNew-NetFirewallRule -DisplayName 'Aislamiento {ip}' -Direction Inbound -RemoteAddress {ip} -Action Block\n"
    with open(vacuna_path, "w", encoding="utf-8") as f:
        f.write(script)
    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", vacuna_path])
    print(f"[DEFENSE] Vacuna de aislamiento ejecutada para {ip}")

# Análisis principal
def main():
    if not os.path.exists(forensic_log):
        print("No hay evidencia forense para analizar.")
        return
    df = pd.read_csv(forensic_log)
    # Beaconing
    beacon_ips = detect_beaconing(df)
    for ip in beacon_ips:
        alertas.append(f"[C2/Beaconing] Dispositivo {ip} muestra patrón de beaconing (C2)")
    # Exfiltración
    exfil_ips = detect_exfiltration(df)
    for ip in exfil_ips:
        alertas.append(f"[Exfiltración] IoT {ip} muestra posible exfiltración de datos")
    # MAC spoofing/TTL mismatch
    spoofed_ips = detect_mac_spoofing(df)
    for ip in spoofed_ips:
        alertas.append(f"[MAC Spoofing/TTL] Dispositivo {ip} sospechoso. Ejecutando vacuna de aislamiento...")
        ejecutar_vacuna_isolator(ip)
    # Reporte
    print("\n--- ALERTAS CRÍTICAS ---")
    for alerta in alertas:
        print(alerta)
    # Actualiza el reporte forense
    update_forensic_report(alertas)

def update_forensic_report(alertas):
    report_path = "../reports/FORENSIC_SUMMARY.md"
    if not os.path.exists(report_path):
        return
    with open(report_path, "a", encoding="utf-8") as f:
        f.write("\n## Alertas Críticas Detectadas por Analista Forense\n")
        for alerta in alertas:
            f.write(f"- {alerta}\n")
        f.write(f"\n_Actualizado: {datetime.now()}\n")

if __name__ == "__main__":
    main()
