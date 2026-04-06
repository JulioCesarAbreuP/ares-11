from domain.models import SomeModel
from pydantic import ValidationError
import pytest

def test_model_fields():
    obj = SomeModel(field1="a", field2=2)
    assert obj.field1 == "a"
    assert obj.field2 == 2

def test_model_validation_error():
    with pytest.raises(ValidationError):
        SomeModel(field1=None, field2=None)
