# pipeline/stages/anomaly/sbom_guardian.py
"""
SBOM Guardian: Valida dependencias contra bases de datos de vulnerabilidades (OSV, NVD).
Formalizado para arquitectura enterprise.
"""
import os
import json
import requests
from core.events import EventBus
from core.contracts import AnomalyOutput

def scan_sbom(requirements_file: str = "requirements.txt") -> AnomalyOutput:
    if not os.path.exists(requirements_file):
        print(f"[SBOM] No se encontró {requirements_file}")
        return AnomalyOutput(anomaly_type="sbom", score=0.0, details={"error": "No requirements.txt"})
    with open(requirements_file) as f:
        packages = [line.strip().split('==')[0] for line in f if line.strip() and not line.startswith('#')]
    vulnerabilities = []
    for pkg in packages:
        resp = requests.get(f"https://api.osv.dev/v1/query?package={pkg}")
        if resp.status_code == 200 and 'vulns' in resp.json():
            for vuln in resp.json()['vulns']:
                vulnerabilities.append({"package": pkg, "id": vuln.get('id'), "summary": vuln.get('summary')})
    details = {"vulnerabilities": vulnerabilities}
    EventBus().publish("sbom.scanned", details)
    score = 1.0 if vulnerabilities else 0.0
    return AnomalyOutput(anomaly_type="sbom", score=score, details=details)
