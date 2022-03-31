# Exercise 2
import random
from functools import wraps, update_wrapper


# Functions can be passed in as parameters
def greet(name, printer=print):
    printer(f"Hi {name}!")


def tnirp(text: str):
    print(text[::-1])


# greet("PyCon", printer=tnirp)


# Functions can be dynamically defined (function factories)
def prefix_factory(prefix: str):
    def prefix_printer(text: str):
        print(f"{prefix}: {text}")
    return prefix_printer


debug = prefix_factory("DEBUG")

# print(debug)
# debug("Hi PyCon!")
# #greet("PyCon", printer=debug)


# We can pass in functions to function factories
def reverse_factory(func):
    @wraps(func)
    def reverse_caller(text):
        func(text[::-1])
    return reverse_caller


# reverse_print = reverse_factory(print)
# reverse_print("Hi PyCon!")
# reverse_tnirp = reverse_factory(tnirp)
# reverse_tnirp("Hi PyCon!")
# reverse_debug = reverse_factory(debug)
# reverse_debug("Hi Pycon!")


# reverse_factory is a decorator!
@reverse_factory
def greet(name):
    print(f"Hi {name}!")

# greet("David")


# Exercise 3
FUNCTIONS = {}


def register(func):
    FUNCTIONS[func.__name__] = func
    return func


def roll_dice():
    return random.randint(1, 6)


@register
def roll_dice():
    return random.randint(1, 6)


# print(FUNCTIONS)
# print(FUNCTIONS["roll_dice"])
# print(FUNCTIONS["roll_dice"]())


def do_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        first = func(*args, **kwargs)
        second = func(*args, **kwargs)
        return first, second
    return wrapper


@register
@do_twice
def roll_dice():
    return random.randint(1, 6)


# print(roll_dice())
# print(FUNCTIONS)


# print(roll_dice.__wrapped__) # You can access the original function through __wrapped__
# print(roll_dice.__wrapped__())


# Exercise 4
def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retrying ({e})")
    return wrapper


@retry
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


# print(only_roll_sixes())


# Use @retry for simple validation of input
@retry
def get_age():
    return int(input("How old are you? "))


# print(get_age())


def retry(exception):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    print(f"Retrying ({e})")
        return wrapper
    return decorator


@retry(ValueError)
def calculation():
    number = random.randint(-5, 5)
    if abs(1 / number) > 0.2:
        raise ValueError(number, abs(1 / number))
    return number


# print(calculation())


def max_retry_decorator(max_retries):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying ({e})")
            return func(*args, **kwargs)  # Add final call to raise error
        return wrapper
    return decorator


@max_retry_decorator(max_retries=2)
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


# print(only_roll_sixes())


# Keep state for decorators
def max_retries_state(max_retries):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_retries - wrapper.num_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying ({e})")
                    print(f"num of retries: {only_roll_sixes.num_retries}")
                    wrapper.num_retries += 1
            print(f"num of retries: {only_roll_sixes.num_retries}")
            return func(*args, **kwargs)
        wrapper.num_retries = 0
        return wrapper
    return decorator


@max_retries_state(max_retries=3)
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)
    return number


# print(only_roll_sixes())


class BeforeAndAfter:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print("BEFORE")
        value = self.func(*args, **kwargs)
        print("AFTER")
        return value


@BeforeAndAfter
def greet(name):
    print(f"Hi {name}!")


# print(greet("PyCon"))
# print(BeforeAndAfter(greet))
# print(type(greet))
# print(type(roll_dice))

def max_attempts_retry_class(max_retries: int):
    class Retry:
        def __init__(self, func):
            update_wrapper(self, func)
            self.func = func
            self.num_retries = 0

        def __call__(self, *args, **kwargs):
            for _ in range(max_retries - self.num_retries):
                try:
                    return self.func(*args, **kwargs)
                except Exception as e:
                    self.num_retries += 1
                    print(f"Retry attempt {self.num_retries}\t Retrying: ({e})")

            return f"max retries '{max_retries}' reached"

    return Retry


class RetryMaxAttempts:

    def __init__(self, func, max_retries: int = 2):
        update_wrapper(self, func)
        self.func = func
        self.num_retries = 0
        self.max_retries = max_retries

    def __call__(self, *args, **kwargs):
        for _ in range(self.max_retries - self.num_retries):
            try:
                return self.func(*args, **kwargs)
            except Exception as e:
                self.num_retries += 1
                print(f"Retry attempt {self.num_retries}\t Retrying: ({e})")

        return f"max retries '{self.max_retries}' reached"


class RetryMaxAttemptsWithParameters:

    def __init__(self, max_retries: int = 2):
        self.num_retries = 0
        self.max_retries = max_retries

    def __call__(self, func):

        # update_wrapper(self, func)
        @wraps(func)
        def decorated(*args, **kwargs):
            for _ in range(self.max_retries - self.num_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    self.num_retries += 1
                    print(f"Retry attempt {self.num_retries}\t Retrying: ({e})")

            return f"max retries '{self.max_retries}' reached"

        return decorated


# @max_attempts_retry_class(max_retries=2)
# @RetryMaxAttempts
@RetryMaxAttemptsWithParameters(max_retries=5)
def only_roll_sixes(max_number: int = 6):
    number = random.randint(1, max_number)
    if number != 6:
        raise ValueError(number)
    return number


print(only_roll_sixes(max_number=8))
# print(only_roll_sixes)
