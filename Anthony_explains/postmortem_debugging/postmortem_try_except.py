import sys
from collections.abc import Iterable
from typing import Union


def average(numbers: Iterable[Union[float, int]]) -> float:
    return sum(numbers) / len(numbers)


def real_main():
    print("enter some numbers, type 'done' when finished:")
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line == 'done':
            break

        numbers.append(line)

    # if not numbers:
    #     print("no numbers were entered")
    #     return
    print(f'The average is {average([float(n) for n in numbers])}')


def main():
    try:
        real_main()
    except Exception as e:
        import pdb

        pdb.post_mortem()
        print(f'unexpected error occurred: {type(e).__name__}:  {e}')
        # sys.exit(1)


if __name__ == '__main__':
    main()
