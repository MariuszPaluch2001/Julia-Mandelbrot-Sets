from src.julia_set import list_interval
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