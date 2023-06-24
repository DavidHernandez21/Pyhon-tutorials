import pathlib
import sys

for filename in sys.argv[1:]:
    path = pathlib.Path(filename)
    counts = [
        (text := path.read_text()).count('\n'),  # Number of lines
        len(text.split()),  # Number of words
        len(text),  # Number of characters
    ]
    print(*counts, path)
