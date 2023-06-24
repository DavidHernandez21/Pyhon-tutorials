import random


def add(a, b):
    return a + b


def get_sum_of_list():
    return [random.randint(1, 100) + random.randint(1, 100) for _ in range(10000000)]


if __name__ == '__main__':
    l = get_sum_of_list()
