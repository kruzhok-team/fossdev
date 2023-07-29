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
