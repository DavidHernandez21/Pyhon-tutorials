import re
from functools import partial
from typing import Callable

PatternFinder = Callable[[re.Pattern, str, dict], dict]


def pattern_finder_only_digits(
    pattern: re.Pattern,
    text: str,
    dates_format_template: tuple,
) -> dict:
    m = pattern.search(text)
    if not m:
        raise ValueError('No date found')
    if len(m.groups()) < 3:
        raise ValueError('Not enough digits in the date extracted')

    return {
        the_format: m.expand(template) for the_format, template in dates_format_template
    }


def find_date_regex_expand(the_format: str, pattern_finder: PatternFinder) -> str:
    d = pattern_finder()
    if the_format not in d:
        raise ValueError('Invalid format')

    return d[the_format]


def main():
    dates_formats_template_tuple = (
        ('us', r'\1/\2/\3'),
        ('eu', r'\2/\1/\3'),
        ('iso', r'\3-\2-\1'),
    )

    text = 'Today is 08/20/2022'
    the_format = 'iso'

    pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    patter_finder = partial(
        pattern_finder_only_digits,
        pattern,
        text,
        dates_formats_template_tuple,
    )
    print(find_date_regex_expand(the_format, patter_finder))
    # print(find_date_regex_expand(text, the_format, pattern))


if __name__ == '__main__':
    main()
