from infrastructure.storage.forensics_packager import package_forensics
from infrastructure.storage.report_generator import generate_pdf_report
import pytest

def test_package_forensics(tmp_path):
    evidence = tmp_path / "evidence.txt"
    evidence.write_text("test data")
    req = type("Req", (), {"evidence_paths": [str(evidence)], "output_zip": str(tmp_path / "out.zip")})
    result = package_forensics(req)
    assert result.output_zip.endswith("out.zip")

def test_generate_pdf_report(tmp_path):
    req = type("Req", (), {"findings": [{"ioc": "X", "severity": "alta"}], "attack_paths": [{"path": "A", "severity": "alta"}], "filename": str(tmp_path / "out.pdf")})
    result = generate_pdf_report(req)
    assert result.filename.endswith("out.pdf")
