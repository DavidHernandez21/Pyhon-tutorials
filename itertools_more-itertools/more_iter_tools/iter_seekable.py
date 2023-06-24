from more_itertools import seekable

data = 'This is example sentence for seeking back and forth'.split()

it = seekable(data)
for _ in it:
    ...

try:
    next(it)
except StopIteration as e:
    print(f'End of iteration: {type(e).__name__}')
# StopIteration
it.seek(3)
print(next(it))
