import contextlib
import sys
from typing import IO

class Error(Exception):
    pass


def output_line(
    s: str,
    stream: IO[str],
    *,
    filename: str | None = None
):
    with contextlib.ExitStack() as stack:
        streams = [stream]
        if filename is not None:
            streams.append(stack.enter_context(open(filename, 'w', encoding="utf-8")))
        
        for output_stream in streams:
            output_stream.write(f"{s}\n")


def main():
    output_line("Hello", sys.stdout)
    output_line("World", sys.stdout, filename="log.log")


if __name__ == "__main__":
    main()