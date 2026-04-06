import importlib

def check_all_services():
    services = [
        'ingest.sniffer_service',
        'analysis.anomaly_service',
        'analysis.correlation_service',
        'ai_layer.gateway_service',
        'ai_layer.decision_service',
        'enforcer.enforcer_service',
        'enforcer.annihilator_service',
    ]
    health = {}
    for svc in services:
        try:
            mod = importlib.import_module(svc)
            health[svc] = mod.check_health()
        except Exception as e:
            health[svc] = False
    return health

if __name__ == "__main__":
    print(check_all_services())
