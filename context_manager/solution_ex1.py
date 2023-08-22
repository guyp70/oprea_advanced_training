from contextlib import contextmanager
from typing import IO, Any, Optional


@contextmanager
def open_file(path, mode):
    file = open(path, mode)
    yield file
    file.close()


class File(object):
    def __init__(self, path: str, mode: str) -> None:
        self.path = path
        self.mode = mode
        self.file = None  # type: Optional[IO[Any]]

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()


def main():
    text = "Hello world!"
    with open_file("test.txt", "w") as f:
        f.write(text)
        print(f'Wrote "{text}" to file.')

    with File("test.txt", "r") as f:
        print(f'Read "{f.read()}" from file.')


if __name__ == "__main__":
    main()
