from src.utilities import list_interval, yield_complex_cord

# @profile
def calculate_z_serial_mandelbrot(max_iteration, xs, ys):
    output = []
    for z in yield_complex_cord(xs, ys):
        n = 0
        z0 = z
        while abs(z) < 2 and n < max_iteration:
            z = z*z + z0
            n += 1

        output.append(n)

    return output

def generate_mandelbrot_set(x1, x2, y1, y2, max_iteration, desired_width):

    xs, ys = list_interval(x1, x2, y1, y2, desired_width)

    output = calculate_z_serial_mandelbrot(max_iteration, xs, ys)

    return xs, ys, output
