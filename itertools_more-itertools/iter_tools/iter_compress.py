from itertools import compress

dates = (
    "2020-01-01",
    "2020-02-04",
    "2020-02-01",
    "2020-01-24",
    "2020-01-08",
    "2020-02-10",
    "2020-02-15",
    "2020-02-11",
)

counts = [1, 4, 3, 8, 0, 7, 9, 2]


bools = (n > 3 for n in counts)
print(list(compress(dates, bools)))