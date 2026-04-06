from infrastructure.storage.worm_logger import upload_worm_log
import pytest

def test_upload_worm_log(tmp_path):
    log_file = tmp_path / "log.txt"
    log_file.write_text("log entry")
    result = upload_worm_log(str(log_file), "blobname")
    assert result is None or isinstance(result, str)
