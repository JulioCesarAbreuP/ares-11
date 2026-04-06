import pytest
from core.contracts import *
from core.events import EventBus
from core.utils import *

def test_contracts_validation():
    # Prueba de validación de contratos Pydantic
    data = AnomalyInput(ip="192.168.1.1", ...)
    assert data.ip == "192.168.1.1"

def test_event_bus_publish():
    # Prueba de publicación de eventos
    bus = EventBus()
    bus.publish("test.event", {"foo": "bar"})
    # No debe lanzar excepción

def test_log_event():
    # Prueba de logs estructurados
    log_event("test.log", {"msg": "ok"})
    # No debe lanzar excepción
