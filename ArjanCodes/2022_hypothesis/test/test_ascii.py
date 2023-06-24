from example import from_ascii_codes
from example import to_ascii_codes
from hypothesis import given
from hypothesis.strategies import text


@given(text())
def test_decode_inverts_encode(test_str: str):
    assert from_ascii_codes(to_ascii_codes(test_str)) == test_str


@given(text())
def test_list_length(test_str: str):
    encoded = to_ascii_codes(test_str)
    assert len(encoded) == len(test_str)
