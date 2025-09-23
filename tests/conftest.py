import pytest

from src.Rectangle import Rectangle


@pytest.fixture
def popular_rectangle_int():
    a = 3
    b = 5

    yield a, b

    a -= 1
    b -= 1


@pytest.fixture
def add_figure():
    return Rectangle(3, 5)
