from collections import deque
from typing import Callable, Dict, List

from .events import Event
from .utils import log

EventHandler = Callable[[Event], None]

class Orchestrator:
    def __init__(self) -> None:
        self._handlers: Dict[str, List[EventHandler]] = {}
        self._queue: deque[Event] = deque()
        self._modules: list[object] = []

    def register_module(self, module: object) -> None:
        self._modules.append(module)
        if hasattr(module, "register"):
            module.register(self)
            log(f"Módulo registrado: {module.__class__.__name__}")

    def on(self, event_name: str, handler: EventHandler) -> None:
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)
        log(f"Handler registrado para evento: {event_name}")

    def emit(self, event: Event) -> None:
        log(f"Evento encolado: {event.name} {event.payload or {}}")
        self._queue.append(event)

    def process_events(self, max_events: int | None = None) -> None:
        processed = 0
        while self._queue and (max_events is None or processed < max_events):
            event = self._queue.popleft()
            handlers = self._handlers.get(event.name, [])
            log(f"Procesando evento: {event.name} con {len(handlers)} handler(s)")
            for handler in handlers:
                handler(event)
            processed += 1
