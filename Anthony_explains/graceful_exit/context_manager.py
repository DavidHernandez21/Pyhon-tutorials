import signal
import time
from types import FrameType


class C:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('world')


class SigTerm(SystemExit):
    pass


def term_cb(signal: int, frame: FrameType) -> None:
    print(f'{frame=}')
    print(dir(frame))
    raise SigTerm(1)


with C():
    signal.signal(signal.SIGTERM, term_cb)
    time.sleep(100)
