import threading
import queue
import time
import logging

logging.basicConfig(level=logging.INFO)

class EventBus:
    def __init__(self):
        self.queues = {}
        self.lock = threading.Lock()
        self.subscribers = {}

    def publish(self, event_type, payload):
        with self.lock:
            if event_type not in self.queues:
                self.queues[event_type] = queue.Queue()
            self.queues[event_type].put(payload)
            logging.info(f"[EventBus] Published {event_type}: {payload}")

    def consume(self, event_type, handler, max_retries=3):
        def worker():
            while True:
                try:
                    payload = self.queues[event_type].get()
                    retries = 0
                    while retries < max_retries:
                        try:
                            handler(payload)
                            break
                        except Exception as e:
                            retries += 1
                            logging.error(f"[EventBus] Handler error for {event_type}: {e} (retry {retries})")
                            time.sleep(1)
                    self.queues[event_type].task_done()
                except Exception as e:
                    logging.error(f"[EventBus] Consumer error: {e}")
        with self.lock:
            if event_type not in self.queues:
                self.queues[event_type] = queue.Queue()
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        self.subscribers.setdefault(event_type, []).append(t)

# Singleton instance
bus = EventBus()
