from functools import wraps


def debug(func):
    """decorator; debugs function when passed."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Full name of this method:", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    """class decorator to use debug method"""

    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


class DebugMeta(type):
    """meta class which feed created class object 
    to debugmethod to get debug functionality 
    enabled objects"""

    def __new__(mcs, clsname, bases, clsdict):
        obj = super().__new__(mcs, clsname, bases, clsdict)
        obj = debugmethods(obj)
        return obj


# now all the subclass of this
# will have debugging applied
class Base(metaclass=DebugMeta):
    pass


# inheriting Base
class Calc(Base):
    def add(self, x, y):
        return x+y


def main():

    calculator = Calc()

    print(calculator.add(2, 2))


if __name__ == "__main__":

    main()





