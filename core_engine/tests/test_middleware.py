from core_engine.middleware import anti_prompt_injection

def test_anti_prompt_injection():
    banner = "\x1b[31mSYSTEM PROMPT\x00"
    filtered = anti_prompt_injection(banner)
    assert '[FILTERED]' in filtered
