from unittest import TestCase

from utils.data import group_count_list


class TestData(TestCase):

    def test_two_group_count_list(self):
        from utils.data import two_group_count_list
        a = two_group_count_list({
            ("C", "a"): [1, 2, 3],
            ("A", "b"): [1, 2, 3],
            ("A", "a"): [1, 2],
            ("B", "c"): [1, 2, 4, 4],
            ("C", "d"): [1, 2]
        })
        e = [['A', 'B', 'C'],
             ['a', 'b', 'c', 'd'],
             [2, 0, 3],
             [3, 0, 0],
             [0, 4, 0],
             [0, 0, 2]]

        self.assertEqual(e, a)

    def test_group_count_list(self):
        a = group_count_list({
            ("C"): [1, 2],
            ("A"): [1, 2, 3],
            ("B"): [1, 2, 4, 4],
        })
        e = [['A', 'B', 'C'],
             [3, 4, 2]
             ]

        self.assertEqual(a, e)
