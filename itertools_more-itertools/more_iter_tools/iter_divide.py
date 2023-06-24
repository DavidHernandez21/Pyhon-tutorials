from more_itertools import distribute
from more_itertools import divide

data = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh')

print([tuple(l) for l in divide(4, data)])

# If you don't care about order you should use distribute as it needs less memory.
print([tuple(l) for l in distribute(4, data)])
