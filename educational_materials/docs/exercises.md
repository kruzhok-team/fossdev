## Задачи 

### Задача 1

Есть два модуля. Функции одного рассчитывают хэши и делают поиск дубликатов по ним. Функции второго заключаются в поиске дубликатов файлов. Напишите документацию к ним и сделайте автоматическую сборку при помощи Sphinx.

([код](/projects/docs/duplicate_finder.py)):

```python
#content of duplicate_finder.py
import hashlib

def calculate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def find_duplicates(lines):
    duplicates = {}
    for idx, line in enumerate(lines):
        line_hash = calculate_hash(line)
        if line_hash in duplicates:
            duplicates[line_hash].append(idx)
        else:
            duplicates[line_hash] = [idx]
    return duplicates
```

([код](/projects/docs/file_processor.py)):

```python
#content of file_processor.py

import os
from duplicate_hash import find_duplicates

def process_files(directory):
    duplicates_found = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                file_duplicates = find_duplicates(lines)
                for line_hash, line_numbers in file_duplicates.items():
                    if line_hash in duplicates_found:
                        duplicates_found[line_hash].append((filename, line_numbers))
                    else:
                        duplicates_found[line_hash] = [(filename, line_numbers)]
    return duplicates_found

if __name__ == "__main__":
    # Example usage
    directory_path = "example_files"  # Replace with your target directory path
    duplicates = process_files(directory_path)
    for line_hash, occurrences in duplicates.items():
        print(f"Hash: {line_hash}")
        for filename, line_numbers in occurrences:
            print(f" - File: {filename}, Line Numbers: {line_numbers}")
        print()
```

**Ответ**

Так как написание документации — творческий процесс и, в отличие от кода, нельзя сказать, что документация работает правильно, в качестве критериев для оценивания этого задания можно взять два:

    * после прочтения документации становится понятно, как использовать функцию;
    * после прочтения документации складывается представление о внутренней реализации функции.

### Задача 2

Напишите генератор для тестовых данных для функции поиска дубликатов, используя документацию к функциям. Предположим, что ее написали заранее. 

([код](/projects/docs/generator_docstring.py)):

```python 
def generate_unique_words(num_words, max_len):
    """
    Generate a list of unique words.

    This function generates a list of unique words with the specified 
    number of words (num_words) and maximum word length (max_len). 
    It uses a set to ensure uniqueness.

    Parameters:
        num_words (int): The number of unique words to generate.
        max_len (int): The maximum length of each word.

    Returns:
        list: A list of unique words.

    Example:
        >>> unique_words = generate_unique_words(num_words=20, max_len=8)
        >>> print(unique_words)
        ['ghijklmn', 'opqrst', 'abcd', 'uvwx', 'ef', 'yz', 'ij', 'klm', 'gh', 
         'nopq', 'rs', 'tuvw','jkl', 'defg', 'cde', 'ijk', 'lmn', 'mn', 'hi', 
         'pqrs']
    """
    pass

def generate_unique_lines(words, num_lines, max_words):
    """
    Generate a list of unique lines.

    Parameters:
        words (list): A list of unique words.
        num_lines (int): The number of unique lines to generate.
        max_words (int): The maximum number of words in each line.

    Returns:
        list: A list of unique lines.

    Example:
        >>> unique_words = ['ghijklmn', 'opqrst', 'abcd', 'uvwx', 'ef', 'yz', 
                            'ij', 'klm', 'gh', 'nopq', 'rs', 'tuvw', 'jkl', 
                            'defg', 'cde', 'ijk', 'lmn', 'mn', 'hi', 'pqrs']
        >>> unique_lines = generate_unique_lines(words=unique_words, num_lines=10, max_words=6)
        >>> print(unique_lines)
        ['pqrs ij ghi pqrs pqrs klm nopq', 'opqrst pqrs pqrs ij pqrs', 
         'klmnopqrs pqrs jkl ij ghi rs pqrs', 'jkl ij jkl defg pqrs ijk lmn', 
         'defg cde ghi opqrst pqrs klm pqrs', 'cde ghi klm ij', 'jkl jkl ijk klm', 
         'lmn pqrs opqrst', 'ijklmn ghi', 'rs']
    """
    pass

def generate_duplicates(lines, num_dup):
   """
    Generate duplicates and their positions. 

    Duplicates are placed in the end of input list. Duplicate positions
    should include atleast 2 values for every duplicate: original line 
    position and position of duplicates originated from this line).

    Parameters:
        lines (list): A list of unique lines.
        num_dup (int): The number of duplicates to generate.

    Returns:
        list: A list of unique lines extended with duplicates.
        dict: A dictionary containing positions of duplicates in the extended list.

    Example:
        >>> unique_lines = ['pqrs ij ghi pqrs pqrs klm nopq', 
                            'opqrst pqrs pqrs ij pqrs', 
                            'klmnopqrs pqrs jkl ij ghi rs pqrs', 
                            'jkl ij jkl defg pqrs ijk lmn', 
                            'defg cde ghi opqrst pqrs klm pqrs', 
                            'cde ghi klm ij', 'jkl jkl ijk klm', 
                            'lmn pqrs opqrst', 'ijklmn ghi', 'rs']
        >>> num_duplicates = 3
        >>> extended_lines, duplicates_positions = \
                generate_duplicates(lines=unique_lines, num_dup=num_duplicates)
        >>> print("Extended Lines:")
        >>> print(extended_lines)
        ['pqrs ij ghi pqrs pqrs klm nopq', 'opqrst pqrs pqrs ij pqrs', 
         'klmnopqrs pqrs jkl ij ghi rs pqrs', 'jkl ij jkl defg pqrs ijk lmn', 
         'defg cde ghi opqrst pqrs klm pqrs', 'cde ghi klm ij', 'jkl jkl ijk klm', 
         'lmn pqrs opqrst', 'ijklmn ghi', 'rs', 'klmnopqrs pqrs jkl ij ghi rs pqrs', 
         'cde ghi klm ij', 'ijklmn ghi']
        >>> print("\nPositions of Duplicates:")
        >>> print(duplicates_positions)
        {'klmnopqrs pqrs jkl ij ghi rs pqrs': [2, 10], 
         'cde ghi klm ij': [5, 11], 
         'ijklmn ghi': [9, 12]}
    """
    pass
```

**Ответ**

([код](/projects/docs/generator.py)):

```python
import random

def generate_unique_words(num_words, max_len):

    words = set()
    while len(words) < num_words:
        word_len = random.randint(1, max_len)
        word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(word_len))
        words.add(word)
    return list(words)

def generate_unique_lines(words, num_lines, max_words):
    lines = []
    while len(lines) < num_lines:
        line_words_count = random.randint(1, max_words)
        line_words = random.sample(words, line_words_count)
        line = ' '.join(line_words)
        if line not in lines:
            lines.append(line)
    return lines

def generate_duplicates(lines, num_dup):
    duplicates = random.sample(lines, num_dup)
    duplicates_positions = {}
    for idx, line in enumerate(lines):
        if line in duplicates:
            if line in duplicates_positions:
                duplicates_positions[line].append(idx)
            else:
                duplicates_positions[line] = [idx]

    # Extend the lines with duplicates
    extended_lines = lines + duplicates

    # Add duplicate positions for each duplicated line
    for line in duplicates_positions:
        occurrences = duplicates_positions[line]
        while len(occurrences) < 2:
            occurrences.append(random.choice(occurrences))

    return extended_lines, duplicates_positions

```

### Задача 3

Работайте в командах. Опишите и реализуйте функции для тестирования функций поиска дубликатов с помощью генератора. Сначала сделайте описание того, что вы хотите получить и какие условия (случаи) нужно реализовать, чтобы считать, что функции работают правильно. Поменяйтесь описанием с другой командой. 

Реализуйте описанное другой командой в коде. Передайте свою реализацию команде, которая делала описание, и обсудите с ней, правильно ли реализовано задуманное (ошибки в реализации могут быть как по причине неполной документации, так и по причине неправильного прочтения документации). 

Возьмите реализацию у команды, которой передавали свое описание, и также обсудите правильность реализации, но уже с позиции тех, кто предоставлял документацию.
