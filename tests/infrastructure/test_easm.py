from infrastructure.network.easm import notify_easm
import pytest

def test_notify_easm_success():
    assert notify_easm("INC123", ["host1"]) is True

def test_notify_easm_failure():
    with pytest.raises(Exception):
        notify_easm("INC123", [])
