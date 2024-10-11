from __future__ import annotations
from collections import deque
from typing import *  # type: ignore
from highwire.variables import R, S, T
from dataclasses import dataclass


@dataclass
class Event(Generic[S]):
    value: S
    time: int
    metadata: Optional[MutableMapping[str, Any]] = None

    def replace(self, value: T) -> Event[T]:
        return Event(value=value, time=self.time, metadata=self.metadata)


Project = Callable[[Event[S]], T]
Select = Callable[[Event[S], Event[S]], Event[S]]
Fold = Callable[[T, Event[S]], T]


def project(event: Event[R], fn: Project[R, S]) -> Event[S]:
    return Event(value=fn(event), time=event.time)


class Queue(Generic[S]):

    _events: Deque[Event[S]]

    def __init__(self):
        self._events = deque()

    def __len__(self):
        return len(self._events)

    def pop(self) -> Optional[Event[S]]:
        try:
            return self._events.popleft()
        except IndexError:
            return None

    def head(self) -> Optional[Event[S]]:
        try:
            return self._events[0]
        except IndexError:
            return None

    def take(self, before: int) -> List[Event[S]]:
        head = self.pop()
        dropped = []
        while head and head.time < before:
            dropped.append(head)
            head = self.pop()
        if head is not None:
            self._events.appendleft(head)
        return dropped

    def remove(self, before: int) -> None:
        self.take(before)

    def append(self, event: Event[S]):
        self._events.append(event)

    def __iter__(self) -> Iterator[Event[S]]:
        return iter(self._events)
