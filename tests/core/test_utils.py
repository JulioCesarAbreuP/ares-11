from core.utils import log_event, retry, trace, sanitize_input
import logging

def test_log_event(capsys):
    log_event("test.log", {"msg": "ok"})
    captured = capsys.readouterr()
    assert "test.log" in captured.out

def test_sanitize_input():
    assert sanitize_input("<script>") == "[sanitized]"
    assert sanitize_input("normal") == "normal"

def test_retry_decorator():
    calls = {'count': 0}
    @retry(retries=2, delay=0)
    def flaky():
        calls['count'] += 1
        if calls['count'] < 2:
            raise Exception('fail')
        return 'ok'
    assert flaky() == 'ok'

def test_trace_decorator():
    @trace(stage='test')
    def foo(x):
        return x + 1
    assert foo(1) == 2

def test_sanitize_input_edge_cases():
    assert sanitize_input(None) == None
    assert sanitize_input(123) == 123
    assert sanitize_input({"a": "<script>"}) == {"a": "[sanitized]"}
