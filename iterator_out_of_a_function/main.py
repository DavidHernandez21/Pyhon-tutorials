from collections.abc import Generator
from functools import partial
from random import randint
from socket import socket


def roll_dice_simulator(dice_max_value: int = 6) -> Generator[int, None, None]:
    for die_roll in iter(lambda: randint(1, dice_max_value), dice_max_value):
        print(f"handling simulation: {die_roll}")
        yield die_roll


def from_input(exit_string: str = "exit") -> Generator[str, None, None]:
    yield from iter(input, exit_string)


def chunk_reader(chunk_size: int = 1024) -> Generator[bytes, None, None]:
    yield from iter(partial(socket.recv, chunk_size), b"")


def main():
    exit_string = "exit"
    print(f"Type '{exit_string}' to exit the program.")
    for user_str in from_input(exit_string=exit_string):
        print(f"User typed {user_str!r}.")

    dice_max_value = 6
    print(f"Simulation will run until random sample {dice_max_value} is thrown.")
    for die_roll in roll_dice_simulator(dice_max_value=dice_max_value):
        print(f"Random sample: {die_roll}")


if __name__ == "__main__":
    main()
