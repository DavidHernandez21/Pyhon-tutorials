import more_itertools

lines = (
    "erhgedrgh",
    "erhgedrghed",
    "esdrhesdresr",
    "ktguygkyuk",
    "-------------",
    "srdthsrdt",
    "waefawef",
    "ryjrtyfj",
    "-------------",
    "edthedt",
    "awefawe",
)

print(list(more_itertools.split_at(lines, lambda x: '-------------' in x)))


print(list(more_itertools.split_at(range(10), lambda n: n % 2 == 1, maxsplit=3)))


print(list(more_itertools.split_at('abcdcba', lambda x: x == 'b', keep_separator=False)))
print(list(more_itertools.split_at('abcdcba', lambda x: x == 'b', keep_separator=True)))