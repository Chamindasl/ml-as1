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
    total = 0
    m = mean(data)
    for i in data:
        total += ((i - m) ** 2)
    return math.sqrt(total * 1.0 / (len(data) - 1))


def count_min_mean_median_mode_sd_max(data: list):
    return {
               "count": count(data),
               "min": min(data),
               "mean": mean(data),
               "mode": mode(data),
               "median": median(data),
               "sd": sd(data),
               "max": max(data)
    }
