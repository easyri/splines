from PyCharm.quadratic_processing import process_quadratic
from PyCharm.quadratic_spline import quadratic_spline

from PyCharm.cubic_spline import cubic_spline
from PyCharm.cubic_processing import process_cubic

import timeit
import numpy as np
from show import amdal


def clocktime(repeat=2):
    time_q = np.zeros(4)
    time_quadratic = min(timeit.Timer(quadratic_spline).repeat(repeat=repeat))
    time_quadratic_proc = np.array(4)
    for i in range(2, 5):
        time_quadratic_proc[i - 1] = min(timeit.Timer(process_quadratic(i)).repeat(repeat=repeat))
    time_q[0] = time_quadratic
    time_q += time_quadratic_proc
    amdal(time_q)

    time_c = np.zeros(4)
    time_cubic = min(timeit.Timer(cubic_spline).repeat(repeat=repeat))
    time_cubic_proc = np.array(3)
    for i in range(2, 5):
        time_cubic_proc[i - 2] = min(timeit.Timer(process_cubic(i)).repeat(repeat=repeat))
    time_c[0] = time_cubic
    time_c += time_cubic_proc
    amdal(time_c)
