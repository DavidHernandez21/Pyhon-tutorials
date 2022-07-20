from dataclasses import dataclass
from functools import singledispatch


@dataclass
class Tea:
    kind: str
    temp: int


@dataclass
class Coffee:
    kind: str
    temp: int


@singledispatch
def boil(obj=None):
    raise NotImplementedError("No boiler instruction for this drink")


@boil.register(Coffee)
def _coffee_boil(obj):
    return "Successfully boiled coffee!"


@boil.register(Tea)
def _tea_boil(obj):
    return "Successfully boiled tea!"


def main():

    tea = Tea(kind="white tea", temp=93)
    coffee = Coffee(kind="Yunnan", temp=98)
    print(boil(tea))
    print(boil(coffee))


if __name__ == "__main__":

    main()
