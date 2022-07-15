from src.julia_set import *
from src.mandelbrot_set import *
from src.utilities import *

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c = complex(-0.62772, -.42193)
width = 1000
maxiter = 300
xs,ys = list_interval(x1, x2,y1,y2, width)

@timefn
def list_interval_wrapper():
    list_interval(x1,x2,y1,y2,width)

@timefn
def calculate_z_serial_julia_wrapper():
    calculate_z_serial_julia(maxiter, xs, ys, c)

@timefn
def calculate_z_serial_mandelbrot_wrapper():
    calculate_z_serial_mandelbrot(maxiter, xs, ys)

@timefn
def generate_julia_set_wrapper():
    generate_julia_set(x1,x2,y1,y2,c, maxiter, width)

@timefn
def generate_mandelbrot_set_wrapper():
    generate_mandelbrot_set(x1,x2,y1,y2, maxiter, width)

if __name__ == "__main__":
    list_interval_wrapper()
    calculate_z_serial_julia_wrapper()
    calculate_z_serial_mandelbrot_wrapper()
    generate_julia_set_wrapper()
    generate_mandelbrot_set_wrapper()
