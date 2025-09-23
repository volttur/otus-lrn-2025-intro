import pytest

from src.Circle import Circle


@pytest.mark.parametrize(
    ("r", "area"), [(1, 3.14), (1.1, 3.8)], ids=["integer", "float"]
)
def test_circle_area_positive(r, area):
    r = Circle(r)
    assert r.area == area, "Circle area with sides 3 and 5 has to be 15"


@pytest.mark.parametrize(
    ("r", "perimeter"), [(2, 12.57), (2.5, 15.71)], ids=["integer", "float"]
)
def test_circle_perimeter_positive(r, perimeter):
    r = Circle(r)
    assert r.perimeter == perimeter, "Circle perimeter with sides 4 and 5 has to be 18"


@pytest.mark.parametrize(
    ("r", "area_sum"), [(1, 18.14), (4.5, 78.62)], ids=["integer", "float"]
)
def test_circle_add_area_positive(r, area_sum, add_figure):
    fig = add_figure
    r = Circle(r)
    assert r.add_area(fig) == area_sum, (
        "Sum of figures with areas 20 and 15 has to be 35"
    )


@pytest.mark.parametrize(("r"), [(0), (-1)], ids=["r zero", "r -1"])
def test_circle_creation_values_negative(r):
    with pytest.raises(ValueError):
        Circle(r)


@pytest.mark.parametrize(
    ("r"), [("str"), (True), (None)], ids=["r str", "r bool", "None"]
)
def test_circle_creation_types_negative(r):
    with pytest.raises(TypeError):
        Circle(r)


# def test_rectangle_perimeter_positive(popular_rectangle_int):
#    a, b = popular_rectangle_int
#    a += 1
#    b += 1
#    r = Rectangle(a, b)
#    assert r.perimeter == 20, f'Rectangle perimeter with sides 4 and 6 has to be 20'
