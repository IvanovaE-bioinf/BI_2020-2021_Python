import time
import random
import numpy
import matplotlib.pyplot as plt


def time_analyzer(min_quant, max_quant, step):
    xs = range(min_quant, max_quant + 1, step)
    print(xs)
    # numpy
    time_list_1 = []
    for i in range(min_quant, max_quant + 1, step):
        start = time.time()
        numpy.random.uniform(0, 1, size=i)
        end = time.time()
        time_list_1.append(end - start)
    # random
    time_list_2 = []
    for i in range(min_quant, max_quant + 1, step):
        start = time.time()
        for j in range(1, i + 1):
            random.uniform(0, 1)
        end = time.time()
        time_list_2.append(end - start)
    # visualization
    plt.plot(xs, time_list_1, color='green', label='numpy')
    plt.plot(xs, time_list_2, color='red', label='random')
    plt.grid()
    plt.title('Duration of the process depending on module and quantity of numbers.')
    plt.xlabel('Quantity of numbers')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig('Numpy_vs_random')
    plt.show()
