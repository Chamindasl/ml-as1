from collections import Counter
import math

from exceptions.base_exceptions import NotANumberList, NotANumber


def count(data: list):
    """
    Item count of any data list
    Examples:
         >>> print(count([1.1, 2.2, 3.3, 4.4, 5.5]))
         5
    :param data: data list
    :return: Item count of data list
    """
    return len(data)


def mean(data: list):
    """
    Mean of numeric list
    Examples:
         >>> print(mean([1.1, 2.2, 3.3, 4.4, 5.5]))
         3.3
    :param data: data list
    :return: Mean of numeric list
    :raise NotANumberList when data list is not numeric list
    """
    try:
        return sum(data) * 1.0 / len(data)
    except TypeError:
        raise NotANumberList


def median(data: list):
    """
    Median of sorted list. Method will NOT sort the list.
    Examples:
         >>> print(median([1.1, 2.2, 3.3, 2.2, 5.5]))
         3.3
    :param data: data list, data list must not be numeric
    :return: Mean of data list
    :raise NotANumber when data has no exact median and left or right is not a number
    """
    try:
        n = count(data)
        if n % 2 == 0:
            return (data[n // 2] + data[n // 2 - 1]) / 2
        else:
            return data[n // 2]
    except TypeError:
        raise NotANumber


def mode(data: list):
    """
    mode and its number of occurrences of a data list.
    Examples:
         >>> print(mode(["A", "B", "C", "A", "B"]))
         [('A', 2), ('B', 2)]
    :param data: data list, data list must not be numeric
    :return: mode of data list
    """
    counter = Counter(data)
    common = counter.most_common()
    first_common = common[0]
    all_modes = []
    for i, j in common:
        if first_common[1] == j:
            all_modes.append((i, j))
        else:
            break
    return all_modes


def sd(data: list):
    """
    Standard Deviation of a numeric data list.
    Examples:
         >>> print(sd([1, 2, 3, 4, 5]))
         1.4142135623730951
    :param data: data list, data list must not be numeric
    :return: mode of data list
    """
    total = 0
    m = mean(data)
    for i in data:
        total += ((i - m) ** 2)
    return math.sqrt(total * 1.0 / (len(data)))


def count_min_mean_median_mode_sd_max(data: list):
    """
    generate min, mean, median, mode, sd and max return as a dictionary
    :param data: numaric data
    :return:
    """

    return {
               "count": count(data),
               "min": min(data),
               "mean": mean(data),
               "mode": mode(data),
               "median": median(data),
               "sd": sd(data),
               "max": max(data)
    }


