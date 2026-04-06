from infrastructure.dlp.dlp_engine import dlp_scan, anonymize_pii

def test_dlp_scan_detects_pii():
    assert dlp_scan("123-45-6789") is True
    assert dlp_scan("user@example.com") is True
    assert dlp_scan("normal data") is False

def test_anonymize_pii():
    assert anonymize_pii("123-45-6789") == "[REDACTED]"
    assert anonymize_pii("user@example.com") == "[REDACTED]"
    assert anonymize_pii("normal data") == "normal data"
