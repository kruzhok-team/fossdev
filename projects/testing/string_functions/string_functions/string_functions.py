def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    return text == text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def remove_whitespace(text):
    return "".join(text.split())

def remove_extra_spaces(text):
    words = text.split()
    return " ".join(words)

def text_to_lines(text, line_width):
    words = text.split()
    lines = []
    current_words = []
    for word in words:
        if not current_line:
            current_words.append(word)
        elif len(" ".join(current_words)) + len(word) + 1 <= line_width:
            current_words.append(word)
        else:
            lines.append(" ".join(current_words))
            current_words = [word]

    if current_words:
        lines.append(" ".join(current_words))

    return lines
