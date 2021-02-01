import matplotlib.pyplot as plt
plt.rcParams['savefig.bbox'] = 'tight'
plt.figure(figsize=(10, 8))
y = [i for i in range(1, 20)]
xs = [[i for i in range(1, 20)]]
for i in range(1, 4):
    xs.append([j + 2 for j in xs[i - 1]])
graph_number = 0
lstyle = ['-', '--', '-.', ':']
for i in range(len(xs)):
    graph_number += 1
    plt.plot(xs[i], y, label=str(graph_number), linestyle=lstyle[i])
plt.title('Line plots')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.legend()
plt.savefig('Line_plots.png')
plt.show()

