import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)
import sys


def scatter_plot(data: list, indexes: list, use_seaborn=False):
    tuple_len = len(indexes)
    use_seaborn_calculated = use_seaborn_cal(use_seaborn, tuple_len)
    fig, axes = plt.subplots(tuple_len, tuple_len, figsize=(tuple_len*4, tuple_len*4))
    i = -1
    j = -1
    for k in indexes:
        i += 1
        for l in indexes:
            j += 1
            try:
                set_axis_labels(axes, i, j, k, l, tuple_len)
                if k[1] != l[1]:
                    if use_seaborn_calculated:
                        sns.regplot(x=data[l[1]], y=data[k[1]], ax=get_axes(axes, i, j, tuple_len))
                    else:
                        get_axes(axes, i, j, tuple_len).scatter(data[l[1]], data[k[1]], alpha=0.1)
                else:
                    if use_seaborn_calculated:
                        sns.distplot(data[l[1]], color="b", ax=get_axes(axes, i, j, tuple_len))
                    else:
                        get_axes(axes, i, j, tuple_len).hist(data[l[1]])
            except:
                print("Oops!", sys.exc_info()[0],"occured.")
        j = -1

    plt.show()


def dist_plot(data_list: list, titles: list, index: tuple):
    tuple_len = len(data_list)
    fig, axes = plt.subplots(tuple_len)
    i = -1
    for data in data_list:
        i += 1
        try:
            axes[i].set_title([titles[i]])
            sns.distplot(data[index[1]], color="b", ax=axes[i])
            if i == tuple_len - 1:
                axes[i].set_xlabel(index[0])
        except:
            print("Oops!", sys.exc_info()[0], "occured.")

    plt.show()


def set_axis_labels(axes, i, j, k, l, tuple_len):
    if j == 0:
        if tuple_len != 1:
            get_axes(axes, i, j, tuple_len).set_ylabel(k[0])
    if i == tuple_len - 1:
        get_axes(axes, i, j, tuple_len).set_xlabel(l[0])


def use_seaborn_cal(use_seaborn, tuple_len):
    if tuple_len == 1:
        return True
    return use_seaborn


def get_axes(axes, i, j, tuple_len):
    if tuple_len == 1:
        return axes
    return axes[i, j]
