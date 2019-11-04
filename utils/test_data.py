from unittest import TestCase

from utils.data import group_count_list, vertical_slice_all_data, vertical_slice_data, sort_data


class TestData(TestCase):

    def test_vertical_slice_data(self):
        data = [(1, "A", 1.1), (2, "B", 2.2), (3, "C", 3.3)]
        expected_array = [[1, 2, 3], ["A", "B", "C"], [1.1, 2.2, 3.3]]
        for i in range(3):
            actual = vertical_slice_data(data, i)
            self.assertEqual(expected_array[i], actual)

    def test_vertical_slice_data_wrong_index(self):
        data = [(1, "A", 1.1), (2, "B", 2.2), (3, "C", 3.3)]
        self.assertRaises(IndexError, vertical_slice_data, data, 4)
        self.assertRaises(TypeError, vertical_slice_data, data, "A")

    def test_vertical_slice_all_data(self):
        data = [(1, "A", 1.1), (2, "B", 2.2), (3, "C", 3.3)]
        expected_array = [[1, 2, 3], ["A", "B", "C"], [1.1, 2.2, 3.3]]
        actual = vertical_slice_all_data(data)
        self.assertEqual(expected_array, actual)

    def test_sort_data(self):
        data = [(3, "A", 1.1), (2, "C", 2.2), (1, "B", 3.3)]
        expected_array = [[(1, "B", 3.3), (2, "C", 2.2), (3, "A", 1.1)],
                          [(3, "A", 1.1), (1, "B", 3.3), (2, "C", 2.2)],
                          [(3, "A", 1.1), (2, "C", 2.2), (1, "B", 3.3)]
                          ]
        for i in range(3):
            actual = sort_data(data, i)
            self.assertEqual(expected_array[i], actual)

    def test_sort_data_wrong_index(self):
        data = [(3, "A", 1.1), (2, "C", 2.2), (1, "B", 3.3)]
        self.assertRaises(IndexError, sort_data, data, 3)

    def test_two_group_count_list(self):
        from utils.data import two_group_count_list
        data = {
            ("C", "a"): [1, 2, 3],
            ("A", "b"): [1, 2, 3],
            ("A", "a"): [1, 2],
            ("B", "c"): [1, 2, 4, 4],
            ("C", "d"): [1, 2]
        }
        actual = two_group_count_list(data)
        expected = [['A', 'B', 'C'],
                    ['a', 'b', 'c', 'd'],
                    [2, 0, 3],
                    [3, 0, 0],
                    [0, 4, 0],
                    [0, 0, 2]]

        self.assertEqual(expected, actual)

    def test_group_count_list(self):
        actual = group_count_list({
            "C": [1, 2],
            "A": [1, 2, 3],
            "B": [1, 2, 4, 4],
        })
        expected = [['A', 'B', 'C'],
                    [3, 4, 2]
                    ]

        self.assertEqual(expected, actual)
