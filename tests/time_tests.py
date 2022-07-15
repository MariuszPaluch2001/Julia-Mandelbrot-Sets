from src.julia_set import *
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
def calculate_z_serial_wrapper():
    calculate_z_serial(maxiter, xs, ys, c)

@timefn
def generate_julia_set_wrapper():
    generate_julia_set(x1,x2,y1,y2,c, maxiter, width)

if __name__ == "__main__":
    list_interval_wrapper()
    calculate_z_serial_wrapper()
    generate_julia_set_wrapper()
