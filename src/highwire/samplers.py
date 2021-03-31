from collections import deque
from typing import Optional, Callable
from highwire.signals import Sampler, Tick
from highwire.variables import X


class MovingAverage(Sampler[X]):
    def __init__(self, n: int, fn: Callable[[], Optional[X]]):
        super().__init__()
        self._n = n
        self._buffer: deque = deque(maxlen=n)
        self._fn: Callable[[], Optional[X]] = fn

    def sample(self, tick: Optional[Tick] = None) -> None:
        val = self._fn()
        if val is not None:
            self._buffer.append(val)

    def get(self) -> Optional[X]:
        if len(self._buffer) == self._n:
            return sum(self._buffer) / self._n  # type: ignore
        return None
