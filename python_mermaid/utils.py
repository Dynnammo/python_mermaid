from re import sub
from unidecode import unidecode


def snake_case(s: str):
    s = unidecode(s)

    s = s.replace("-", " ")
    s = s.replace("_", " ")

    s = sub(" ([A-Z]+)", r"_\1", s) # All caps word

    s = sub(" ([A-Z][a-z]+)", r"_\1", s) # Capitalized word

    s = sub("([a-z])([A-Z])", r"\1_\2", s) # Camel Case word

    s = sub("([A-Z])([A-Z])([a-z]+)", r"\1_\2\3", s) # words such as THESEWords

    s = sub("(  )", r"__", s) # Multiple spaces

    s = "_".join(s.split()).lower()

    return s


def sanitize_string(s: str) -> str:
    # fmt: off
    translation_table = str.maketrans({
        "\n": "/",
        "\t": "/",
        "\r": "",
        "(": "-",
        ")": "-"
    })
    # fmt: on
    return s.translate(translation_table)
