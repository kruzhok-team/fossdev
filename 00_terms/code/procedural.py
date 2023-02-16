def average_age(table):
    average = 0
    count = 0
    for item in table:
        average = average + item[1] 
        count = count + 1 
    return average / count

workers = [("Ivan", 24), ("Mary", 20), ("Alex", 21), ("Sara", 29)]
print("Average age:", average_age(workers))
