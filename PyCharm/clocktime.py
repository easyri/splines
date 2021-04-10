from PyCharm.quadratic_processing import process_quadratic
from PyCharm.quadratic_spline import quadratic_spline

from PyCharm.cubic_spline import cubic_spline
from PyCharm.cubic_processing import process_cubic

import timeit
import numpy as np
from show import amdal


def clocktime(repeat=2, proc=4):
    time_q = np.zeros(proc)
    time_quadratic = min(timeit.Timer(quadratic_spline).repeat(repeat=repeat))
    time_quadratic_proc = np.array(proc)
    for i in range(1, proc):
        time_quadratic_proc[i] = min(timeit.Timer(process_quadratic(i + 1)).repeat(repeat=repeat))
    time_q[0] = time_quadratic  # 1 thread script
    time_q += time_quadratic_proc  # 2, 3, 4 ... process script
    amdal(time_q)

    time_c = np.zeros(proc)
    time_cubic = min(timeit.Timer(cubic_spline).repeat(repeat=repeat))
    time_cubic_proc = np.array(proc)
    for i in range(1, proc):
        time_cubic_proc[i] = min(timeit.Timer(process_cubic(i + 1)).repeat(repeat=repeat))
    time_c[0] = time_cubic
    time_c += time_cubic_proc
    amdal(time_c)
