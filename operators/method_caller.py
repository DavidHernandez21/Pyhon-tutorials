from operator import methodcaller

print(methodcaller('rjust', 12, '.')('some text'))
# "...some text"

column = ['data', 'more data', 'other value', 'another row']
print([methodcaller('rjust', 12, '.')(value) for value in column])
