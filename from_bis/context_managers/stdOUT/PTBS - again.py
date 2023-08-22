from typing import Any, Callable


def retry(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error running {func.__name__}:")
                print(e)

    return wrapper


def test_retry():
    g = 0

    @retry
    def divide_by_zero():
        nonlocal g
        t = g
        g = 1
        return 1 / t

    assert divide_by_zero() == 1
