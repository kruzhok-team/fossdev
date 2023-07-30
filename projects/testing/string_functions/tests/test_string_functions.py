from string_functions import (
    reverse_string,
    is_palindrome,
    count_vowels,
    remove_whitespace,
    remove_extra_spaces
)

def test_capitalize_string():
    result = capitalize_string("hello world")
    assert result == "Hello world"

def test_reverse_string():
    result = reverse_string("hello")
    assert result == "olleh"

def test_is_palindrome():
    assert is_palindrome("radar")
    assert not is_palindrome("python")

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Python is awesome") == 6

def test_remove_whitespace():
    result = remove_whitespace("  remove  whitespace  ")
    assert result == "removewhitespace"

def test_swap_case():
    result = swap_case("Hello, World!")
    assert result == "hELLO, wORLD!"

def test_remove_extra_spaces():
    result = remove_extra_spaces("   This    is   a   test  sentence.  ")
    assert result == "This is a test sentence."

def test_text_to_lines():
    # Test with a short input text and line width
    text = "Hello World!"
    line_width = 8
    result = text_to_lines(text, line_width)
    assert result == ["Hello", "World!"]

    # Test with a long input text and line width
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nonummy."
    line_width = 20
    result = text_to_lines(text, line_width)
    assert result == [
        "Lorem ipsum dolor",
        "sit amet,",
        "consectetur",
        "adipiscing elit. Sed",
        "nonummy."
    ]
    # Test with a word exceeding the line width
    text = "Supercalifragilisticexpialidocious"
    line_width = 10
    result = text_to_lines(text, line_width)
    assert result == ["Supercalifragilisticexpialidocious"]

    # Test with an empty input text
    text = ""
    line_width = 15
    result = text_to_lines(text, line_width)
    assert result == []

    # Test with a very small line width
    text = "This is a test"
    line_width = 1
    result = text_to_lines(text, line_width)
    assert result == ["This", "is", "a", "test"]
