
import pytest
from lib.palindrome import longest_palindromic_substring

def is_palindrome(sub):
    return sub == sub[::-1]


def brute_force_longest_palindrome_length(s):
    n = len(s)
    best = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            if is_palindrome(sub) and len(sub) > best:
                best = len(sub)
    return best


def assert_valid_palindrome_answer(s, result):
    assert isinstance(result, str)
    assert result in s, f"{result!r} is not a substring of {s!r}"
    assert is_palindrome(result), f"{result!r} is not a palindrome"
    expected_len = brute_force_longest_palindrome_length(s)
    assert len(result) == expected_len, (
        f"Expected longest palindrome length {expected_len}, "
        f"got {len(result)} ({result!r})"
    )


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


def test_single_character_z():
    assert longest_palindromic_substring("z") == "z"


def test_two_identical_characters():
    assert longest_palindromic_substring("aa") == "aa"


def test_two_different_characters():
    result = longest_palindromic_substring("ac")
    assert result in ("a", "c")
    assert len(result) == 1

def test_no_repeated_characters():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1
    assert result in "abcde"

def test_all_same_character_short():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_all_same_character_longer():
    assert longest_palindromic_substring("bbbbbbb") == "bbbbbbb"

def test_even_length_palindrome():
    assert longest_palindromic_substring("abba") == "abba"


def test_odd_length_palindrome():
    assert longest_palindromic_substring("abcba") == "abcba"


def test_nested_even_palindrome():
    assert longest_palindromic_substring("aabbaa") == "aabbaa"

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

def test_numeric_palindrome():
    assert longest_palindromic_substring("12321") == "12321"


def test_mixed_alphanumeric_palindrome():
    s = "123abccba321"
    result = longest_palindromic_substring(s)
    assert_valid_palindrome_answer(s, result)

def test_case_sensitivity_not_treated_as_equal():
    result = longest_palindromic_substring("Aba")
    assert is_palindrome(result)
    assert len(result) == 1

def test_long_string_all_same_character():
    s = "a" * 1000
    assert longest_palindromic_substring(s) == s


def test_long_string_completes_without_crashing():
    s = "ab" * 500  # length 1000, minimal repetition to avoid trivial case
    result = longest_palindromic_substring(s)
    assert isinstance(result, str)
    assert is_palindrome(result)
    assert result in s

def test_empty_string_returns_empty_string():
    assert longest_palindromic_substring("") == ""


def test_none_input_raises_type_error():
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)


def test_integer_input_raises_type_error():
    with pytest.raises(TypeError):
        longest_palindromic_substring(12321)