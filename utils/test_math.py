from unittest import TestCase

from numpy import mean as n_mean, median as n_median, std

from exceptions.base_exceptions import NotANumberList, NotANumber
from utils.math import count, mean, median, mode, sd, count_min_mean_median_mode_sd_max


class TestMath(TestCase):

    def test_count(self):
        data = [(1, "A", 1.1), (2, "B", 2.2), (3, "C", 3.3), (3, "C", 3.3)]
        expect = 4
        self.assertEqual(expect, count(data))

    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(n_mean(data), mean(data))
        data = [1.1, 2.2, 3.3, 4.4, 5.5]
        self.assertEqual(n_mean(data), mean(data))

    def test_mean_error_cases(self):
        data = [1, 2, 3, 4, "A"]
        self.assertRaises(NotANumberList, mean, data)

    def test_median(self):
        data = [1.1, 2.2, 3.3, 4.4, 5.5]
        self.assertEqual(n_median(data), median(data))  # testing median using numpy
        data = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(n_median(data), median(data))  # testing median using numpy
        data = [1.1, 2.2, 3.4, "A"]
        self.assertEqual(2.8, median(data))  # numpy does not support median for non numeric
        data = ["A", "A", "A"]
        self.assertEqual("A", median(data))  # numpy does not support median for non numeric

    def test_median_error_cases(self):
        data = [1.1, "A", 1, 3.4, ]  # no exact middle, and left or right are not numeric
        self.assertRaises(NotANumber, median, data)
        data = [1.1, 1, "A", 3.4, ]  # no exact middle, and left or right are not numeric
        self.assertRaises(NotANumber, median, data)
        data = [1.1, "A", "A", 3.4, ]  # no exact middle, and left or right are not numeric
        self.assertRaises(NotANumber, median, data)

    def test_mode(self):
        data = [1.1, 2.2, 2.2, 4.4, 5.5]
        self.assertEqual([(2.2, 2)], mode(data))  # mode is 2.2 and occurrences is 2
        data = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual([(1.1, 1), (2.2, 1), (3.3, 1), (4.4, 1)], mode(data))  # all items are modes
        data = [1.1, 2.2, 3.3, 4.4, 1.1, 2.2, 3.3, 4.4]
        self.assertEqual([(1.1, 2), (2.2, 2), (3.3, 2), (4.4, 2)], mode(data))  # all items are modes
        data = [1.1, "A", 3.4, "A"]
        self.assertEqual([('A', 2)], mode(data))  # mode is A and occurrences is 2
        data = ["A", "B", "C", "A", "B"]  # 2 modes modes are A, and B their and occurrences is 2
        self.assertEqual([('A', 2), ('B', 2)], mode(data))

    def test_sd(self):
        data = [2, 2, 2, 2, 2]
        self.assertEqual(0, sd(data))  # no deviation
        data = [1, 2, 3, 4, 5]
        self.assertEqual(std(data), sd(data))  # testing standard deviation using numpy
        data = [1.1, 2.2, 3.3, 4.4, 5.5]
        self.assertEqual(std(data), sd(data))  # testing standard deviation using numpy

    def test_count_min_mean_median_mode_sd_max(self):
        data = [1, 2, 3, 3, 4, 5]
        result = count_min_mean_median_mode_sd_max(data)
        self.assertEqual(6, result["count"])
        self.assertEqual(1, result["min"])
        self.assertEqual(3, result["mean"])
        self.assertEqual([(3, 2)], result["mode"])
        self.assertEqual(3, result["median"])
        self.assertEqual(std(data), result["sd"])
        self.assertEqual(5, result["max"])

    def test_count_min_mean_median_mode_sd_max_error_cases(self):
        data = ["A", 2, 3, 3, 4, 5]
        self.assertRaises(TypeError, count_min_mean_median_mode_sd_max, data)
