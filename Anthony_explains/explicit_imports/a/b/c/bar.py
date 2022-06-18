import sys
print(sys.path)
from .foo import x
from .. import b
from ... import a



print(f'got {x=} from foo')

print(f'imported {a=} from a')


print(f'imported {b=} from b')
