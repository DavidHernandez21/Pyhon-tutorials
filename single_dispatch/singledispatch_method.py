from functools import singledispatchmethod
from dataclasses import dataclass

@dataclass
class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg


def main():

    negator = Negator()

    print(negator.neg(5))
    print(negator.neg(True))


if __name__ == "__main__":

    main()