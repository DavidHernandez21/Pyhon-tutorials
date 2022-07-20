from datetime import datetime
from datetime import timedelta

from more_itertools import partition

# import timeit

dates = (
    datetime.now() - timedelta(days=8),
    datetime.now() - timedelta(days=38),
    datetime.now() - timedelta(days=48),
    datetime.now() - timedelta(days=16),
    datetime.now() - timedelta(days=28),
    datetime.now() - timedelta(days=90),
)

is_old = lambda x: datetime.now() - x < timedelta(days=30)


def is_old_2(x):
    return datetime.now() - x < timedelta(days=30)


old, recent = partition(is_old_2, dates)
print(list(old))

print(list(recent))


# Split based on file extension
files = (
    "foo.jpg",
    "bar.exe",
    "baz.gif",
    "text.txt",
    "data.bin",
)

my_str: str

ALLOWED_EXTENSIONS = ("jpg", "jpeg", "gif", "bmp", "png")
is_allowed = lambda my_str: my_str.split(".")[1] in ALLOWED_EXTENSIONS


def is_allowed_2(x):
    return x.split(".")[1] in ALLOWED_EXTENSIONS


allowed, forbidden = partition(is_allowed_2, files)
print(list(allowed))
#  ['bar.exe', 'text.txt', 'data.bin']
print(list(forbidden))
