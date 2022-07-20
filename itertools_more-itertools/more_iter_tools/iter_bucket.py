import more_itertools


class Cube:
    def __repr__(self) -> str:
        return "Cube"

    pass


class Circle:
    def __repr__(self) -> str:
        return "Circle"

    pass


class Triangle:
    def __repr__(self) -> str:
        return "Triangle"

    pass


shapes = [Circle(), Cube(), Circle(), Circle(), Cube(), Triangle(), Triangle()]
s = more_itertools.bucket(shapes, key=type)
print(list(s))
# s -> <more_itertools.more.bucket object at 0x7fa65323f210>
print(list(s[Cube]))
#  [<__main__.Cube object at 0x7f394a0633c8>, <__main__.Cube object at 0x7f394a063278>]
print(list(s[Circle]))
