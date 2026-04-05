# engine/remediation_script_gen.py
"""
Genera scripts de remediación personalizados para Windows, Linux y Azure.
"""
def generate_remediation_script(finding, os_type='windows'):
    if os_type == 'windows':
        if 'RDP' in finding.get('issue', ''):
            return "Disable-NetFirewallRule -DisplayName 'Remote Desktop - User Mode (TCP-In)'"
        if 'SMB' in finding.get('issue', ''):
            return "Set-SmbServerConfiguration -EnableSMB1Protocol $false"
    elif os_type == 'linux':
        if 'Telnet' in finding.get('issue', ''):
            return "sudo systemctl stop telnet.socket && sudo systemctl disable telnet.socket"
        if 'SNMP' in finding.get('issue', ''):
            return "sudo systemctl stop snmpd && sudo systemctl disable snmpd"
    elif os_type == 'azure':
        if 'NSG' in finding.get('issue', ''):
            return "az network nsg rule update --resource-group <RG> --nsg-name <NSG> --name <Rule> --access Deny"
    return "# Remediación personalizada no disponible para este hallazgo."
