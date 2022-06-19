from datetime import datetime
from more_itertools import consecutive_groups

dates = (
    datetime(2020, 1, 15),
    datetime(2020, 1, 16),
    datetime(2020, 1, 17),
    datetime(2020, 2, 1),
    datetime(2020, 2, 2),
    datetime(2020, 2, 5)
)

# ordinal_dates = []
# for d in dates:
#     ordinal_dates.append(d.toordinal())

ordinal_dates = (d.toordinal() for d in dates)

groups = (tuple(map(datetime.fromordinal, group)) for group in consecutive_groups(ordinal_dates))
[print(group) for group in groups]