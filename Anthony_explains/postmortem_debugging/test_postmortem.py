from collections.abc import Iterable


def average(values: Iterable[float | int]) -> float:
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


def test_average() -> None:
    """Test the average function."""
    assert average([20, 30, 70]) == 50.0
