import sys

sys.path.append('/home/jzere/otus_lrn/otus-lrn-2025-intro/src')

from Rectangle import Rectangle

def test_rectangle():
        r = Rectangle(3, 5)
        assert r.get_area == 15
