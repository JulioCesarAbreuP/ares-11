# infrastructure/storage/forensics_packager.py
"""
Empaqueta logs, hallazgos y evidencia en un ZIP. Formalizado para arquitectura enterprise.
"""
import zipfile
import os
from core.utils import log_event, trace, retry, sanitize_input
from core.contracts import ForensicsPackageRequest, ForensicsPackageResult

@trace(stage="forensics_packager")
@retry(retries=2, delay=1.0)
def package_forensics(request: ForensicsPackageRequest) -> ForensicsPackageResult:
    evidence_paths = [sanitize_input(p) for p in request.evidence_paths]
    output_zip = sanitize_input(request.output_zip or 'ARES11-EVIDENCIA.zip')
    try:
        with zipfile.ZipFile(output_zip, 'w') as zipf:
            for path in evidence_paths:
                if os.path.exists(path):
                    if os.path.isfile(path):
                        zipf.write(path)
                    else:
                        for root, _, files in os.walk(path):
                            for file in files:
                                zipf.write(os.path.join(root, file))
        log_event("forensics.packaged", {"output_zip": output_zip, "evidence": evidence_paths}, context={"stage": "forensics_packager"})
        print(f"[FORENSICS] Evidencia empaquetada en {output_zip}")
        return ForensicsPackageResult(output_zip=output_zip, evidence=evidence_paths)
    except Exception as e:
        log_event("forensics.packager.error", str(e), context={"stage": "forensics_packager"})
        raise
