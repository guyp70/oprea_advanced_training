import contextlib
import sys
from io import StringIO

from typing import Iterator
from types import TracebackType
from typing import Optional, Type


class StdCapture:
    """Captures stdout in the given context."""

    def __init__(self, out: Optional[StringIO] = None) -> None:
        self.out = out or StringIO()

    def __enter__(self) -> None:
        """Replace stdout stream with new one."""
        self.original_out = sys.stdout
        sys.stdout = self.out

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Revert stdout to regular stream."""
        sys.stdout = self.original_out


@contextlib.contextmanager
def capture_stdout() -> Iterator[StringIO]:
    """Capture stdout in the given context."""
    old_stdout = sys.stdout
    capturer = StringIO()
    sys.stdout = capturer
    yield capturer
    sys.stdout = old_stdout
