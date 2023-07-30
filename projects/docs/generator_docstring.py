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
