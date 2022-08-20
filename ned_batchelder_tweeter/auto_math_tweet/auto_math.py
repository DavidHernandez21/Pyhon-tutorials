# def __getattr__(name) -> int | float:
#     op, mun = name.split("_")
#     if op not in ("times", "plus", "minus", "divide", "power"):
#         raise AttributeError(f"No such operation -> '{op}'")
#     try:
#         num = int(mun)
#     except ValueError as error:
#         raise ValueError(f"Could not convert to number -> '{mun}'") from error
#     return {
#         "times": lambda x: x * num,
#         "plus": lambda x: x + num,
#         "minus": lambda x: x - num,
#         "divide": lambda x: x / num,
#         "power": lambda x: x ** num,
#     }[op]
from logging import warning

valid_ops = ('times', 'plus', 'minus', 'divide', 'power')


def __getattr__(name) -> int | float:
    match name.split('_'):
        case [op, number, deci, *rest] if op in valid_ops:
            try:
                if rest:
                    warning(f'ignoring {rest}')
                new_number = '.'.join((number, deci))
                num = float(new_number)
            except ValueError as error:
                raise ValueError(
                    f"Could not convert to number -> '{new_number}'",
                ) from error

        case [op, number] if op in valid_ops:
            try:
                num = int(number)
            except ValueError as error:
                raise ValueError(
                    f"Could not convert to number -> '{number}'",
                ) from error
        case [op] if op in valid_ops:
            raise AttributeError(f"missing number for operation  -> '{op}'")
        case _:
            raise AttributeError(f"No such operation -> '{op}'")

    return {
        'times': lambda x: x * num,
        'plus': lambda x: x + num,
        'minus': lambda x: x - num,
        'divide': lambda x: x / num,
        'power': lambda x: x**num,
    }[op]
