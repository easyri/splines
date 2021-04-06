import matplotlib.pyplot as plt
import multiprocessing as mp
import numpy as np

import show

img = plt.imread("../img/mandrill.jpg")

# Ширина и длина
n = img.shape[0]
m = img.shape[1]


def cut(img: np.array):
    img1 = img.copy()
    for i in range(n):
        for j in range(m):
            if (i % 2 == 0) or (j % 2 == 0):
                img1[i][j] = 0
    return img1


# # TODO переделать функцию для мультипроцессинга
# Функция, с заранее известными коэффициентами
def u(u_j: np.array, u_j1: np.array):
    array = np.abs(0.5 * u_j + 0.5 * u_j1)
    return np.where(array > 255, 255, array)


# # TODO Исправить индексы
#   восстанавливаем строки
def quadratic_spline_row(shared):
    for i in range(0, n):
        for j in range(1, m - 1, 2):
            shared[i][j] = u(shared[i][j - 1], shared[i][j + 1])


#   восстанавливаем столбцы
def quadratic_spline_column(shared):
    for j in range(0, m):
        for i in range(1, n - 1, 2):
            shared[i][j] = u(shared[i - 1][j], shared[i + 1][j])


def process_quadratic():

    shared_array = mp.Array('i', n * m * 3)
    shared_array[:] = cut(img).reshape(-1)

    p1 = mp.Process(target=quadratic_spline_row, args=[shared_array, ])
    p2 = mp.Process(target=quadratic_spline_column, args=[shared_array, ])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # # TODO Преобразовать в объект np.array
    # matrix = np.frombuffer(sharedArray.get_obj()).reshape((n, m))
    # show.show_one(matrix, 'quadratic_threading')
