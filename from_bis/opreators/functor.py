from typing import Any, Callable, Union


class Functor:
    """
    This class represents a function.
    """

    def __init__(self, func: Callable) -> None:
        """
        Initializes a Functor instance.

        :param func: A function to wrap.
        """
        self._func = func

    def __call__(self, *args, **kwargs) -> Any:
        """
        Calls the function with it's arguments

        :return: Result of function execution using given args.
        """
        return self._func(*args, **kwargs)

    def __add__(self, other: Union['Functor', int]) -> 'Functor':
        """
        :param other: Function or number to add.
        :return: Functor instance which includes the new function.
        """
        if isinstance(other, Functor):
            return Functor(lambda *args, **kwargs: other(*args, **kwargs) + self(*args, **kwargs))
        elif isinstance(other, int):
            return Functor(lambda *args, **kwargs: (self(*args, **kwargs) + other))

        raise TypeError(f'Expected Functor or int, but got {type(other)} instead.')

    def __sub__(self, other: Union['Functor', int]) -> 'Functor':
        """
        :param other: Function or number to subtract from this function.
        :return: Functor instance which includes the new function.
        """
        if isinstance(other, Functor):
            return Functor(lambda *args, **kwargs: self(*args, **kwargs) - other(*args, **kwargs))
        elif isinstance(other, int):
            return Functor(lambda *args, **kwargs: (self(*args, **kwargs) - other))

        raise TypeError(f'Expected Functor or int, but got {type(other)} instead.')

    def __mul__(self, other: Union['Functor', int]) -> 'Functor':
        """
        :param other: Function or number to multiply this function by
        :return: Functor instance which includes the new function.
        """
        if isinstance(other, Functor):
            return Functor(lambda *args: self(other(*args)))
        elif isinstance(other, int):
            return Functor(lambda *args: (self(*args) * other))

        raise TypeError(f'Expected Functor or int, but got {type(other)} instead.')

    def __pow__(self, n: int) -> 'Functor':
        """
        Returns a new function that is the current function multiplied by itself n times.

        :param n: The number of times to execute this function.
        :return: Functor instance which includes the new function.
        """
        if isinstance(n, int):
            if n == 0:
                return Functor(lambda *args, **kwargs: 1)
            if n == 1:
                return self
            if n < 0:
                pow_function = self ** abs(n)
                return Functor(lambda *args, **kwargs: 1 / pow_function(*args, **kwargs))

            return self * (self ** (n - 1))

        raise TypeError(f'Expected int, but got {type(n)} instead.')
