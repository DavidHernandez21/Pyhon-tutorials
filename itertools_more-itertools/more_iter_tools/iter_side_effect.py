from collections.abc import Iterable

import more_itertools

num_events = 0


def _increment_num_events(event: int):
    global num_events
    if event % 2 == 0:
        print(f'{event} is even')
        num_events += 1


# Iterator that will be consumed
events: Iterable[int] = iter(range(10))
event_iterator = more_itertools.side_effect(_increment_num_events, events)

more_itertools.consume(event_iterator)

print(num_events)
