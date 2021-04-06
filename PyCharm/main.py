import matplotlib.pyplot as plt
import time
import numpy as np

import PyCharm.error
from PyCharm.show import show, show_one

from PyCharm.quadratic_processing import process_quadratic
from PyCharm.quadratic_spline import quadratic_spline

from PyCharm.cubic_spline import cubic_spline
from PyCharm.cubic_processing import process_cubic

if __name__ == '__main__':
    # img = plt.imread("../img/mandrill.jpg")
    # step = 2
    # img_array_cutted = np.array(img[::step, ::step].copy(), dtype=np.uint8)

    # # Quadratic spline
    # quadratic_spline(img_array_cutted, img)

    # #Cubic spline
    # cubic_spline(img_array_cutted, img)

    # #-----Multiprocessing-----
    # # Quadratic spline + processing
    process_quadratic(num_process=2)

    # # Cubic spline + threading
    process_cubic(num_process=2)
    # #~~~~~Multiprocessing~~~~~
