import pytest

from python_mermaid.utils import snake_case


def test_one_lowercase_letter():
    assert snake_case("a") == "a"

def test_one_capital_letter():
    assert snake_case("A") == "a"

def test_one_word():
    assert snake_case("testing") == "testing"

def test_one_word_all_caps():
    assert snake_case("TESTING") == "testing"

def test_already_snake_case():
    assert snake_case("already_snake_case") == "already_snake_case"

def test_already_snake_case__fully_all_caps():
    assert snake_case("ALL_CAPS_SNAKE_CASE") == "all_caps_snake_case"

def test_camel_case():
    assert snake_case("camelCaseInput") == "camel_case_input"

def test_mixed_cases():
    assert snake_case("MIXEDCases mixedCases mixed_cases") == "mixed_cases_mixed_cases_mixed_cases"

def test_capitalized_word():
    assert snake_case("Capitalized") == "capitalized"

def test_mix_of_hyphens_underscores_spaces():
    assert snake_case("hyphenated-words spaced apart SNAKE_CASE_CONSTANT") == "hyphenated_words_spaced_apart_snake_case_constant"

def test_capital_letter_after_hyphen():
    assert snake_case("Capital-After-Hyphen") == "capital_after_hyphen"

def test_capital_letter_after_space():
    assert snake_case("Capital After Space") == "capital_after_space"

def test_capital_letter_after_underscore():
    assert snake_case("Capital_After_Underscore") == "capital_after_underscore"

def test_already_snake_case__partially_all_caps():
    assert snake_case("ALLCAPS_SURROUNDED_BY_UNDERSCORES_lowercase") == "allcaps_surrounded_by_underscores_lowercase"

def test_capitalized_mix_of_hyphens_underscores_spaces():
    assert snake_case("Capitalized-Hyphenated Capitalized Spaced Capitalized_Underscores") == "capitalized_hyphenated_capitalized_spaced_capitalized_underscores"

def test_multiple_underscores_in_a_row():
    assert snake_case("multiple__underscores") == "multiple__underscores"

def test_multiple_underscores_in_a_row__capital_after_underscore():
    assert snake_case("multiple__Underscores") == "multiple__underscores"
