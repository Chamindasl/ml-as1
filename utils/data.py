from utils.math import count_min_mean_median_mode_sd_max
import operator


def vertical_slice_data(data: list, index):
    return [item[index] for item in data]


def vertical_slice_all_data(data: list):
    return [list(i) for i in list(zip(*data))]


def sort_data(data: tuple, index):
    return sorted(data, key=lambda x: x[index])


def group_by(data: list, index):
    groups = {}
    for i in data:
        if not i[index] in groups:
            groups[i[index]] = []
        groups[i[index]].append(i)
    return groups


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
