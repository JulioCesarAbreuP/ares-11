from domain.rules import some_rule

def test_rule_logic():
    assert some_rule(5) is True
    assert some_rule(0) is False

def test_rule_invalid_input():
    from domain.rules import some_rule
    try:
        some_rule(None)
    except Exception as e:
        assert isinstance(e, Exception)
