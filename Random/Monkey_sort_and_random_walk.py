import random
import time
import matplotlib.pyplot as plt
import numpy as np


# генерация массивов разного размера
def list_generator(min_size=8, max_size=10, step=1):
    list_of_lists = []
    xs = []
    for i in range(min_size, max_size + 1, step):
        the_list = np.random.randint(0, 10, i)
        list_of_lists.append(the_list)
        xs.append(i)
    return list_of_lists, xs
# этот код короче, но мой простой мне роднее
# def is_sorted(x):
#     return all(b >= a for a, b in zip(the_list, the_list[1:])


# проверка отсортирован ли список
def sort_check(my_list):
    flag = True
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            flag = False
    return flag


# сортировка, возвращает время выполнения
def monkey_sort(my_list):
    start = time.time()
    while not sort_check(my_list):
        random.shuffle(my_list)
    end = time.time()
    return end - start


# зависимость среднего времени выполнения от количества элементов
def monkey_visualization(min_list_size=8, max_list_size=11, step=1, replics=3):
    lst, xs = list_generator(min_list_size, max_list_size, step)
    mean_list = []
    sd_list = []
    for elem in lst:
        repl_list = []
        for _ in range(replics):
            repl_list.append(monkey_sort(elem))
        mean_list.append(np.mean(repl_list))
        sd_list.append(np.std(repl_list))
    _, ax = plt.subplots()
    ax.bar(xs, mean_list, color='green', align='center', alpha=0.5)
    ax.errorbar(xs, mean_list, sd_list, color='#297083', ls='none', lw=2, capthick=2)
    ax.set_title('Distribution of time for monkey sort.')
    ax.set_xlabel('Number of elements')
    ax.set_ylabel('Time')
    plt.grid()
    plt.savefig('Monkey_sort.png')
    plt.show()


# случайная прогулка из (0, 0)
def random_walk(steps):
    xs = [0] * steps
    ys = [0] * steps
    for i in range(1, steps):
        result = np.random.randint(1, 5)
        if result == 1:
            xs[i] = xs[i - 1]
            ys[i] = ys[i - 1] + 1
        elif result == 2:
            xs[i] = xs[i - 1] + 1
            ys[i] = ys[i - 1]
        elif result == 3:
            xs[i] = xs[i - 1]
            ys[i] = ys[i - 1] - 1
        else:
            xs[i] = xs[i - 1] - 1
            ys[i] = ys[i - 1]
    plt.scatter(xs, ys, c='green', marker='*')
    plt.title('Random walk scatter plot')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.savefig('Random_walk')
    plt.show()
