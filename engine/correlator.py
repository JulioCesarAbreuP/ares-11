import json

def analyze_risk(scan_data):
    recommendations = []
    
    # Lógica SC-300: Identidad y Acceso
    if scan_data['port'] == 3389 and scan_data['status'] == "Open":
        recommendations.append({
            "control": "CIS 5.1 / SC-300",
            "issue": "RDP Expuesto",
            "fix": "Habilitar NLA y restringir via Azure NSG (AZ-104)",
            "mitre_ttp": "T1021.001"
        })
    
    return recommendations

# Cargar datos y procesar
with open('data_scan.json', 'r') as f:
    data = json.load(f)
    report = analyze_risk(data)
    print(json.dumps(report, indent=2))
