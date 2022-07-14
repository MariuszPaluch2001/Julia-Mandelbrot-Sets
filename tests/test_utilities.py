from src.julia_set import list_interval, yield_complex_cord, calculate_z_serial
import pytest

def test_list_interval():
    x1, x2, y1, y2, desired_width = 0, 1, 0, 1, 10
    xs, ys = list_interval(x1,x2,y1,y2,desired_width)
    assert xs ==  pytest.approx([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
    assert ys ==  pytest.approx([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])

def test_list_interval_empty():
    x1, x2, y1, y2, desired_width = 0, 0, 0, 0, 10
    xs, ys = list_interval(x1,x2,y1,y2,desired_width)
    assert len(xs) == 0
    assert len(ys) == 0

def test_yield_complex_cord():
    xs = [1,2]
    ys = [0,3]

    complex_cords = [cord for cord in yield_complex_cord(xs, ys)]

    assert complex_cords == [1 + 0j, 2+0j, 1+3j, 2+3j]

def test_z_serial_output():
    x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
    c = complex(-0.62772, -.42193)

    xs, ys = list_interval(x1, x2, y1, y2, 1000)

    output = calculate_z_serial(300, xs, ys, c)
    
    assert sum(output) == 33219980