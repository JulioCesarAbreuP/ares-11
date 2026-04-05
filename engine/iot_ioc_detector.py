# engine/iot_ioc_detector.py
"""
Detecta indicadores de compromiso (IoC) de malware por defecto en dispositivos IoT y recomienda defensas alineadas a SC-300/AZ-104.
"""

def detect_iot_iocs(host):
    findings = []
    # Cámaras IP: Telnet y HTTP expuestos
    if host.get('device_type') == 'camera' and (23 in host.get('ports', []) or 8080 in host.get('ports', [])):
        findings.append({
            "ioc": "Cámara IP con Telnet/HTTP expuesto",
            "defense": "Aislar en VLAN sin salida a Internet (ACLs en AZ-104)",
            "severity": "CRITICAL"
        })
    # Smart TV / IoT: Tráfico saliente sospechoso
    if host.get('device_type') in ['smart_tv', 'coffee_maker', 'fridge'] and host.get('suspicious_traffic', False):
        findings.append({
            "ioc": "Tráfico saliente a C2 (China/Rusia)",
            "defense": "Implementar Azure Firewall con filtrado IDPS",
            "severity": "HIGH"
        })
    # Impresoras: SNMP v1 comunidad 'public'
    if host.get('device_type') == 'printer' and host.get('snmp_version') == 'v1' and host.get('snmp_community') == 'public':
        findings.append({
            "ioc": "Impresora con SNMP v1 y comunidad 'public'",
            "defense": "Deshabilitar servicios innecesarios y usar SNMP v3",
            "severity": "HIGH"
        })
    return findings
