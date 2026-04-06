from core.events import EventBus

def test_event_publish_and_consume():
    bus = EventBus()
    received = []
    def handler(event):
        received.append(event)
    bus.subscribe("test.event", handler)
    bus.publish("test.event", {"data": 123})
    assert received[0]["data"] == 123

def test_multiple_event_handlers():
    bus = EventBus()
    called = []
    bus.subscribe("multi.event", lambda e: called.append("a"))
    bus.subscribe("multi.event", lambda e: called.append("b"))
    bus.publish("multi.event", {})
    assert called == ["a", "b"]

def test_unsubscribed_event():
    bus = EventBus()
    # No handler suscrito, no error
    bus.publish("no.handler", {"x": 1})
