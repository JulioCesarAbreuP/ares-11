# Integración de WORM Logger como microservicio
from engine.worm_logger import upload_worm_log

def check_health():
    try:
        upload_worm_log("logs/ai_gateway.log")
        return True
    except Exception:
        return False

def upload_log(log_path):
    return upload_worm_log(log_path)
