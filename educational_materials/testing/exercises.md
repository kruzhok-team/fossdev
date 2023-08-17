## Задачи: 

### Задача 1

Напишите класс `Fraction`, который будет принимать числитель и знаменатель для создания экземпляра класса. Класс должен иметь методы для приведения дроби к простому виду `4/6 -> 2/3`, а также метод для определения дроби, наиболее близкой к иррационального числу (напомним, что иррациональное число нельзя представить в виде дроби). При поиске ближайшей к иррациональном числу дроби ограничьте знаменатель, чтобы он не превышал 100. Напишите тесты к этим функциям.

**Ответ**

([код](/projects/testing/fraction/fraction/fraction.py)):

```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = self._compute_gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def _compute_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def closest_ratio_to_irrational(self, irrational):
        closest_difference = float("inf")
        closest_numerator = 0
        closest_denominator = 0

        for denominator in range(1, 101):
            numerator = round(denominator * irrational)
            difference = abs(irrational - numerator / denominator)

            if difference < closest_difference:
                closest_difference = difference
                closest_numerator = numerator
                closest_denominator = denominator

        return closest_numerator, closest_denominator
```

Тесты


([код](/projects/testing/fraction/tests/test_fraction.py)):

```python
# test_fraction.py

from fraction import Fraction

def test_simplify():
    fraction = Fraction(6, 9)
    fraction.simplify()
    assert fraction.numerator == 2
    assert fraction.denominator == 3

def test_compute_gcd():
    fraction = Fraction(15, 25)
    gcd = fraction._compute_gcd(15, 25)
    assert gcd == 5

def test_closest_ratio_to_irrational():
    fraction = Fraction(7, 20)

    # Test with an irrational number of 0.3
    irrational_number = 0.3
    numerator, closest_denominator = fraction.closest_ratio_to_irrational(irrational_number)
    assert numerator == 3
    assert closest_denominator == 10

    # Test with an irrational number of 0.8
    irrational_number = 0.8
    numerator, closest_denominator = fraction.closest_ratio_to_irrational(irrational_number)
    assert numerator == 4
    assert closest_denominator == 5

    # Test with an irrational number of 0.5
    irrational_number = 0.5
    numerator, closest_denominator = fraction.closest_ratio_to_irrational(irrational_number)
    assert numerator == 1
    assert closest_denominator == 2

    # Test with an irrational number of 0.123456789
    irrational_number = 0.123456789
    numerator, closest_denominator = fraction.closest_ratio_to_irrational(irrational_number)
    assert numerator == 10
    assert closest_denominator == 81
```



### Задача 2

Напишите тесты для функций из модуля `string_functions.py`, которые проводят операции со строками.

([код](/projects/testing/string_functions/string_functions/string_functions.py)):

```python
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

```


**Ответ**

([код](/projects/testing/string_functions/tests/test_string_functions.py)):

```python
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
```

### Задача 3

Реализуйте функцию `parse_csv` (парсер данных в формате csv). csv (comma-separated-value) — табличный формат, когда значения каждой колонки разделяются запятой. Для реализации можно пользоваться библиотекой `csv` или написать все вручную. Основная цель этого задания — реализовать все случаи, которые покрыты тестами.

([код](/projects/testing/csv/tests/test_csv_parser.py)):

```python
def test_parse_csv_empty_string():
    csv_string = ""
    result = parse_csv(csv_string)
    assert result == []

def test_parse_csv_single_row():
    csv_string = "Name,Age,City\nJohn,30,New York"
    result = parse_csv(csv_string)
    expected = [{"Name": "John", "Age": "30", "City": "New York"}]
    assert result == expected

def test_parse_csv_multiple_rows():
    csv_string = "Name,Age,City\nJohn,30,New York\nAlice,25,Chicago"
    result = parse_csv(csv_string)
    expected = [
        {"Name": "John", "Age": "30", "City": "New York"},
        {"Name": "Alice", "Age": "25", "City": "Chicago"},
    ]
    assert result == expected

def test_parse_csv_missing_columns():
    csv_string = "Name,Age,City\nJohn,30"
    result = parse_csv(csv_string)
    expected = [{"Name": "John", "Age": "30", "City": ""}]
    assert result == expected

def test_parse_csv_trailing_comma():
    csv_string = "Name,Age,City\nJohn,30,New York,"
    result = parse_csv(csv_string)
    expected = [{"Name": "John", "Age": "30", "City": "New York"}]
    assert result == expected

def test_parse_csv_extra_whitespace():
    csv_string = "  Name  , Age , City  \n   John,  30  ,  New York"
    result = parse_csv(csv_string)
    expected = [{"Name": "John", "Age": "30", "City": "New York"}]
    assert result == expected

def test_parse_csv_empty_fields():
    csv_string = "Name,Age,City\nJohn,,New York\n,25,\nAlice,30,"
    result = parse_csv(csv_string)
    expected = [
        {"Name": "John", "Age": "", "City": "New York"},
        {"Name": "", "Age": "25", "City": ""},
        {"Name": "Alice", "Age": "30", "City": ""},
    ]
    assert result == expected

def test_parse_csv_with_quotes():
    csv_string = 'Name,Age,City\n"John",30,"New York"\n"Alice",25,"Chicago"'
    result = parse_csv(csv_string)
    expected = [
        {"Name": "John", "Age": "30", "City": "New York"},
        {"Name": "Alice", "Age": "25", "City": "Chicago"},
    ]
    assert result == expected
```

**Ответ**

([код](/projects/testing/csv/csv_parser/csv_parser.py)):

```python
import csv

def parse_csv(csv_string):
    data = []
    lines = csv_string.strip().split("\n")
    if not lines:
        return data

    reader = csv.reader(lines)
    header = next(reader)

    for row in reader:
        row_dict = {}
        for col_name, value in zip(header, row):
            row_dict[col_name] = value.strip()
        data.append(row_dict)

    return data
```

### Задача 4

Используйте класс калькулятор.

([код](/projects/testing/calculator/calculator/calculator.py)):

/home/artem/swdev/gitrepo/edu/toolchain

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
```

Напишите тесты, которые используют `@pytest.fixture` вместо того, чтобы создавать экземпляр класса внутри каждого теста.

**Ответ**

([код](/projects/testing/calculator/tests/test_calculator.py)):

```python
# test_calculator.py

import pytest
from calculator import Calculator

# Define the fixture to set up an instance of the Calculator class for testing
@pytest.fixture
def calculator_instance():
    return Calculator()

def test_add(calculator_instance):
    result = calculator_instance.add(3, 4)
    assert result == 7

def test_subtract(calculator_instance):
    result = calculator_instance.subtract(10, 5)
    assert result == 5

def test_multiply(calculator_instance):
    result = calculator_instance.multiply(2, 3)
    assert result == 6

def test_divide(calculator_instance):
    result = calculator_instance.divide(10, 2)
    assert result == 5

def test_divide_by_zero(calculator_instance):
    with pytest.raises(ValueError):
        calculator_instance.divide(10, 0)

def test_divide_float(calculator_instance):
    result = calculator_instance.divide(5, 0.1)
    assert result == pytest.approx(50)

if __name__ == '__main__':
    pytest.main()
```