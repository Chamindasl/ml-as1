from utils.math import count_min_mean_median_mode_sd_max
import operator


def vertical_slice_data(data: list, index):
    return [item[index] for item in data]


def vertical_slice_all_data(data: list):
    return [list(i) for i in list(zip(*data))]


def sort_data(data: tuple, index):
    return sorted(data, key=lambda x: x[index])


def group_by(data: list, indexes):
    groups = {}
    for i in data:
        key = []
        for j in indexes:
            key.append(i[j])
        key_tuple = tuple(key)
        if key_tuple not in groups:
            groups[key_tuple] = []
        groups[key_tuple].append(i)
    return {i: groups[i] for i in sorted(groups.keys())}


def two_group_count_list(data: dict):
    g1 = set(k for k, v in data.keys())
    g2 = set(v for k, v in data.keys())
    k = 0
    ll = 0
    result = []
    sorted1 = sorted(g1)
    sorted2 = sorted(g2)
    for i in sorted1:
        result.append([])
        for j in sorted2:
            result[k].append([])
            if (sorted1[k], sorted2[ll]) in data:
                result[k][ll] = len(data[(sorted1[k], sorted2[ll])])
            else:
                result[k][ll] = 0
            ll += 1
        ll = 0
        k += 1
    result.insert(0, sorted1)
    result.insert(1, sorted2)
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
