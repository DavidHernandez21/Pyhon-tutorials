import logging
from contextlib import ContextDecorator
from dataclasses import dataclass
from dataclasses import field
from random import randint
from time import perf_counter
from time import sleep
from typing import Callable
from typing import ClassVar
from typing import Dict
from typing import Optional

# from functools import  wraps

logging.basicConfig(level=logging.DEBUG)


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    __slots__ = ('_start_time', 'name', 'text', 'logger')
    timers = {}

    def __init__(
        self,
        name=None,
        text='Elapsed time: {:0.4f} seconds',
        logger=print,
    ):
        self._start_time = None
        self.name = name
        self.text = text
        self.logger = logger

        # Add new named timers to dictionary of timers
        if name:
            self.timers.setdefault(name, 0)

    # Other methods are unchanged

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError('Timer is running. Use .stop() to stop it')

        self._start_time = perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError('Timer is not running. Use .start() to start it')

        elapsed_time = perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))
        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time


@dataclass()
class TimerDataclass(ContextDecorator):
    timers: ClassVar[Dict[str, float]] = {}
    name: Optional[str] = None
    text: str = 'Elapsed time: {:0.4f} seconds'
    logger: Optional[Callable[[str], None]] = print
    _start_time: Optional[float] = field(default=None, init=False, repr=False)

    def __post_init__(self):
        """Initialization: add timer to dict of timers"""
        if self.name:
            self.timers.setdefault(self.name, 0)

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError('Timer is running. Use .stop() to stop it')

        self._start_time = perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError('Timer is not running. Use .start() to start it')

        elapsed_time = perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))
        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time

    def __enter__(self):
        """Start a new timer as a context manager"""
        self.start()
        return self

    def __exit__(self, *exc_info):
        """Stop the context manager timer"""
        self.stop()

    # def __call__(self, func):
    #     """Support using Timer as a decorator"""
    #
    #     @wraps(func)
    #     def wrapper_timer(*args, **kwargs):
    #         with self:
    #             return func(*args, **kwargs)
    #
    #     return wrapper_timer


def main():
    """Print the 10 latest tutorials from Real Python"""
    t = TimerDataclass(name='download', logger=logging.debug)
    for tutorial_num in range(2):
        t.start()
        sleep(randint(1, 2))
        t.stop()
        # print(tutorial)

    download_time = TimerDataclass.timers['download']
    print(f'Downloaded 10 tutorials in {download_time:0.2f} seconds')
    print(t)


def main2():
    with TimerDataclass() as t:
        for num in range(-3, 3):
            sleep(0.5)
            print(f'1 / {num} = {1 / num:.3f}')
        print(t.timers)


def main3():
    @TimerDataclass(logger=logging.debug, name='my_func')
    def my_func():
        for num in range(1, 4):
            sleep(0.5)
            print(f'1 / {num} = {1 / num:.3f}')

    my_func()


if __name__ == '__main__':
    # main()
    main2()
    # main3()
