from unittest import TestCase


class TestData(TestCase):

    def test_two_group_count_list(self):
        from utils.data import two_group_count_list
        a = two_group_count_list({
            ("C", "E"): [1, 2, 3],
            ("A", "AA"): [1, 2, 3],
            ("A", "AB"): [1, 2],
            ("B", "AB"): [1, 2, 4, 4],
            ("C", "D"): [1],
            ("A", "D"): [1],
        })
        e = [['A', 'B', 'C'],
              ['AA', 'AB', 'D', 'E'],
              [3, 2, 1, 0],
              [0, 4, 0, 0],
              [0, 0, 1, 3]]

        self.assertEqual(a, e)
        print(a)
