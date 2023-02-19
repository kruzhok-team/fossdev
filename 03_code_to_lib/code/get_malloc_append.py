import tracemalloc
import sys

data = list()
print(f"According to sys: {sys.getsizeof(data)}")
for i in range(10):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    data.append(1)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: {after[1] - before[1]}")
    print(f"According to sys: {sys.getsizeof(data)}")
