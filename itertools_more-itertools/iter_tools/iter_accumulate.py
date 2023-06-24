import functools
import operator
from itertools import accumulate

data = (3, 4, 1, 3, 5, 6, 9, 0, 1)

print(list(accumulate(data, max)))  # running maximum
#  [3, 4, 4, 4, 5, 6, 9, 9, 9]

print(list(accumulate(range(1, 11), operator.mul)))

print(list(accumulate(range(1, 11), operator.add)))

# If you don't care about intermediate results, you could use functools.reduce (called fold in other languages),
#  which keeps only final value and is also more memory efficient.
print(functools.reduce(operator.add, range(1, 11)))
