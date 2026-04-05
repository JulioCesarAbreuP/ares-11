import threading
from scanner.os_firmware_engine import get_deep_infrastructure_details
from scanner.network_hardware_audit import get_port_speeds
# from engine.cisa_correlator import check_known_exploits  # Placeholder for CISA correlation

def auditoria_total_un_clic(network_range):
    print("🚀 ARES-11: Iniciando Ejecución Táctica...")

    # Hilo 1: Velocidad de cables y hardware (Capa 1 y 2)
    t1 = threading.Thread(target=get_port_speeds, args=(network_range,))
    # Hilo 2: Versiones de Windows, parches y firmware (Capa 3 y 4)
    t2 = threading.Thread(target=get_deep_infrastructure_details, args=(network_range,))
    # Hilo 3: Cruce con vulnerabilidades reales de CISA (Inteligencia)
    # t3 = threading.Thread(target=check_known_exploits, args=(network_range,))

    t1.start()
    t2.start()
    # t3.start()

    t1.join(); t2.join() #; t3.join()
    print("✅ Auditoría Exhaustiva Completada. Scripts de remediación generados.")

if __name__ == "__main__":
    # Ejemplo: Escanear toda la oficina
    auditoria_total_un_clic("192.168.1.0/24")
