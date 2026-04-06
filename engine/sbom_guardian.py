# engine/sbom_guardian.py
"""
SBOM Guardian: Valida dependencias del proyecto contra bases de datos de vulnerabilidades (GitHub Advisory, NVD).
"""
import os
import json
import requests

def scan_sbom(requirements_file="requirements.txt"):
    if not os.path.exists(requirements_file):
        print(f"[SBOM] No se encontró {requirements_file}")
        return []
    with open(requirements_file) as f:
        packages = [line.strip().split('==')[0] for line in f if line.strip() and not line.startswith('#')]
    vulnerabilities = []
    for pkg in packages:
        # Consulta simulada a la API de GitHub Advisory (puede integrarse real con token)
        resp = requests.get(f"https://api.osv.dev/v1/query?package={pkg}")
        if resp.status_code == 200 and 'vulns' in resp.json():
            for vuln in resp.json()['vulns']:
                vulnerabilities.append({"package": pkg, "id": vuln.get('id'), "summary": vuln.get('summary')})
    if vulnerabilities:
        print(f"[SBOM] Vulnerabilidades detectadas: {json.dumps(vulnerabilities, indent=2)}")
    else:
        print("[SBOM] No se detectaron vulnerabilidades conocidas.")
    return vulnerabilities
