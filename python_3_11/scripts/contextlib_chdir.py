import contextlib
import os

# working directory is a global property of the process
# so this is not thread safe/ async safe

print(os.getcwd())

with contextlib.chdir('..'):
    print(os.getcwd())

print(os.getcwd())
