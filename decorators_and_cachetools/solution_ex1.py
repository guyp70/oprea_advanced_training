import timeit
from circular_dict import CircularDict
from functools import wraps


def memoize(func):
    """
    Memoize the results of a function call. (caches up to 100 latest results)
    """
    cache = CircularDict(maxlen=100)

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
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
