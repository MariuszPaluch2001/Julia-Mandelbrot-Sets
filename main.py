from src.julia_set import generate_julia_set
from src.mandelbrot_set import generate_mandelbrot_set
from src.utilities import generate_plot

if __name__ == "__main__":
    x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
    c = complex(-0.75, 0.1)
    xs, ys, F = generate_julia_set(x1,x2,y1,y2, c, 300, 1000)
    generate_plot(xs,ys,F)
    xs, ys, F = generate_mandelbrot_set(x1,x2,y1,y2, 300, 1000)
    generate_plot(xs,ys,F)