from typing import TypeVar, Optional
from highwire.streams import keyed_merge
from highwire.events import Event


X = TypeVar("X")


def constant_stream(x: X, delay: int, n: Optional[int] = None):
    def it():
        k = 0
        while True:
            if n is not None and k >= n:
                return
            yield Event(value=x, occurred_at=k * delay, received_at=k * delay)
            k += 1

    return it()


def event(value: X, time: int):
    return Event(value=value, occurred_at=time, received_at=time)


class TestKeyedMerge:
    def test_single_stream_with_tick(self):
        stream = keyed_merge({"x": constant_stream("x", 6)}, ("tick", 2))
        assert next(stream) == ("x", event("x", 0))
        assert next(stream) == ("tick", event(None, 2))
        assert next(stream) == ("tick", event(None, 4))
        assert next(stream) == ("x", event("x", 6))
        assert next(stream) == ("tick", event(None, 6))
        assert next(stream) == ("tick", event(None, 8))
