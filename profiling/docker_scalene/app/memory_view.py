r = 1000000


def bytes_slice(r: int):
    """Slice using normal bytes"""
    word = b"A" * r
    for i in range(r):
        _ = word[:i]


def memoryview_slice(r: int):
    """Convert to a memoryview first."""
    word = memoryview(b"A" * r)
    for i in range(r):
        _ = word[:i]


def main(r: int):
    """Main function"""
    bytes_slice(r)
    memoryview_slice(r)


if __name__ == "__main__":
    main(r)
