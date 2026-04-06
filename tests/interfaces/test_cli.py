import subprocess
import sys

def test_cli_help():
    result = subprocess.run([sys.executable, "interfaces/cli/ares11.py", "--help"], capture_output=True, text=True)
    assert "Usage" in result.stdout or "usage" in result.stdout
