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


# Функция, с заранее известными коэффициентами
def u(u_j: np.array, u_j1: np.array):
    return abs(0.5 * u_j + 0.5 * u_j1)


# TODO
def linear_parallel_enlarge_threads(cutdata: mp.Array, width: int, height: int, n: int, part: int, th: int, data: mp.Array):
    num = height / th
    if num % 2 == 1:
        num -= 1
    i = width * n * part * num
    end_i = i + width * n * num

    if part == th - 1:
        end_i = width * height * n
    j = i * 4

    while i < end_i:
        k = 0
        s = 0
        while k < width * n:
            data[j + s] = cutdata[i + k]
            data[j + s + 1] = cutdata[i + k + 1]
            data[j + s + 2] = cutdata[i + k + 2]
            k += 3
            s += 6

        i += width * n
        j += 4 * width * n

    for channel in range(n):
        i = width * n * 4 * part * num
        end_i = width * n * 4 * (part + 1) * num
        if part == th - 1:
            end_i = width * height * n * 4

        while i < end_i:
            j = n
            while j < 2 * width * n - 3:
                res = u(data[i + j - n + channel], data[i + j + n + channel])
                if res > 255:
                    res = 255
                data[i + j + channel] = res  # int8_t
                j += n * 2

            if j == 2 * width * n - 3:
                res = u(data[i + j - n + channel], data[i + j - 2 * n + channel])
                if res > 255:
                    res = 255
                data[i + j + channel] = res  # int8_t

            i += width * 4 * n

    for channel in range(n):
        actual_width = 2 * width * n
        i = 0
        while i <= actual_width - 1:
            j = num * part * 2 + 1
            end_j = num * 2 * (part + 1) - 1
            if part == th - 1:
                end_j = height * 2 - 1

            while j < end_j:
                res = u(data[i + actual_width * (j - 1) + channel], data[i + actual_width * (j + 1) + channel])
                if res > 255:
                    res = 255
                data[i + actual_width * j + channel] = res
                j += 2

            if j == end_j:
                res = u(data[i + actual_width * (j - 1) + channel], data[i + actual_width * (j - 2) + channel])
                if res > 255:
                    res = 255
                data[i + actual_width * j + channel] = res

            i += n


def process_quadratic():

    shared_img_cutted = mp.Array('d', n * m * 3)
    shared_img_cutted[:] = cut(img).reshape(-1)

    shared_img = mp.Array('d', n * m * 3)
    _ = np.array(img.copy())
    shared_img[:] = _.reshape(-1)

    p1 = mp.Process(target=linear_parallel_enlarge_threads, args=(shared_img_cutted, n, m, 3, 1, 2, shared_img,))
    p2 = mp.Process(target=linear_parallel_enlarge_threads, args=(shared_img_cutted, n, m, 3, 2, 2, shared_img,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # # TODO Преобразовать в объект np.array
    # matrix = np.frombuffer(sharedArray.get_obj()).reshape((n, m))
    # show.show_one(matrix, 'quadratic_threading')
