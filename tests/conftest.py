import pytest

@pytest.fixture
def popular_rectangle_int():
    a = 3
    b = 5

    yield a, b

    a -= 1
    b -= 1

