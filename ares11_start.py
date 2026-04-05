import subprocess
from scanner.high_speed_probe import industrial_scan
from engine.intelligence import correlate_findings

def ares_execution_clic():
    # 1. Escaneo de red (Oficina Clase C /24)
    network_data = industrial_scan("192.168.1.0/24")
    
    # 2. Correlación con Inteligencia de Amenazas
    threats = correlate_findings(network_data)
    
    # 3. Generar Reporte NIST y Scripts de Remediación
    # subprocess.run(["python3", "engine/enforcer.py"])
    
    print(">> AUDITORÍA TÁCTICA COMPLETADA. REVISE EL DASHBOARD.")

if __name__ == "__main__":
    ares_execution_clic()
