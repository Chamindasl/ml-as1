
def slice_data(data: tuple, index):
    return [item[index] for item in data]


def sort_data(data: tuple, index):
    return sorted(data, key=lambda x: x[index])
