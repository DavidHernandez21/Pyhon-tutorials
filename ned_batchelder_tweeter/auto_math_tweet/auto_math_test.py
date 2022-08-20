import random

import auto_math
import pytest
from auto_math import valid_ops


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param(
            ('plus_10', 5),
            15,
            id='parsing the number after the first underscore as an int',
        ),
    ],
)
def test_int_parsing(test_input, expected):
    # assert auto_math.plus_10(test_input) == expected
    assert auto_math.__getattr__(test_input[0])(test_input[1]) == expected


@pytest.mark.parametrize(
    'test_input',
    [
        pytest.param(
            ('plus_t', 5),
            id='unable to parse the number after the first underscore as an int',
        ),
    ],
)
def test_int_parsing_error(test_input):
    # assert auto_math.plus_10(test_input) == expected
    with pytest.raises(ValueError):
        auto_math.__getattr__(test_input[0])(test_input[1])


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param(
            ('plus_10_5', 5),
            15.5,
            id='interpreting the number after the second underscore as the decimal part',
        ),
    ],
)
def test_float_parsing(test_input, expected):
    assert auto_math.__getattr__(test_input[0])(test_input[1]) == expected


@pytest.mark.parametrize(
    'test_input',
    [
        pytest.param(
            ('plus_4_t', 5),
            id='unable to parse the number after the second underscore as an int',
        ),
    ],
)
def test_float_parsing_error(test_input):
    # assert auto_math.plus_10(test_input) == expected
    with pytest.raises(ValueError):
        auto_math.__getattr__(test_input[0])(test_input[1])


@pytest.mark.parametrize(
    'test_input, expected',
    [
        pytest.param(
            ('plus_10_5_sfa_23535', 5),
            15.5,
            id='ignoring the arguments from the third underscore onwards',
        ),
    ],
)
def test_float_ignore_arguments_after_second_underscore(test_input, expected):
    assert auto_math.__getattr__(test_input[0])(test_input[1]) == expected


@pytest.mark.parametrize(
    'test_input',
    [pytest.param(5, id='operation not followed by an underscore and a number')],
)
def test_no_number_specified_after_operation(test_input):
    with pytest.raises(AttributeError):
        choice = random.choice(valid_ops)
        auto_math.__getattr__(choice)(test_input)


@pytest.mark.parametrize(
    'test_input',
    [pytest.param(5, id='invalid operation')],
)
def test_invalid_operation(test_input):
    with pytest.raises(AttributeError):
        auto_math.invalid(test_input)
