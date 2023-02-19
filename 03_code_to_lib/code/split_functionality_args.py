import tracemalloc
import sys

def do_something_usefull(n):
    data = [1 for _ in range(n)]    
    return data

def do_something_else_usefull(n, m, step=1):
    data = [[1 for _ in range(n)] for _ in range(0, m, step)]
    return data
    
def execute_and_get_memory_usage(function, *args, **kwargs):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    result = function(*args, **kwargs)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
    return result

print('1D example:')
execute_and_get_memory_usage(do_something_usefull, 10)

print('\n2D example:')
execute_and_get_memory_usage(do_something_else_usefull, 10, 10, step=2)
