from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable


def retry_on_exception(retries: int = 3, delay_seconds: float = 0.15):
    def decorator(func: Callable[..., Any]):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:  # pragma: no cover
                    last_error = exc
                    if attempt == retries:
                        raise
                    time.sleep(delay_seconds * attempt)
            raise RuntimeError(f"Retry failed: {last_error}")

        return wrapper

    return decorator
