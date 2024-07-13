from collections.abc import Generator
from functools import partial
from random import randint
from socket import socket


def roll_dice_simulator(dice_max_value: int = 6) -> Generator[int, None, None]:
    for die_roll in iter(lambda: randint(1, dice_max_value), dice_max_value):
        print(f'handling simulation: {die_roll}')
        yield die_roll


def from_input(exit_string: str = 'exit') -> Generator[str, None, None]:
    for user_str in iter(input, exit_string):
        yield user_str


def chunk_reader(chunk_size: int = 1024) -> Generator[bytes, None, None]:
    for block in iter(partial(socket.recv, chunk_size), b''):
        yield block


def main():
    exit_string = 'exit'
    print(f"Type '{exit_string}' to exit the program.")
    for user_str in from_input(exit_string=exit_string):
        print(f'User typed {user_str!r}.')

    dice_max_value = 6
    print(f'Simulation will run until random sample {dice_max_value} is thrown.')
    for die_roll in roll_dice_simulator(dice_max_value=dice_max_value):
        print()


if __name__ == '__main__':
    main()
