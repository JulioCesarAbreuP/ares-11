import pytest
from core.contracts import *
from pydantic import ValidationError

def test_contract_validation():
    # Ejemplo: validar un contrato genérico
    contract = SomeContract(field="valor")
    assert contract.field == "valor"
    with pytest.raises(ValidationError):
        SomeContract(field=None)

def test_contract_type_enforcement():
    with pytest.raises(ValidationError):
        SomeContract(field=123)  # Debe ser str

def test_nested_contract_validation():
    class NestedContract(SomeContract):
        subfield: str
    obj = NestedContract(field="ok", subfield="sub")
    assert obj.subfield == "sub"
    with pytest.raises(ValidationError):
        NestedContract(field="ok", subfield=None)

def test_event_contract_validation():
    from core.events import EventContract
    event = EventContract(event_type="test", payload={"foo": 1})
    assert event.event_type == "test"
    with pytest.raises(ValidationError):
        EventContract(event_type=None, payload={})
