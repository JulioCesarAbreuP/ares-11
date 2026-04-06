
import logging
import functools
import uuid
import time
from typing import Any, Callable, TypeVar, Dict

logger = logging.getLogger("ares11")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)

T = TypeVar('T')

def log_event(event_type: str, data: Any, context: Dict = None):
    context = context or {}
    logger.info(f"EVENT: {event_type} | DATA: {data} | CONTEXT: {context}")

def trace(stage: str, event_id: str = None, correlation_id: str = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            eid = event_id or str(uuid.uuid4())
            cid = correlation_id or str(uuid.uuid4())
            logger.info(f"TRACE: Enter {func.__name__} | stage={stage} | event_id={eid} | correlation_id={cid}")
            start = time.time()
            try:
                result = func(*args, **kwargs)
                logger.info(f"TRACE: Exit {func.__name__} | duration={time.time()-start:.3f}s | event_id={eid}")
                return result
            except Exception as e:
                logger.error(f"TRACE: Error in {func.__name__} | {e} | event_id={eid}")
                raise
        return wrapper
    return decorator

def retry(retries: int = 3, delay: float = 1.0, fallback: Callable = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.warning(f"RETRY: {func.__name__} failed (attempt {attempt}/{retries}): {e}")
                    time.sleep(delay)
            if fallback:
                logger.warning(f"FALLBACK: Executing fallback for {func.__name__}")
                return fallback(*args, **kwargs)
            raise Exception(f"All retries failed for {func.__name__}")
        return wrapper
    return decorator

class CircuitBreaker:
    def __init__(self, max_failures=3, reset_timeout=60):
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.failures = 0
        self.last_failure = 0

    def call(self, func, *args, **kwargs):
        if self.failures >= self.max_failures and (time.time() - self.last_failure) < self.reset_timeout:
            logger.error(f"CIRCUIT BREAKER: Open for {func.__name__}")
            raise Exception("Circuit breaker open")
        try:
            result = func(*args, **kwargs)
            self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            self.last_failure = time.time()
            logger.error(f"CIRCUIT BREAKER: Failure in {func.__name__}: {e}")
            raise

class ValidationError(Exception):
    pass

def validate_contract(contract_cls, data):
    try:
        return contract_cls(**data)
    except Exception as e:
        logger.error(f"Validation error: {e}")
        raise ValidationError(str(e))

def sanitize_input(data: Any) -> Any:
    # Hook para sanitización de inputs (puede ampliarse)
    if isinstance(data, str):
        return data.replace("<", "&lt;").replace(">", "&gt;")
    return data

def dlp_hook(data: Any):
    # Hook para Data Loss Prevention (DLP)
    logger.info(f"DLP: Revisando datos para fuga de información")
    # Implementar lógica real aquí
    return True

def worm_hook(file_path: str):
    # Hook para WORM (Write Once Read Many)
    logger.info(f"WORM: Protegiendo archivo {file_path}")
    # Implementar lógica real aquí
    return True
