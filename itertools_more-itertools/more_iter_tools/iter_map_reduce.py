from more_itertools import map_reduce
data = 'This sentence has words of various lengths in it, both short ones and long ones'.split()

# keyfunc = lambda x: len(x)
result = map_reduce(data, len)
print(result)
# defaultdict(None, {
#   4: ['This', 'both', 'ones', 'long', 'ones'],
#   8: ['sentence'],
#   3: ['has', 'it,', 'and'],
#   5: ['words', 'short'],
#   2: ['of', 'in'],
#   7: ['various', 'lengths']})

# valuefunc = lambda x: 1
result = map_reduce(data, len, lambda x: 1)
print(result)
# defaultdict(None, {
#   4: [1, 1, 1, 1, 1],
#   8: [1],
#   3: [1, 1, 1],
#   5: [1, 1],
#   2: [1, 1],
#   7: [1, 1]})

reducefunc = sum
result = map_reduce(data, len, lambda x: 1, sum)
print(result)