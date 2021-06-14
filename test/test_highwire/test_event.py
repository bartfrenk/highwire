from highwire.events import Event


class TestEvent:
    def test_replace_event_value(self):
        # pylint: disable=no-member
        event = Event(value=1, time=0)
        actual = event.replace(2)
        assert actual.value == 2
        assert actual.time == event.time
