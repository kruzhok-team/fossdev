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
