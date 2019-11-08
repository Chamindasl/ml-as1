import operator

from utils.math import count_min_mean_median_mode_sd_max


def vertical_slice_data(data: list, index):
    """
    This is a reusable utility method can be used with any data set, which can be used to slice vertically indexed data
     as a list from list of tuple or list of list.
    Examples:
         >>> print(vertical_slice_data([
         (1, "A", 1.1),
         (2, "B", 2.2),
         (3, "C", 3.3)], 1))
         ["A", "B", "C"]
    :param data: as list of tuple or list of list
    :param index: index of tuple
    :return: index data of all tuple as list

    Raises:
        IndexError: When index is out of range.
        TypeError: When index is not integer.

    .. seealso:: ``vertical_slice_all_data``
    """
    return [item[index] for item in data]


def vertical_slice_all_data(data: list):
    """
    This is a reusable utility method can be used with any data set, which can be used to slice vertically
    all indexed data as a list from list of tuple or list of list.

    Examples:
         >>> print(vertical_slice_all_data([ \
         (1, "A", 1.1), \
         (2, "B", 2.2), \
         (3, "C", 3.3)]))
         [[1, 2, 3], ["A", "B", "C"], [1.1, 2,2, 3.3]]
    :param data: as list of tuple or list of list
    :return: all index data of all tuple as list

    .. seealso:: ``vertical_slice_data``
    """
    return [list(i) for i in list(zip(*data))]


def sort_data(data: tuple, index):
    """
    This is a reusable utility method can be used with any data set, which sorts vector type data
     (eg, list of tuple, list of list) based on given indexed column

    Examples:
         >>> print(sort_data([ \
         (3, "A", 1.1), \
         (2, "B", 2.2), \
         (1, "C", 3.3)]))
         [(1, "C", 3.3), (2, "B", 2.2), (3, "A", 1.1)]

    :param data: as list of tuple or list of index
    :param index: column index
    :return: sorted vector (list or tuple) by column index

    Raises:
        IndexError: When index is out of range.
        TypeError: When index is not integer.

    """
    return sorted(data, key=lambda x: x[index])


def group_by(data: list, indexes: list):
    """
    This is a reusable utility method can be used with any data set, which groups the vector data
    (list of list or list ot tuple) by given one or more column indexes
    :param data: as list of tuple or list of index
    :param indexes: list of column index, single element list can be used for one column
    :return: dictionary, key as column values and value as list of tuple

    Examples:
         >>> print(group_by([(3, "A", 1.1), (2, "A", 2.2), (3, "C", 1.1), \
          (1, "B", 4.3), (1, "B", 3.3), (1, "BB", 3.3)], \
           [0, 1])
         {
                (1, 'B'): [(1, 'B', 4.3), (1, 'B', 3.3)],
                (1, 'BB'): [(1, 'BB', 3.3)],
                (2, 'A'): [(2, 'A', 2.2)],
                (3, 'A'): [(3, 'A', 1.1)],
                (3, 'C'): [(3, 'C', 1.1)]
        }

    Raises:
        IndexError: When index is out of range.
        TypeError: When index is not integer.

    """
    groups = {}  # dic for groups
    for i in data:
        key = []  # all keys
        for j in indexes:
            key.append(i[j])
        if len(key) > 1:  # if multiple columns, key would be tuple, otherwise key would be single value to avoid (k,)
            key_tuple = tuple(key)
        else:
            key_tuple = key[0]
        if key_tuple not in groups:  # if key is not in dict add it it with empty list
            groups[key_tuple] = []
        groups[key_tuple].append(i)  # append data to relevant group
    return {i: groups[i] for i in sorted(groups.keys())}  # sort group by its key


def group_count_list(data: dict):
    """
    This is a reusable utility method can be used with any dictionary has key and corresponding data as a list, where
    output needs to be keys as a list and values as count of data as a separate list. This kind of data structure is
    required for graphs such as matlibplot or seaborn bar charts. Keys will be sorted for better visualization

    Examples:
         >>> print(group_count_list({ \
            "C": [1, 2],  \
            "A": [1, 2, 3], \
            "B": [1, 2, 4, 4], \
            "D": [] \
        })
        [['A', 'B', 'C', 'D'],
        [3, 4, 2, 0]
        ]
    :param data: data as dictionary of key and list of values
    :return: list of key and count of its items

    .. seealso:: ``two_group_count_list``

    """
    sorted1 = sorted(set(k for k in data.keys()))  # sorted keys
    result = [len(data[i]) for i in sorted1]  # count as list
    return [sorted1, result]


def two_group_count_list(data: dict):
    """
    This is a reusable utility method can be used with any dictionary has 2 items tuple as key and corresponding
    data as a list, where output needs to be keys as a list and values as count of data as a separate list in.
    tabular form. This kind of data structure is required for graphs such as matlibplot or seaborn bar charts.
    Keys will be sorted for better visualization.

    Examples:
         >>> print(two_group_count_list({ \
            ("C", "a"): [1, 2, 3], \
            ("A", "b"): [1, 2, 3], \
            ("A", "a"): [1, 2], \
            ("B", "c"): [1, 2, 4, 4], \
            ("C", "d"): [1, 2] \
        })
        [['A', 'B', 'C'],
        ['a', 'b', 'c', 'd'],
        [2, 0, 3],
        [3, 0, 0],
        [0, 4, 0],
        [0, 0, 2]]
    :param data: data as dictionary of key and list of values
    :return: list of 2 keys and count of its items in tabular form

    .. seealso:: ``group_count_list``

    """
    sorted_group_1 = sorted(set(k for k, v in data.keys()))  # sorted 1st level keys
    sorted_group_2 = sorted(set(v for k, v in data.keys()))  # sorted 2nd level keys
    key_1 = 0
    key_2 = 0
    result = []
    for i in sorted_group_2:  # loop through 2nd group
        result.append([])
        for j in sorted_group_1:  # loop through 2nd group
            result[key_2].append([])
            result[key_2][key_1] = 0  # initial count would be 0 always
            if (sorted_group_1[key_1], sorted_group_2[key_2]) in data:  # if tuple found in data
                result[key_2][key_1] = len(data[(sorted_group_1[key_1], sorted_group_2[key_2])])  # replace initial 0
            key_1 += 1
        key_1 = 0
        key_2 += 1
    result.insert(0, sorted_group_1)  # add first level keys as 1st item
    result.insert(1, sorted_group_2)  # add 2nd level keys as 2nd item
    return result


def filter_by_index(data: list, index, operator_txt, value):
    """
    Utility method to filter tuples as list from list of tuples based on a condition of a tuple index value.

    :param data: as list of tuple
    :param index: index of tuple
    :param operator_txt: operator, one of ">, <, >=, <=, ="
    :param value: value of the condition.
    :return: filtered list of tuple

    Examples:
        >>> filter_by_index([(3, "A", 1.1), (2.2, "A", 2.2), (3, "C", 1.1), (1, "B", 4.3), (1, "B", 3.3), \
         (1, "BB", 3.3)], 0, ">=", 2.2)
         [(3, 'A', 1.1), (2.2, 'A', 2.2), (3, 'C', 1.1)]

    Raises:
        IndexError: When index is out of range.
        TypeError: When index is not integer.
        ValueError: When operator_txt is not accepted

    """
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '=': operator.eq}
    if operator_txt not in ops:
        raise ValueError("Not a valid operator")
    return [i for i in data if ops[operator_txt](i[index], value)]


def summary(data: list, indexes: list):
    """
    Generate the summary for given columns. Summary includes Count, Min, Mean, Median, Mode, SD, and Max

    :param data: as list of tuple
    :param indexes: index of tuple
    :return: Summary of each index column of data

    Raises:
        IndexError: When index is out of range.
        TypeError: When index is not integer.
        TypeError: When column data is not numeric type.

    """

    summary_list = []
    for i, j in indexes:
        vs_data = sorted(vertical_slice_data(data, j))
        summary_list.append(((i, j), count_min_mean_median_mode_sd_max(vs_data)))
    return summary_list
