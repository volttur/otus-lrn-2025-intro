import pytest

from src.Square import Square


@pytest.mark.parametrize(
    ("a", "area"), [(5, 25), (5.5, 30.25)], ids=["integer", "float"]
)
def test_square_area_positive(a, area):
    r = Square(a)
    assert r.area == area, "Square area with side 5 has to be 25"


@pytest.mark.parametrize(
    ("a", "perimeter"), [(5, 20), (5.5, 22)], ids=["integer", "float"]
)
def test_square_perimeter_positive(a, perimeter):
    r = Square(a)
    assert r.perimeter == perimeter, "Square perimeter with side 5 has to be 20"


@pytest.mark.parametrize(
    ("a", "area_sum"), [(5, 40), (5.5, 45.25)], ids=["integer", "float"]
)
def test_square_add_area_positive(a, area_sum, add_figure):
    fig = add_figure
    r = Square(a)
    assert r.add_area(fig) == area_sum, (
        "Sum of figures with areas 20 and 15 has to be 35"
    )


@pytest.mark.parametrize(("a"), [(0), (-1)], ids=["a zero", "b -1"])
def test_square_creation_values_negative(a):
    with pytest.raises(ValueError):
        Square(a)


@pytest.mark.parametrize(
    ("a"), [("str"), (True), (None)], ids=["a str", "a bool", "a None"]
)
def test_square_creation_types_negative(a):
    with pytest.raises(TypeError):
        Square(a)
