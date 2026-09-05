"""
Test suite for longest_palindromic_substring(s).

TDD approach: these tests are written BEFORE the function is implemented.
They should all FAIL initially (or error, since the function body is `pass`
and returns None). Once palindrome.py is implemented, all tests should pass.
"""

import pytest
from lib.palindrome import longest_palindromic_substring


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_palindrome(sub):
    """Return True if the given string reads the same forwards and backwards."""
    return sub == sub[::-1]


def brute_force_longest_palindrome_length(s):
    """
    Slow, obviously-correct reference implementation used ONLY to compute the
    expected max length for test assertions on small/ambiguous inputs.
    Not the solution under test -- just a way to avoid hardcoding wrong
    expectations in the test file itself.
    """
    n = len(s)
    best = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if is_palindrome(sub) and len(sub) > best:
                best = len(sub)
    return best


def assert_valid_palindrome_answer(s, result):
    """
    Shared assertion for cases where multiple correct answers exist.
    Confirms the result is:
      1. an actual substring of s
      2. a valid palindrome
      3. of the correct (maximum possible) length
    """
    assert isinstance(result, str)
    assert result in s, f"{result!r} is not a substring of {s!r}"
    assert is_palindrome(result), f"{result!r} is not a palindrome"
    expected_len = brute_force_longest_palindrome_length(s)
    assert len(result) == expected_len, (
        f"Expected longest palindrome length {expected_len}, "
        f"got {len(result)} ({result!r})"
    )


# ---------------------------------------------------------------------------
# Basic cases (from the assignment table)
# ---------------------------------------------------------------------------

def test_babad_returns_valid_palindrome():
    result = longest_palindromic_substring("babad")
    assert result in ("bab", "aba")


def test_cbbd_returns_bb():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_single_character_a():
    assert longest_palindromic_substring("a") == "a"


def test_ac_returns_valid_single_char():
    result = longest_palindromic_substring("ac")
    assert result in ("a", "c")


def test_racecar_entire_string_is_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


# ---------------------------------------------------------------------------
# Edge cases: single character / very short strings
# ---------------------------------------------------------------------------

def test_single_character_z():
    assert longest_palindromic_substring("z") == "z"


def test_two_identical_characters():
    assert longest_palindromic_substring("aa") == "aa"


def test_two_different_characters():
    result = longest_palindromic_substring("ac")
    assert result in ("a", "c")
    assert len(result) == 1


# ---------------------------------------------------------------------------
# Edge cases: no palindrome longer than one character
# ---------------------------------------------------------------------------

def test_no_repeated_characters():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1
    assert result in "abcde"


# ---------------------------------------------------------------------------
# Edge cases: all identical characters
# ---------------------------------------------------------------------------

def test_all_same_character_short():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_all_same_character_longer():
    assert longest_palindromic_substring("bbbbbbb") == "bbbbbbb"


# ---------------------------------------------------------------------------
# Edge cases: even-length vs odd-length palindromes
# ---------------------------------------------------------------------------

def test_even_length_palindrome():
    assert longest_palindromic_substring("abba") == "abba"


def test_odd_length_palindrome():
    assert longest_palindromic_substring("abcba") == "abcba"


def test_nested_even_palindrome():
    assert longest_palindromic_substring("aabbaa") == "aabbaa"


# ---------------------------------------------------------------------------
# Edge cases: palindrome not centered / surrounded by noise
# ---------------------------------------------------------------------------

def test_palindrome_embedded_in_longer_string():
    s = "aacabdkacaa"
    result = longest_palindromic_substring(s)
    assert_valid_palindrome_answer(s, result)


def test_palindrome_at_start_of_string():
    s = "abccbaxyz"
    result = longest_palindromic_substring(s)
    assert_valid_palindrome_answer(s, result)


def test_palindrome_at_end_of_string():
    s = "xyzabccba"
    result = longest_palindromic_substring(s)
    assert_valid_palindrome_answer(s, result)


# ---------------------------------------------------------------------------
# Edge cases: numeric strings (constraint allows digits)
# ---------------------------------------------------------------------------

def test_numeric_palindrome():
    assert longest_palindromic_substring("12321") == "12321"


def test_mixed_alphanumeric_palindrome():
    s = "123abccba321"
    result = longest_palindromic_substring(s)
    assert_valid_palindrome_answer(s, result)


# ---------------------------------------------------------------------------
# Edge cases: case sensitivity
# ---------------------------------------------------------------------------

def test_case_sensitivity_not_treated_as_equal():
    # 'A' and 'a' are different characters, so "Aba" is not a full palindrome.
    # The longest valid palindrome here is "b" (or "A"/"a" individually).
    result = longest_palindromic_substring("Aba")
    assert is_palindrome(result)
    assert len(result) == 1


# ---------------------------------------------------------------------------
# Edge cases: long strings (upper end of constraint, 1 <= len(s) <= 1000)
# ---------------------------------------------------------------------------

def test_long_string_all_same_character():
    s = "a" * 1000
    assert longest_palindromic_substring(s) == s


def test_long_string_completes_without_crashing():
    # Not asserting a specific value here -- just confirming the function
    # can handle the upper constraint boundary without error or timeout.
    s = "ab" * 500  # length 1000, minimal repetition to avoid trivial case
    result = longest_palindromic_substring(s)
    assert isinstance(result, str)
    assert is_palindrome(result)
    assert result in s


# ---------------------------------------------------------------------------
# Error handling / out-of-spec input
#
# The stated constraints are 1 <= len(s) <= 1000, using only digits and
# English letters. The cases below go outside that spec on purpose, to
# document expected behavior for inputs a caller might still pass in.
# ---------------------------------------------------------------------------

def test_empty_string_returns_empty_string():
    # Design decision: rather than raising an exception for an empty string,
    # we expect the function to degrade gracefully and return "".
    assert longest_palindromic_substring("") == ""


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)


def test_integer_input_raises_type_error():
    with pytest.raises(TypeError):
        longest_palindromic_substring(12321)