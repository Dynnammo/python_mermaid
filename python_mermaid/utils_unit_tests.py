#!/usr/bin/env python3

import unittest

from utils import snake_case


class SnakeCaseUnitTests(unittest.TestCase):
    def test_one_lowercase_letter(self):
        self.assertEqual(snake_case("a"), "a")

    def test_one_capital_letter(self):
        self.assertEqual(snake_case("A"), "a")

    def test_one_word(self):
        self.assertEqual(snake_case("testing"), "testing")

    def test_one_word_all_caps(self):
        self.assertEqual(snake_case("TESTING"), "testing")

    def test_already_snake_case(self):
        self.assertEqual(snake_case("already_snake_case"), "already_snake_case")

    def test_already_snake_case__fully_all_caps(self):
        self.assertEqual(snake_case("ALL_CAPS_SNAKE_CASE"), "all_caps_snake_case")

    def test_camel_case(self):
        self.assertEqual(snake_case("camelCaseInput"), "camel_case_input")

    def test_mixed_cases(self):
        self.assertEqual(
            snake_case("MIXEDCases mixedCases mixed_cases"),
            "mixed_cases_mixed_cases_mixed_cases",
        )

    def test_capitalized_word(self):
        self.assertEqual(snake_case("Capitalized"), "capitalized")

    def test_mix_of_hyphens_underscores_spaces(self):
        self.assertEqual(
            snake_case("hyphenated-words spaced apart SNAKE_CASE_CONSTANT"),
            "hyphenated_words_spaced_apart_snake_case_constant",
        )

    def test_capital_letter_after_hyphen(self):
        self.assertEqual(snake_case("Capital-After-Hyphen"), "capital_after_hyphen")

    def test_capital_letter_after_space(self):
        self.assertEqual(snake_case("Capital After Space"), "capital_after_space")

    def test_capital_letter_after_underscore(self):
        self.assertEqual(
            snake_case("Capital_After_Underscore"), "capital_after_underscore"
        )

    def test_already_snake_case__partially_all_caps(self):
        self.assertEqual(
            snake_case("ALLCAPS_SURROUNDED_BY_UNDERSCORES_lowercase"),
            "allcaps_surrounded_by_underscores_lowercase",
        )

    def test_capitalized_mix_of_hyphens_underscores_spaces(self):
        self.assertEqual(
            snake_case(
                "Capitalized-Hyphenated Capitalized Spaced Capitalized_Underscores"
            ),
            "capitalized_hyphenated_capitalized_spaced_capitalized_underscores",
        )

    def test_multiple_underscores_in_a_row(self):
        self.assertEqual(snake_case("multiple__underscores"), "multiple__underscores")

    def test_multiple_underscores_in_a_row__capital_after_underscore(self):
        self.assertEqual(snake_case("multiple__Underscores"), "multiple__underscores")

if __name__ == "__main__":
    unittest.main()
