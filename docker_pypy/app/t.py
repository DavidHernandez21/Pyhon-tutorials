# print([l * l for l  in range(10000)])
import timeit


def test():
    [l * l for l in range(10000)]


def main():
    test()


if __name__ == "__main__":
    runs = timeit.repeat(main, number=1000, repeat=100)
    print(sum(runs) / len(runs))
