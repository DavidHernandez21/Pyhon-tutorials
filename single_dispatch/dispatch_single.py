from functools import singledispatch
from decimal import Decimal
"""
When there is no registered implementation found, its MRO is used to find a more generic implementation. Hence the original function decorated is registered for the base object type, and is used if no other implementation is found.
"""

@singledispatch
def calc_num(num):
    raise NotImplementedError("cannot calculate for unknown number type")


@calc_num.register(int)
def calc_int(num):
    print(f"int: {num}")


@calc_num.register(float)
def calc_float(num):
    print(f"float: {num}")


"""
The decorator also supports decorator stacking, so we can create an overloaded function to handle multiple types.
"""


@calc_num.register(float)
@calc_num.register(Decimal)
def calc_float_or_decimal(num):
    print(f"float/decimal: {round(num, 2)}")


def main():

    calc_num(1)
    calc_num(1.0)
    calc_num(1.02324)
    # calc_num("num")
    calc_float_or_decimal(3.4454)


if __name__ == "__main__":

    main()