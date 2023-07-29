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
