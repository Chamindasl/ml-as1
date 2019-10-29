from utils.math import count_min_mean_median_mode_sd_max


def vertical_slice_data(data: list, index):
    return [item[index] for item in data]


def sort_data(data: tuple, index):
    return sorted(data, key=lambda x: x[index])


def summary(data: list, fields: list):
    summary_list = []
    for i, j in fields:
        vs_data = sorted(vertical_slice_data(data, j))
        summary_list.append(((i, j), count_min_mean_median_mode_sd_max(vs_data)))
    return summary_list
