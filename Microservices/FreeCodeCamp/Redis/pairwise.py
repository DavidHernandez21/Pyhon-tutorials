import random
from itertools import pairwise

l = [random.randint(0, 100) for _ in range(10)]
# print(id(l))

for a, b in pairwise(l):
    # if a > b:
    print(a, b)

# print(id(l))
print(list(l))
