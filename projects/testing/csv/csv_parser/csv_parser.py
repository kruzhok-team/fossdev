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
