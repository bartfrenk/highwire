import itertools
from highwire.samplers import MovingAverage
from highwire.events import Event


def cycle(xs):
    it = itertools.cycle(xs)

    def fn():
        return next(it)

    return fn


class TestMovingAverage:
    def test_return_first_value_at_end_of_period(self):
        tick = Event(value=None, time=0)
        sampler = MovingAverage(10, cycle([1]))
        for _ in range(9):
            sampler.sample(tick)
            assert sampler.get() is None
        sampler.sample(tick)
        assert sampler.get() == 1

    def test_moving_average_of_constant_sequence_is_constant(self):
        tick = Event(value=None, time=0)
        sampler = MovingAverage(10, cycle([1]))
        for _ in range(9):
            sampler.sample(tick)
        for _ in range(9):
            sampler.sample(tick)
            assert sampler.get() == 1

    def test_moving_average_of_non_constant_sequence(self):
        tick = Event(value=None, time=0)
        sampler = MovingAverage(2, cycle([1, 2, 3, 4, 5, 6]))
        sampler.sample(tick)
        sampler.sample(tick)
        assert sampler.get() == 1.5
        sampler.sample(tick)
        assert sampler.get() == 2.5
        sampler.sample(tick)
        assert sampler.get() == 3.5
        sampler.sample(tick)
        assert sampler.get() == 4.5
        sampler.sample(tick)
        assert sampler.get() == 5.5
        sampler.sample(tick)
        assert sampler.get() == 3.5


class TestDifferenceOfMovingAverages:
    # TODO
    def test_difference_is_none_when_operand_is_none(self):
        tick = Event(value=None, time=0)
        x = MovingAverage(2, cycle([1]))
        y = MovingAverage(3, cycle([1]))
        z = x - y
        x.sample(tick)
        x.sample(tick)
        assert x.get() == 1
        assert z.get() is None

    def test_difference_moves_with_sample(self):
        tick = Event(value=None, time=0)
        x = MovingAverage(2, cycle([1, 2, 3]))
        y = MovingAverage(3, cycle([1, 2, 3, 4]))
        z = x - y
        for _ in range(2):
            x.sample(tick)
        for _ in range(3):
            y.sample(tick)
        assert z.get() == -0.5
        x.sample(tick)
        assert z.get() == 0.5
        y.sample(tick)
        assert z.get() == -0.5
        x.sample(tick)
        assert z.get() == -1
