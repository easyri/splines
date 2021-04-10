from PyCharm.quadratic_processing import process_quadratic
from PyCharm.quadratic_spline import quadratic_spline

from PyCharm.cubic_spline import cubic_spline
from PyCharm.cubic_processing import process_cubic

import timeit


time = min(timeit.Timer(cubic_spline).repeat(repeat=10))
