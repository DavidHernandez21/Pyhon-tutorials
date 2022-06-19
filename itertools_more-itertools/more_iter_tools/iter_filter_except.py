from more_itertools import filter_except

data = ('1.5', '6', 'not-important', '11', '1.23E-7', 'remove-me', '25', 'trash')

print(tuple(filter_except(float, data, TypeError, ValueError)))

print(tuple(map(float, filter_except(float, data, TypeError, ValueError))))
# list(map(float, filter_except(float, data, TypeError, ValueError)))