# engine/kill_switch.py
"""
Kill-Switch: Bloquea automáticamente la IP de cualquier dispositivo sospechoso mediante reglas de firewall.
"""
import os

def block_ip(ip):
    print(f"[KILL-SWITCH] Bloqueando IP sospechosa: {ip}")
    # Windows (PowerShell)
    os.system(f"powershell New-NetFirewallRule -DisplayName 'ARES11_Block_{ip}' -Direction Inbound -RemoteAddress {ip} -Action Block")
    # Linux (iptables)
    # os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    # Azure (CLI)
    # os.system(f"az network nsg rule create --resource-group MyRG --nsg-name MyNSG --name Block_{ip} --priority 100 --source-address-prefixes {ip} --access Deny --protocol '*' --direction Inbound")
    print(f"[KILL-SWITCH] IP {ip} bloqueada.")
