import unittest
from base import Point

class TestBase(unittest.TestCase):
    def test_add(self):
        assert Point(1,0) + Point(1, 1) == Point(2, 1)
        assert Point(1,0) + Point(1, 1) != Point(3, 1)

    def test_repr(self):
        assert(Point(1,1).__repr__() == (1, 1))

    def test_eq(self):
        assert (Point(1, 1) == Point(1,1))
        assert (Point(2, 1) != Point(2, 1))