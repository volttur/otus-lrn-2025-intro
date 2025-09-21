import sys
import pytest

sys.path.append('/home/jzere/otus_lrn/otus-lrn-2025-intro/src')

from Rectangle import Rectangle

@pytest.mark.parametrize(('side_a', 'side_b', 'area'), [(3, 5, 15), (3.5, 5.5, 19.25)], ids=['integer', 'float'])
def test_rectangle_area_positive(side_a, side_b, area):
        r = Rectangle(side_a, side_b)
        assert r.area == area, f'Rectangle area with sides 3 and 5 has to be 15'

def test_rectangle_perimeter_positive(popular_rectangle_int):
    a, b = popular_rectangle_int
    a += 1
    b += 1
    r = Rectangle(a, b)
    assert r.perimeter == 20, f'Rectangle perimeter with sides 4 and 6 has to be 20'

