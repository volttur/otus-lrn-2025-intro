import pytest

from src.Triangle import Triangle


@pytest.mark.parametrize(
    ("a", "b", "c", "area"),
    [(3, 4, 5, 6), (3.5, 4.5, 5.5, 7.85)],
    ids=["integer", "float"],
)
def test_triangle_area_positive(a, b, c, area):
    r = Triangle(a, b, c)
    assert r.area == area, "Triangle area with sides 3, 4 and 5 has to be 6"


@pytest.mark.parametrize(
    ("a", "b", "c", "perimeter"),
    [(3, 4, 5, 12), (2.5, 4.5, 5.5, 12.5)],
    ids=["integer", "float"],
)
def test_triangle_perimeter_positive(a, b, c, perimeter):
    r = Triangle(a, b, c)
    assert r.perimeter == perimeter, (
        "Triangle perimeter with sides 2.5, 4.5 and 7.5 has to be 14.5"
    )


@pytest.mark.parametrize(
    ("a", "b", "c", "area_sum"),
    [(3, 4, 5, 21), (3.5, 4.5, 5.5, 22.85)],
    ids=["integer", "float"],
)
def test_triangle_add_area_positive(a, b, c, area_sum, add_figure):
    fig = add_figure
    r = Triangle(a, b, c)
    assert r.add_area(fig) == area_sum, (
        "Sum of figures with areas 6 and 15 has to be 21"
    )


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        (1, 2, 5),
        (0, 1, 2),
        (1, 0, 2),
        (1, 2, 0),
        (-1, 1, 2),
        (1, -1, 2),
        (1, 2, -1),
        (0, 0, 0),
        (-1, -1, -1),
    ],
    ids=[
        "Cant build",
        "a zero",
        "b zero",
        "c zero",
        "a -1",
        "b -1",
        "c -1",
        "all zero",
        "all -1",
    ],
)
def test_triangle_creation_values_negative(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        ("str", 5, 6),
        (5, "str", 6),
        (5, 6, "str"),
        (True, 5, 6),
        (5, False, 6),
        (5, 6, None),
    ],
    ids=["a str", "b str", "c str", "a bool", "b bool", "c None"],
)
def test_triangle_creation_types_negative(a, b, c):
    with pytest.raises(TypeError):
        Triangle(a, b, c)
