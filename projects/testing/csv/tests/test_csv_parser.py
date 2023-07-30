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
