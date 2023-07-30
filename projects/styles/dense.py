capacity = [(j * 8, 256**j-1) for j in (1 << i for i in range(4))]
print("\n".join("%i bits can store number up to %i" % bc for bc in capacity))
