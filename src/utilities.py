import numpy as np
import matplotlib.pyplot as plt

from functools import wraps
import time


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time

def interval_generator(a, b, width):
    epsilon = abs(a - b) / width
    cord, up_limit = min(a, b), max(a, b)
    while cord < up_limit:
        yield cord
        cord += epsilon

def list_interval(x1, x2, y1, y2, desired_width):
    xs = list(interval_generator(x1, x2, desired_width))
    ys = list(interval_generator(y1, y2, desired_width))

    return xs, ys

def yield_complex_cord(xs, ys):
    for y_cord in ys:
        for x_cord in xs:
            yield complex(x_cord, y_cord)

def generate_plot(xs, ys, F):
    shape = int(np.sqrt(len(F)))
    F = np.reshape(F, (shape, shape))
    plt.pcolormesh(xs, ys, F, cmap = "binary", shading="gouraud")
    plt.axis('equal')
    plt.axis('off')
    plt.show()