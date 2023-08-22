from typing import Callable


def contextmanager(func: Callable) -> Callable:
    class FuncContextManager:
        def __init__(self, *args, **kwargs):
            self.func_generator = func(*args, **kwargs)

        def __enter__(self):
            try:
                return next(self.func_generator)
            except StopIteration:
                raise RuntimeError("Generator didn't yield.")

        def __exit__(self, exc_type, exc_val, exc_tb):
            try:
                next(self.func_generator)
            except StopIteration:
                pass
            else:
                raise RuntimeError("Generator didn't stop.")

    return FuncContextManager


@contextmanager
def open_file(path, mode):
    file = open(path, mode)
    yield file
    file.close()


def main():
    text = "Hello world!"

    with open_file("test.txt", "w") as f:
        f.write(text)
        print(f'Wrote "{text}" to file.')

    with open_file("test.txt", "r") as f:
        print(f'Read "{f.read()}" from file.')


if __name__ == "__main__":
    main()
