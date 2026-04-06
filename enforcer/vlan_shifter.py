import paramiko

def isolate_port(switch_ip, port_id, vlan_quarantine=999):
    print(f"[!] ARES-11: Iniciando Aislamiento Físico del puerto {port_id}...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Conexión al Switch (Cisco/Aruba/Ubiquiti)
    ssh.connect(switch_ip, username='ares_admin', password='secure_password')
    remote_conn = ssh.invoke_shell()
    # Comandos tácticos para mover el puerto a la VLAN de cuarentena
    remote_conn.send(f"conf t\n")
    remote_conn.send(f"interface {port_id}\n")
    remote_conn.send(f"switchport access vlan {vlan_quarantine}\n")
    remote_conn.send(f"exit\n")
    print(f"[✓] Puerto {port_id} movido a VLAN {vlan_quarantine}. Amenaza contenida.")
