import matplotlib.pyplot as plt

def plot_lines(data):
    plt.plot(data)
    plt.show()
    
def plot_dots(data):
    x = [x for x in range(len(data))]
    plt.scatter(x, data)
    plt.show()
