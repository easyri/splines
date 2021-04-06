import matplotlib.pyplot as plt
import numpy as np


def show_one(img: np.array, s: str):
    figsize = 10, 10
    f = plt.figure(figsize=figsize)
    _ = plt.imshow(img)
    plt.savefig('../img/' + s + '.jpg')


def show(new_img: np.array, img: np.array, name1: str, name2='original image'):
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 15))
    ax1.set_title(name1)
    _ = ax1.imshow(new_img)
    ax2.set_title(name2)
    _ = ax2.imshow(img)
    plt.savefig('../img/' + name1 + '.jpg')
