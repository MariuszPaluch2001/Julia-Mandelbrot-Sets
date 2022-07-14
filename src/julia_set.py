from utilities import list_interval, yield_complex_cord


def calculate_z_serial(max_iteration, xs, ys, c):
    output = []
    for z in yield_complex_cord(xs, ys):
        n = 0
        while abs(z) < 2 and n < max_iteration:
            z = z**2 + c
            n += 1

        output.append(n)

    return output

def generate_julia_set(x1, x2, y1, y2, c, max_iteration, desired_width):

    xs, ys = list_interval(x1, x2, y1, y2, desired_width)

    output = calculate_z_serial(max_iteration, xs, ys, c)

    return xs, ys, output