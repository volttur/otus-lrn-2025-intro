import sys
import pytest

sys.path.append('C:/Users/AristovAV3/pyprojs/otus-lrn-2025-intro/src')

from Rectangle import Rectangle

@pytest.mark.parametrize(('side_a', 'side_b', 'area'), [(3, 5, 15), (3.5, 5.5, 19.25)], ids=['integer', 'float'])
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'Rectangle area with sides 3 and 5 has to be 15'

@pytest.mark.parametrize(('a', 'b', 'perimeter'), [(4, 5, 18), (2.5, 7.5, 20)], ids=['integer', 'float'])
def test_rectangle_perimeter_positive(a, b, perimeter):
    r = Rectangle(a, b)
    assert r.perimeter == perimeter, f'Rectangle perimeter with sides 4 and 5 has to be 18'

@pytest.mark.parametrize(('a', 'b', 'area_sum'), [(4, 5, 35), (4.5, 5.5, 39.75)], ids=['integer', 'float'])
def test_rectangle_add_area_positive(a, b, area_sum, add_figure):
    fig = add_figure
    r = Rectangle(a, b)
    assert r.add_area(fig) == area_sum, f'Sum of figures with areas 20 and 15 has to be 35'

@pytest.mark.parametrize(('a', 'b'), [(0, 5), (5, 0), (-1, 5), (5, -1), (0, 0)], ids=['a zero', 'b zero', 'a -1', 'b -1', 'all zero'])
def test_rectangle_creation_values_negative(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)

@pytest.mark.parametrize(('a', 'b'), [('str', 5), (5, 'str'), (True, 5), (5, False), (None, None)], ids=['a str', 'b str', 'a bool', 'b bool', 'All None'])
def test_rectangle_creation_types_negative(a, b):
    with pytest.raises(TypeError):
        Rectangle(a, b)

@pytest.mark.parametrize(('x'), [(5), ('str'), (True), (None)], ids=['int', 'str', 'bool', 'None'])
def test_rectangle_add_area_types_negative(x, add_figure):
    fig = add_figure
    with pytest.raises(TypeError):
        fig.add_area(x)

