from unittest import TestCase

from utils.math import count


class TestMath(TestCase):

    def test_count(self):
        data = [(1, "A", 1.1), (2, "B", 2.2), (3, "C", 3.3), (3, "C", 3.3)]
        expect = 4
        self.assertEqual(expect, count(data))
