import atexit


def square(x: float) -> float:
    return x * x


def run_last_function(func, x: float):
    print('daje')

    print(func(x))


def main():
    x = 3
    atexit.register(run_last_function, func=square, x=x)
    x = 2
    print(square(x=x))


if __name__ == '__main__':
    main()
