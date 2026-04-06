from typing import Callable, Dict, List, Any

class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, handler: Callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    def publish(self, event_type: str, data: Any):
        handlers = self._subscribers.get(event_type, [])
        for handler in handlers:
            try:
                handler(data)
            except Exception as e:
                # Punto de extensión para resiliencia/logs
                print(f"[EventBus] Error en handler de '{event_type}': {e}")
