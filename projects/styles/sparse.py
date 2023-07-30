capacity = list()
for i in range(4):
    j = 1 << i
    bits = j * 8
    max_val = 256**j - 1
    capacity.append((bits , max_val))

for bits, max_val in capacity:
    print("%i bits can store number up to %i" % (bits, max_val))
