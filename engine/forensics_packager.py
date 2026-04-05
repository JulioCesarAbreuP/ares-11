# engine/forensics_packager.py
"""
Modo Forense: Empaqueta logs, hallazgos y evidencia en un ZIP.
"""
import zipfile
import os

def package_forensics(evidence_paths, output_zip='ARES11-EVIDENCIA.zip'):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for path in evidence_paths:
            if os.path.exists(path):
                if os.path.isfile(path):
                    zipf.write(path)
                else:
                    for root, _, files in os.walk(path):
                        for file in files:
                            zipf.write(os.path.join(root, file))
    print(f"[FORENSICS] Evidencia empaquetada en {output_zip}")
