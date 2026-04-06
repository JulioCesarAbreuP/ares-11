# infrastructure/api/notifier.py
"""
Envía notificaciones a Telegram (adaptable a Slack/Teams). Formalizado para arquitectura enterprise.
"""
import requests
from core.utils import log_event, trace, retry, sanitize_input
from core.contracts import NotificationRequest, NotificationResult

@trace(stage="notifier")
@retry(retries=2, delay=1.0)
def notify_telegram(request: NotificationRequest) -> NotificationResult:
    message = sanitize_input(request.message)
    bot_token = sanitize_input(request.bot_token)
    chat_id = sanitize_input(request.chat_id)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        resp = requests.post(url, data=data, timeout=5)
        if resp.status_code == 200:
            log_event("notify.success", {"platform": "telegram", "message": message}, context={"stage": "notifier"})
            print("[NOTIFY] Alerta enviada a Telegram.")
            return NotificationResult(success=True, platform="telegram", message=message)
        else:
            log_event("notify.error", {"platform": "telegram", "error": resp.text}, context={"stage": "notifier"})
            print(f"[NOTIFY] Error enviando alerta: {resp.text}")
            return NotificationResult(success=False, platform="telegram", message=message, error=resp.text)
    except Exception as e:
        log_event("notify.exception", {"platform": "telegram", "exception": str(e)}, context={"stage": "notifier"})
        print(f"[NOTIFY] Excepción: {e}")
        return NotificationResult(success=False, platform="telegram", message=message, error=str(e))
