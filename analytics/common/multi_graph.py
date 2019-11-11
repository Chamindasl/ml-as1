from datetime import datetime
import logging
import re
import matplotlib.pyplot as plt
import seaborn as sns

SPECIAL_CHARS = '[^a-zA-Z0-9\n\\.]'

sns.set(color_codes=True)

logger = logging.getLogger(__name__)


def scatter_plot(data: list, indexes: list, use_sea_born=False, title=None):
    tuple_len = len(indexes)
    if tuple_len > 1:
        logger.warning("Generating %s pair scatter plots for %s variables, this could take minutes",
                       tuple_len * tuple_len, tuple_len)
    use_sea_born_calculated = use_sea_born_cal(use_sea_born, tuple_len)
    fig, axes = plt.subplots(tuple_len, tuple_len, figsize=(tuple_len * 4, tuple_len * 4))
    fig.suptitle(title, color='r')
    i = -1
    j = -1
    for k in indexes:
        i += 1
        for l in indexes:
            j += 1
            plot_sub_scatter_plot(axes, data, i, j, k, l, tuple_len, use_sea_born_calculated)
        j = -1
    png = "../analytics/graphs/%s___%s.png" % (re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    fig.savefig(png.lower(),  dpi=fig.dpi)
    plt.show()


def plot_sub_scatter_plot(axes, data, i, j, k, l, tuple_len, use_sea_born_calculated):
    try:
        set_axis_labels(axes, i, j, k, l, tuple_len)
        if k[1] != l[1]:
            if use_sea_born_calculated:
                sns.regplot(x=data[l[1]], y=data[k[1]], ax=get_axes(axes, i, j, tuple_len))
            else:
                get_axes(axes, i, j, tuple_len).scatter(data[l[1]], data[k[1]], alpha=0.1)
        else:
            if use_sea_born_calculated:
                sns.distplot(data[l[1]], color="b", ax=get_axes(axes, i, j, tuple_len))
            else:
                get_axes(axes, i, j, tuple_len).hist(data[l[1]])
    except:
        pass


def group_bar_plot(data: list, title=None):
    labels = data[0]
    legends = data[1]
    for i in range(len(legends)):
        x_pos = [j * (len(legends) + 1) + i for j in range(len(labels))]
        plt.bar(x_pos, data[i + 2], width=1)
    x_pos_leb = [(len(legends) * (len(legends) + 1) * j + sum(range(len(legends)))) / len(legends) for j in
                 range(len(labels))]
    plt.xticks(x_pos_leb, labels)
    plt.legend(legends)
    plt.title(title)
    png = "../analytics/graphs/%s___%s.png" % (re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    plt.savefig(png.lower())
    plt.show()


def dist_plot(data_list: list, titles: list, means: list, index: tuple, title=None):
    tuple_len = len(data_list)
    fig, axes = plt.subplots(tuple_len, 2)
    fig.suptitle(title, color='r')
    i = -1
    for data in data_list:
        i += 1
        try:
            axes[i][0].set_title("{0}, mean: {1:.2f}".format(titles[i], means[i]))
            axes[i][0].axvline(means[i], color='r', linestyle='--')
            axes[i][1].set_title(titles[i])
            sns.distplot(data[index[1]], color="b", ax=axes[i, 0])
            sns.violinplot(data[index[1]], color="b", ax=axes[i, 1])
            if i == tuple_len - 1:
                axes[i][0].set_xlabel(index[0])
                axes[i][1].set_xlabel(index[0])

        except:
            pass
    png = "../analytics/graphs/%s___%s.png" % (re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    fig.savefig(png.lower(), dpi=fig.dpi)
    plt.show()


def violin_plot(data_dict: dict, title=None):
    fig, axes = plt.subplots(1)
    fig.suptitle(title, color='r')
    g = sns.violinplot(data=list(data_dict.values()), ax=axes)
    g.set_xticklabels(list(data_dict.keys()))
    png = "../analytics/graphs/%s___%s.png" % (re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    fig.savefig(png.lower(),  dpi=fig.dpi)
    plt.show()


def pie_plot(data: list, title=None):
    labels = data[0]
    data_list = data[1]
    sum_all = sum(data_list)
    sizes = [i * 100.0 / sum_all for i in data_list]
    fig, ax = plt.subplots()
    fig.suptitle(title, color='r')
    ax.pie(sizes, labels=labels, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    png = "../analytics/graphs/%s___%s.png" % (re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    fig.savefig(png.lower(),  dpi=fig.dpi)
    plt.show()


def set_axis_labels(axes, i, j, k, l, tuple_len):
    if tuple_len != 1:
        get_axes(axes, i, j, tuple_len).set_ylabel(k[0])
    get_axes(axes, i, j, tuple_len).set_xlabel(l[0])


def use_sea_born_cal(use_sea_born, tuple_len):
    if tuple_len == 1:
        return True
    return use_sea_born


def get_axes(axes, i, j, tuple_len):
    if tuple_len == 1:
        return axes
    return axes[i, j]
