import pytest
from interfaces.cli.ares11 import main
from interfaces.agents.anomaly_agent import handle_ingest
from interfaces.agents.correlation_agent import handle_anomaly
from interfaces.agents.external_surface_agent import handle_external_surface

def test_cli_main():
    # Simula llamada CLI
    try:
        main()
    except SystemExit:
        pass

def test_anomaly_agent():
    handle_ingest({"ip": "192.168.1.1"})
    # No debe lanzar excepción

def test_correlation_agent():
    handle_anomaly({"anomaly": True})
    # No debe lanzar excepción

def test_external_surface_agent():
    handle_external_surface("8.8.8.8")
    # No debe lanzar excepción
