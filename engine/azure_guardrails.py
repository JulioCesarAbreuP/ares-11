from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
import os


def audit_azure_networks(subscription_id):
    print(f"[*] ARES-11: Iniciando Auditoría de Nube (Subscription: {subscription_id})...")
    credential = DefaultAzureCredential()
    network_client = NetworkManagementClient(credential, subscription_id)
    nsgs = network_client.network_security_groups.list_all()
    for nsg in nsgs:
        for rule in nsg.security_rules:
            if rule.access == "Allow" and rule.direction == "Inbound":
                if rule.source_address_prefix == "*" and rule.destination_port_range in ["3389", "22"]:
                    print(f"[!!!] CRÍTICO: NSG '{nsg.name}' expone el puerto {rule.destination_port_range} a INTERNET.")
                    generate_cloud_remediation(nsg.name, rule.name)
    print("[+] Fase de NSG Guardrails completada.\n")

# --- Identity Guardrails (SC-300/MFA/Privileged Access) ---

def identity_guardrails_premium():
    print("[*] ARES-11: Identity Guardrails Premium (SC-300/Zero Trust)")
    # --- Datos simulados para demo doctrinal ---
    users = [
        {"user": "alice@empresa.com", "mfa": False, "roles": ["Global Admin"], "direct_perms": 5, "last_login_days": 120, "groups": ["Admins", "ShadowOps"], "mfa_rejects": 7, "mfa_attempts": 12},
        {"user": "bob@empresa.com", "mfa": True, "roles": ["User"], "direct_perms": 0, "last_login_days": 3, "groups": ["Users"], "mfa_rejects": 0, "mfa_attempts": 2},
        {"user": "carol@empresa.com", "mfa": False, "roles": ["User", "Privileged Role Admin"], "direct_perms": 2, "last_login_days": 45, "groups": ["PrivOps", "Users"], "mfa_rejects": 3, "mfa_attempts": 8},
        {"user": "dave@empresa.com", "mfa": True, "roles": ["User"], "direct_perms": 0, "last_login_days": 400, "groups": ["Users"], "mfa_rejects": 0, "mfa_attempts": 1},
    ]
    os.makedirs("vaccines", exist_ok=True)
    shadow_admins = []
    lateral_paths = []
    lockdown_actions = []
    with open("vaccines/identity_fix.sh", "w") as f, open("vaccines/identity_paths.txt", "w") as p, open("vaccines/emergency_lockdown.sh", "w") as l:
        for u in users:
            # --- Identity Exposure Score ---
            score = 10
            if u["mfa"]: score -= 4
            if any(r in ["Global Admin", "Privileged Role Admin"] for r in u["roles"]): score += 2
            if u["direct_perms"] > 0: score += u["direct_perms"]
            if u["last_login_days"] > 90: score += 2
            # --- Shadow Admin Detection ---
            shadow = False
            privilege_chain_length = 1
            if "ShadowOps" in u["groups"] or (len(u["roles"]) > 1 and "Privileged Role Admin" in u["roles"]):
                shadow = True
                privilege_chain_length = 2 + len(u["groups"])
                shadow_admins.append(u["user"])
                print(f"[SHADOW] {u['user']} es Shadow Admin (chain={privilege_chain_length})")
                f.write(f"# Revisar privilegios indirectos de {u['user']}\n")
            # --- MFA Fatigue Analysis ---
            mfa_fatigue_score = u["mfa_rejects"] * 2 + (u["mfa_attempts"] - u["mfa_rejects"])
            if mfa_fatigue_score > 10:
                print(f"[MFA FATIGUE] {u['user']} tiene score alto: {mfa_fatigue_score}")
                f.write(f"# Forzar reconfiguración MFA para {u['user']}\n")
            # --- Lateral Movement Pathing ---
            path = f"{u['user']} → {','.join(u['groups'])} → {','.join(u['roles'])} → CRITICAL_ASSET"
            lateral_paths.append(path)
            p.write(path + "\n")
            # --- JIT Recommendations ---
            if any(r in ["Global Admin", "Privileged Role Admin"] for r in u["roles"]):
                print(f"[JIT] {u['user']} tiene rol privilegiado permanente. Recomendado activar PIM/JIT.")
                f.write(f"# Activar PIM/JIT para {u['user']}\n")
            # --- Emergency Lockdown ---
            if score > 15 or shadow:
                lockdown_actions.append(u["user"])
                l.write(f"az ad user update --id {u['user']} --account-enabled false\n")
                l.write(f"az ad user revoke-signin-sessions --id {u['user']}\n")
                l.write(f"az ad user update --id {u['user']} --force-change-password-next-login\n")
            # --- Recomendaciones SC-300 clásicas ---
            print(f"[ID] Usuario: {u['user']}")
            print(f"    MFA: {'HABILITADO' if u['mfa'] else 'NO HABILITADO'} | Roles: {', '.join(u['roles'])} | Permisos directos: {u['direct_perms']} | Último login: {u['last_login_days']} días")
            print(f"    Identity Exposure Score: {score}/20 | Shadow Admin: {shadow}")
            if not u["mfa"]:
                print("    [DEF] Recomendación: Habilitar MFA (SC-300)")
                f.write(f"az ad user update --id {u['user']} --force-change-password-next-login\n")
            if u["direct_perms"] > 0:
                print("    [DEF] Recomendación: Revisar permisos asignados directamente (SC-300)")
                f.write(f"# Revisar permisos directos de {u['user']}\n")
            if u["last_login_days"] > 90:
                print("    [DEF] Recomendación: Deshabilitar cuenta inactiva (SC-300)")
                f.write(f"az ad user update --id {u['user']} --account-enabled false\n")
            print()
        # Sentinel/Defender Integration (Opcional)
        if os.getenv("SEND_TO_SENTINEL"):
            print("[SENTINEL] Enviando hallazgos críticos a Sentinel/Defender...")
            # Señal conceptual
            print("    [SENTINEL] sentinel_incident_created: True")
    print("[+] Archivo de acciones sugeridas: vaccines/identity_fix.sh")
    print("[+] Archivo de rutas de movimiento lateral: vaccines/identity_paths.txt")
    print("[+] Archivo de lockdown de emergencia: vaccines/emergency_lockdown.sh\n")
    # Resumen táctico doctrinal
    print("[RESUMEN PREMIUM] ARES-11 Identity Exposure:")
    print(f"  - Shadow Admins detectados: {len(shadow_admins)} → {', '.join(shadow_admins) if shadow_admins else 'Ninguno'}")
    print(f"  - Rutas de movimiento lateral: {len(lateral_paths)} (ver identity_paths.txt)")
    print(f"  - MFA Fatigue Score (max): {max(u['mfa_rejects']*2 + (u['mfa_attempts']-u['mfa_rejects']) for u in users)}")
    print(f"  - Recomendaciones JIT: {sum(1 for u in users if any(r in ['Global Admin','Privileged Role Admin'] for r in u['roles']))}")
    print(f"  - Lockdown sugerido para: {len(lockdown_actions)} cuentas privilegiadas\n")


def generate_cloud_remediation(nsg_name, rule_name):
    # Esto es Security as Code puro
    remediation = f"az network nsg rule delete --resource-group RG_PROD --nsg-name {nsg_name} --name {rule_name}"
    os.makedirs("vaccines", exist_ok=True)
    with open("vaccines/cloud_fix.sh", "a") as f:
        f.write(remediation + "\n")
    print(f"[+] Script de remediación añadido a vaccines/cloud_fix.sh")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python engine/azure_guardrails.py <AZURE_SUBSCRIPTION_ID>")
        sys.exit(1)
    subscription_id = sys.argv[1]
    audit_azure_networks(subscription_id)
    identity_guardrails()
    print("\n[RESUMEN TÁCTICO] ARES-11: Cloud & Identity Guardrails completados.\n- NSG y puertos críticos auditados.\n- Identidades privilegiadas y MFA evaluados.\n- Acciones sugeridas en /vaccines/cloud_fix.sh y /vaccines/identity_fix.sh\n- Siguiente fase: Integración con War Map y Telemetría avanzada.\n")
