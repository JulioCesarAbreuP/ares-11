import datetime

def log(message: str) -> None:
    timestamp = datetime.datetime.utcnow().isoformat()
    print(f"[{timestamp}] [ARES-11] {message}")
