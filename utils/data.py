from utils.math import count_min_mean_median_mode_sd_max


def vertical_slice_data(data: list, index):
    return [item[index] for item in data]


def vertical_slice_all_data(data: list):
    return [list(i) for i in list(zip(*data))]


def sort_data(data: tuple, index):
    return sorted(data, key=lambda x: x[index])


def group_by(data: list, index):
    groups = {}
    for i in data:
        if i[index] in groups:
            groups[i[index]].append(i)
        else:
            groups[i[index]] = list(i)
    return groups


def summary(data: list, fields: list):
    summary_list = []
    for i, j in fields:
        vs_data = sorted(vertical_slice_data(data, j))
        summary_list.append(((i, j), count_min_mean_median_mode_sd_max(vs_data)))
    return summary_list
