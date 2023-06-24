from time import sleep


def slow(num: int) -> int:
    sleep(0.5)
    return num


numbers = [7, 6, 1, 4, 1, 8, 0, 6]


# Using filter
# results = filter(lambda value: value > 0, (slow(num) for num in numbers))

# Using a double list comprehension
# results = [value for num in numbers for value in [slow(num)] if value > 0]

results = [value for num in numbers if (value := slow(num)) > 0]

print(results)
