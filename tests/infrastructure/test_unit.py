import pytest
from infrastructure.storage.worm_logger import upload_worm_log
from infrastructure.storage.forensics_packager import package_forensics
from infrastructure.storage.report_generator import generate_pdf_report
from infrastructure.api.notifier import notify_telegram

def test_worm_logger():
    upload_worm_log("test.log")
    # No debe lanzar excepción

def test_forensics_packager():
    result = package_forensics({"evidence_paths": ["test.log"], "output_zip": "test.zip"})
    assert "output_zip" in result

def test_report_generator():
    result = generate_pdf_report({"findings": [], "attack_paths": [], "filename": "test.pdf"})
    assert "filename" in result

def test_notifier():
    result = notify_telegram({"message": "test", "bot_token": "token", "chat_id": "id"})
    assert result["success"]
