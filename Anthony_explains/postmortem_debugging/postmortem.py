# import numbers
import sys
from collections.abc import Iterable
from typing import Union


def average(numbers: Iterable[Union[float, int]]) -> float:
    return sum(numbers) / len(numbers)


def main():
    print("enter some numbers, type 'done' when finished:")
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line == "done":
            break

        numbers.append(line)

    if not numbers:
        print("no numbers were entered")
        return
    print(f"The average is {average([float(n) for n in numbers])}")


if __name__ == "__main__":
    main()
