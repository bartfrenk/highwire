import itertools
from highwire.samplers import MovingAverage


def cycle(xs):
    it = itertools.cycle(xs)

    def fn():
        return next(it)

    return fn


class TestMovingAverage:
    def test_return_first_value_at_end_of_period(self):
        sampler = MovingAverage(10, cycle([1]))
        for _ in range(9):
            assert sampler() is None
        assert sampler() == 1

    def test_moving_average_of_constant_sequence_is_constant(self):
        sampler = MovingAverage(10, cycle([1]))
        for _ in range(9):
            sampler.sample()
        for _ in range(9):
            assert sampler() == 1

    def test_moving_average_of_non_constant_sequence(self):
        sampler = MovingAverage(2, cycle([1, 2, 3, 4, 5, 6]))
        sampler.sample()
        assert sampler() == 1.5
        assert sampler() == 2.5
        assert sampler() == 3.5
        assert sampler() == 4.5
        assert sampler() == 5.5
        assert sampler() == 3.5
