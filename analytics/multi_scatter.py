import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)


def plot(data: list, indexes: list, use_seaborn=False):
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
                    if use_seaborn:
                        sns.regplot(x=data[l[1]], y=data[k[1]], ax=axes[i, j])
                    else:
                        axes[i, j].scatter(data[l[1]], data[k[1]], alpha=0.1)
                else:
                    if use_seaborn:
                        sns.distplot(data[l[1]], color="b", ax=axes[i, j])
                    else:
                        axes[i, j].hist(data[l[1]])
            except:
                ValueError
        j = -1

    plt.show()
