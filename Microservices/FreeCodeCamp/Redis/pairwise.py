from itertools import pairwise
import random

l = [random.randint(0, 100) for _ in range(10)]

print(l)
for a, b in pairwise(l):
    # if a > b:
    print(a, b)