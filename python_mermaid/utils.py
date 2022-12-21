from re import sub
from unidecode import unidecode


def snake_case(s):
    s = unidecode(s)
    s = '_'.join(
        sub(
            '([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1', s.replace('-', ' '))
        ).split()
    ).lower()

    return s
