import json

def generate_remediation(finding):
    """
    Toma un hallazgo y genera el script de remediación específico.
    Alineado con AZ-104 (Infra) y SC-300 (Identidad).
    """
    remediation_script = ""
    
    # Caso: RDP Expuesto (Fallo CIS 5.1 / NIST Protect)
    if finding['issue'] == "RDP Expuesto":
        remediation_script = """
# ARES-11 Remediation Script: Secure RDP
# Target: Azure NSG / Local Windows Firewall

# 1. Bloquear RDP desde Internet en Firewall Local
Disable-NetFirewallRule -DisplayName "Remote Desktop - User Mode (TCP-In)"

# 2. Sugerencia AZ-104: Cerrar puerto en el NSG de Azure vía CLI
# az network nsg rule update --resource-group MyRG --nsg-name MyNSG --name AllowRDP --access Deny
        """
    
    # Caso: SNMP Inseguro (Fallo CIS 4.1)
    elif finding['issue'] == "SNMP v1/v2 Detectado":
        remediation_script = """
# ARES-11 Remediation: Disable Insecure SNMP
Stop-Service -Name "SNMP"
Set-Service -Name "SNMP" -StartupType Disabled
        """
        
    return remediation_script

# Ejecución de prueba
sample_finding = {'issue': 'RDP Expuesto'}
print(f"--- SCRIPT DE REMEDIACIÓN GENERADO ---\n{generate_remediation(sample_finding)}")
