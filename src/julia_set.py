def list_interval(x1, x2, y1, y2, desired_width):
    x_epsilon = abs(x2 - x1) / desired_width
    y_epsilon = abs(y2 - y1) / desired_width

    xs = []
    x_cord, x_up_limit = min(x1, x2), max(x1, x2)
    while x_cord < x_up_limit:
        xs.append(x_cord)
        x_cord += x_epsilon

    ys = []
    y_cord, y_up_limit = min(y1, y2), max(y1, y2)
    while y_cord < y_up_limit:
        ys.append(y_cord)
        y_cord += y_epsilon

    return xs, ys

def yield_complex_cord(xs, ys):
    for y_cord in ys:
        for x_cord in xs:
            yield complex(x_cord, y_cord)


def calculate_z_serial(max_iteration, xs, ys, c):
    output = []
    for z in yield_complex_cord(xs, ys):
        n = 0
        while abs(z) < 2 and n < max_iteration:
            z = z**2 + c
            n += 1

        output.append(n)

    return output