import tracemalloc
import sys

def do_something_usefull(n):
    data = [1 for _ in range(n)]    
    return data
    
def execute_and_get_memory_usage(function, n):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    data = function(i)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
    return data 
    
for i in range(10):
    execute_and_get_memory_usage(do_something_usefull, i)
