# engine/notifier.py
"""
Envía notificaciones a Telegram (puede adaptarse a Slack/Teams).
"""
import requests

def notify_telegram(message, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        resp = requests.post(url, data=data, timeout=5)
        if resp.status_code == 200:
            print("[NOTIFY] Alerta enviada a Telegram.")
        else:
            print(f"[NOTIFY] Error enviando alerta: {resp.text}")
    except Exception as e:
        print(f"[NOTIFY] Excepción: {e}")
