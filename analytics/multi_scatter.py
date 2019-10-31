import matplotlib.pyplot as plt


def plot(data: list, indexes: list):
    tuple_len = len(indexes)
    fig, axes = plt.subplots(tuple_len, tuple_len, figsize=(tuple_len*4, tuple_len*4))
    i = -1
    j = -1
    for k in indexes:
        i += 1
        for l in indexes:
            j += 1
            try:
                if j == 0:
                    axes[i, j].set_ylabel(k[0])
                if i == tuple_len - 1:
                    axes[i, j].set_xlabel(l[0])
                if k[1] != l[1]:
                    axes[i, j].scatter(data[l[1]], data[k[1]], alpha=0.1)
            except:
                ValueError
        j = -1

    plt.show()
