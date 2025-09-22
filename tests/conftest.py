import pytest
import sys

sys.path.append('C:/Users/AristovAV3/pyprojs/otus-lrn-2025-intro/src')

from Rectangle import Rectangle

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

