import pytest
from highwire.signals import LastEvent, Crossing
from highwire.events import Event


class TestCrossing:
    def test_crossing_vanishes_when_signal_is_none(self):
        signal = LastEvent()
        crossing = Crossing(signal, 0)
        for _ in range(10):
            signal.update(Event(value=None, time=0))
            assert crossing.get() == 0

    def test_initial_value_of_crossing_is_none(self):
        signal = LastEvent()
        crossing = Crossing(signal, 0)
        assert crossing.get() is None

    def test_positive_when_increasing_past_threshold(self):
        signal = LastEvent()
        crossing = Crossing(signal, 0)
        signal.update(Event(value=-1, time=0))
        assert crossing.get() == 0
        signal.update(Event(value=1, time=1))
        assert crossing.get() == 1
        signal.update(Event(value=2, time=2))
        assert crossing.get() == 0
        signal.update(Event(value=2, time=3))
        assert crossing.get() == 0
        signal.update(Event(value=0, time=4))
        assert crossing.get() == 0

    def test_negative_when_increasing_past_threshold(self):
        signal = LastEvent()
        crossing = Crossing(signal, 0)
        signal.update(Event(value=1, time=0))
        assert crossing.get() == 0
        signal.update(Event(value=-1, time=1))
        assert crossing.get() == -1
        signal.update(Event(value=-2, time=2))
        assert crossing.get() == 0
        signal.update(Event(value=-2, time=3))
        assert crossing.get() == 0
        signal.update(Event(value=0, time=4))
        assert crossing.get() == 0

    @pytest.mark.parametrize(
        "xs",
        [
            [(0, 0), (1, 0), (2, 0), (-1, -1), (0, 0), (1, 1)],
            [(0, 0), (0, 0), (0, 0), (1, 0), (-1, -1), (1, 1), (-1, -1)],
        ],
    )
    def test_sequences(self, xs):
        signal = LastEvent()
        crossing = Crossing(signal, 0)
        for (t, (x, c)) in enumerate(xs):
            signal.update(Event(value=x, time=t))
            assert crossing.get() == c
