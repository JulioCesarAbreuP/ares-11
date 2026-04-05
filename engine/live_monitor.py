# engine/live_monitor.py
"""
Modo Live Monitor: Monitorea la red en tiempo real y alerta sobre nuevos dispositivos o escaneos.
"""
import time
from scanner.ecosystem_probe import audit_ecosystem
from engine.notifier import notify_telegram

def live_monitor(network_range, bot_token=None, chat_id=None, interval=60):
    known_hosts = set()
    while True:
        results = audit_ecosystem(network_range)
        current_hosts = set(results.keys())
        new_hosts = current_hosts - known_hosts
        if new_hosts:
            msg = f"[LIVE MONITOR] Nuevos dispositivos detectados: {', '.join(new_hosts)}"
            print(msg)
            if bot_token and chat_id:
                notify_telegram(msg, bot_token, chat_id)
        known_hosts = current_hosts
        time.sleep(interval)
