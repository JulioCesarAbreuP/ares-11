from impacket.smbconnection import SMBConnection

def check_null_session(target):
    try:
        # Intento de conexión sin usuario ni password
        conn = SMBConnection(target, target)
        conn.login('', '') 
        print(f"[!!!] CRÍTICO: Null Session permitida en {target}. Extrayendo SID y Usuarios...")
        # Aquí ARES-11 lista los usuarios de la oficina
    except:
        print(f"[+] {target}: SMB Protegido contra sesiones nulas.")
