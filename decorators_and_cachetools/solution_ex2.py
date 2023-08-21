import timeit
from circular_dict import CircularDict
from functools import wraps


def memoize(cache_size: int = 100):    
    def decorator(func):
        cache = CircularDict(maxlen=cache_size)

        @wraps(func)
        def wrapper(*args, **kwargs):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]

        return wrapper
    return decorator


@memoize(10)
def fibo(n: int) -> int:
    """
    Calculate the n'th fibonacci number.
    """
    if n < 0:
        raise ValueError('n must be a positive integer')
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


def main():
    run_time = timeit.timeit('fibo(35)', globals=globals(), number=1)
    print(f"Run Time: {run_time}")


if __name__ == '__main__':
    main()
