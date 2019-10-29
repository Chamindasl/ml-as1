from collections import Counter
import math


def count(data: list):
    return len(data)


def mean(data: list):
    return sum(data) * 1.0 / len(data)


def median(data: list):
    n = count(data)
    if n % 2 == 0:
        return (data[n // 2] + data[n // 2 - 1]) / 2
    else:
        return data[n // 2]


def mode(data: list):
    get_mode = dict(Counter(data))
    return [k for k, v in get_mode.items() if v == max(list(data.values()))]


def sd(data: list):
    total = 0
    m = mean(data)
    for i in data:
        total += ((i - m) ** 2)
    return math.sqrt(total * 1.0 / (len(data) - 1))


def count_min_mean_median_mode_sd_max(data:list):
    return {
               "count": count(data),
               "min": min(data),
               "mean": mean(data),
               "median": median(data),
               "sd": sd(data),
               "max": max(data)
    }
