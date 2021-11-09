from copy import deepcopy

import pytest

from highwire.async_streams import window
from highwire.events import Event


class TestWindow:
    @pytest.mark.asyncio
    async def test_window_in_correct_order(self):
        async def stream(n):
            for i in range(n):
                yield Event(value=i, time=i)

        actual = []
        async for xs in window(stream(4), 2):
            actual.append(deepcopy(xs.value))
        assert actual == [[0, 1], [1, 2], [2, 3]]
