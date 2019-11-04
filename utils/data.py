import operator

from utils.math import count_min_mean_median_mode_sd_max


def vertical_slice_data(data: list, index):
    """
    Can be used to slice vertically indexed data as a list from list of tuple or list of list.

    Examples:
         >>> print([i for i in vertical_slice_data([
         (1, "A", 1.1),
         (2, "B", 2.2),
         (3, "C", 3.3)], 1)])
         ["A", "B", "C"]
    :param data: as list of tuple or list of list
    :param index: index of tuple
    :return: index data of all tuple as list

    Raises:
        IndexError: When index is out of.
        TypeError: When index is not integer.

    .. seealso:: ``vertical_slice_all_data``
    """
    return [item[index] for item in data]


def vertical_slice_all_data(data: list):
    """
    Can be used to slice vertically all indexed data as a list from list of tuple or list of list.

    Examples:
         >>> print([i for i in vertical_slice_data([
         (1, "A", 1.1),
         (2, "B", 2.2),
         (3, "C", 3.3)])])
         [[1, 2, 3], ["A", "B", "C"], [1.1, 2,2, 3.3]]
    :param data: as list of tuple or list of list
    :return: all index data of all tuple as list

    Raises:
        IndexError: When index is out of.
        TypeError: When index is not integer.

    .. seealso:: ``vertical_slice_data``
    """
    return [list(i) for i in list(zip(*data))]


def sort_data(data: tuple, index):
    """
    Sort vector type data (eg, list of tuple, list of list) based on given indexed column

    Examples:
         >>> print([i for i in vertical_slice_data([
         (3, "A", 1.1),
         (2, "B", 2.2),
         (1, "C", 3.3)])])
         [(1, "C", 3.3), (2, "B", 2.2), (3, "A", 1.1)]

    :param data: as list of tuple or list of index
    :param index: column index
    :return:
    """
    return sorted(data, key=lambda x: x[index])


def group_by(data: list, indexes):
    groups = {}
    for i in data:
        key = []
        for j in indexes:
            key.append(i[j])
        if len(key) > 1:
            key_tuple = tuple(key)
        else:
            key_tuple = key[0]
        if key_tuple not in groups:
            groups[key_tuple] = []
        groups[key_tuple].append(i)
    return {i: groups[i] for i in sorted(groups.keys())}


def group_count_list(data: dict):
    g1 = set(k for k in data.keys())
    k = 0
    result = []
    sorted1 = sorted(g1)
    result.append([])
    for i in sorted1:
        if (sorted1[k]) in data:
            result[0].append(len(data[(sorted1[k])]))
        else:
            result[0].append(0)
        k += 1
    result.insert(0, sorted1)
    return result


def two_group_count_list(data: dict):
    sorted_group_1 = sorted(set(k for k, v in data.keys()))
    sorted_group_2 = sorted(set(v for k, v in data.keys()))
    k = 0
    ll = 0
    result = []
    for i in sorted_group_2:
        result.append([])
        for j in sorted_group_1:
            result[ll].append([])
            result[ll][k] = 0
            if (sorted_group_1[k], sorted_group_2[ll]) in data:
                result[ll][k] = len(data[(sorted_group_1[k], sorted_group_2[ll])])
            k += 1
        k = 0
        ll += 1
    result.insert(0, sorted_group_1)
    result.insert(1, sorted_group_2)
    return result


def filter_by_index(data: list, index, op, value):
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '=': operator.eq}
    return [i for i in data if ops[op](i[index[1]], value)]


def summary(data: list, fields: list):
    summary_list = []
    for i, j in fields:
        vs_data = sorted(vertical_slice_data(data, j))
        summary_list.append(((i, j), count_min_mean_median_mode_sd_max(vs_data)))
    return summary_list
