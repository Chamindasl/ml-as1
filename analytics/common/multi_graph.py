import logging
import re
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns

from definitions import SHOW_GRAPH, SAVE_GRAPH, GRAPH_PATH

SPECIAL_CHARS = '[^a-zA-Z0-9\n\\.]'

sns.set(color_codes=True)

logger = logging.getLogger(__name__)


def scatter_plot(data: list, indexes: list, use_sea_born=False, title=None):
    """
    Generate pair scatter plots against each item. Can be used to find correlation.
    Default seaborn only accept DataFrame. This has been customized single scatter plot which accepts list as x and y,
    to generate pair scatter plots
    :param data: vertical sliced data
    :param indexes: indexed to be used
    :param use_sea_born: use seaborn or matplotlib, default to matplotlib. seaborn has default correlation
    :param title: title of the graph
    :return:
    """
    tuple_len = len(indexes)
    if tuple_len > 1:
        logger.warning("Generating %s pair scatter plots for %s variables, this could take minutes",
                       tuple_len * tuple_len, tuple_len)
    use_sea_born_calculated = use_sea_born_cal__(use_sea_born, tuple_len)
    # total number of plots = tuple_len * tuple_len
    fig, axes = plt.subplots(tuple_len, tuple_len, figsize=(tuple_len * 4, tuple_len * 4))
    fig.suptitle(title, color='r')
    i = -1  # axis x
    j = -1  # axis y
    for k in indexes:
        i += 1
        for l in indexes:
            j += 1
            # sup plot on axes [i, j]
            plot_sub_scatter_plot(axes, data, i, j, k, l, tuple_len, use_sea_born_calculated)
        j = -1  # finished a row, staring next row
    # new file name, based on given name and current time
    png = "%s%s___%s.png" % (GRAPH_PATH, re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    # save and/or display graph
    save_and_print_graph(fig, png)


def save_and_print_graph(fig, png):
    """
    save or display graph based on configurations
    :param fig: figure to save or display
    :param png: name of the png
    :return:
    """
    if SAVE_GRAPH:
        fig.savefig(png.lower(), dpi=fig.dpi)
    if SHOW_GRAPH:
        plt.show()


def save_and_print_graph_plt(png):
    """
    save or display graph based on configurations
    :param png: name of the png
    :return:
    """
    if SAVE_GRAPH:
        plt.savefig(png.lower())
    if SHOW_GRAPH:
        plt.show()


def plot_sub_scatter_plot(axes, data, i, j, k, l, tuple_len, use_sea_born_calculated):
    """
    place sub scatter plot on main pair scatter plot
    :param axes: axes
    :param data: data list
    :param i: x of axes
    :param j: y of axes
    :param k: x index of  data list
    :param l: y index of  data list
    :param tuple_len: tuple_len
    :param use_sea_born_calculated: should use seaborn of matplotlit
    :return:
    """
    try:
        set_axis_labels__(axes, i, j, k, l, tuple_len)
        if k[1] != l[1]:  # if plotting against same then it should be distribution plot
            if use_sea_born_calculated:
                sns.regplot(x=data[l[1]], y=data[k[1]], ax=get_axes__(axes, i, j, tuple_len))
            else:  # otherwise it should be scatter plot
                get_axes__(axes, i, j, tuple_len).scatter(data[l[1]], data[k[1]], alpha=0.1)
        else:
            if use_sea_born_calculated:
                sns.distplot(data[l[1]], color="b", ax=get_axes__(axes, i, j, tuple_len))
            else:
                get_axes__(axes, i, j, tuple_len).hist(data[l[1]])
    except TypeError:
        pass


def group_bar_plot(data: list, title=None):
    """
    Two group bar plot
    :param data: data list
    :param title: title of graph
    :return:
    """
    labels = data[0]  # first group as x axis
    legends = data[1]  # 2nd group as legends
    for i in range(len(legends)):
        x_pos = [j * (len(legends) + 1) + i for j in range(len(labels))]
        # positioning individual bar on plot
        plt.bar(x_pos, data[i + 2], width=1)
    # positioning x labels middle of each x data set
    x_pos_leb = [(len(legends) * (len(legends) + 1) * j + sum(range(len(legends)))) / len(legends) for j in
                 range(len(labels))]
    plt.xticks(x_pos_leb, labels)
    # set legends and title
    plt.legend(legends)
    plt.title(title)
    png = "%s%s___%s.png" % (GRAPH_PATH, re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    save_and_print_graph_plt(png)


def dist_plot(data_list: list, titles: list, means: list, index: tuple, title=None):
    """
    Reusable multi distribution plot (KDE) and Violin Plot side by side
    :param data_list: data as list of list
    :param titles: title for each sub data list
    :param means: mean values for each data set
    :param index: index tuple
    :param title: title of the main graph
    :return:
    """
    tuple_len = len(data_list)
    fig, axes = plt.subplots(tuple_len, 2)
    fig.suptitle(title, color='r')
    i = -1
    for data in data_list:
        i += 1
        try:
            axes[i][0].set_title("{0}, mean: {1:.2f}".format(titles[i], means[i]))
            axes[i][0].axvline(means[i], color='r', linestyle='--')  # custom mean
            axes[i][1].set_title(titles[i])
            sns.distplot(data[index[1]], color="b", ax=axes[i, 0])  # distribution plot
            sns.violinplot(data[index[1]], color="b", ax=axes[i, 1])  # violin plot
            if i == tuple_len - 1:
                axes[i][0].set_xlabel(index[0])
                axes[i][1].set_xlabel(index[0])

        except TypeError:
            pass
    png = "%s%s___%s.png" % (GRAPH_PATH, re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    save_and_print_graph(fig, png)


def violin_plot(data_dict: dict, title=None):
    """
    Reusable violin graph
    :param data_dict: data as a dictionary
    :param title: title of the graph
    :return:
    """
    fig, axes = plt.subplots(1)
    fig.suptitle(title, color='r')
    g = sns.violinplot(data=list(data_dict.values()), ax=axes)
    g.set_xticklabels(list(data_dict.keys()))
    png = "%s%s___%s.png" % (GRAPH_PATH, re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    save_and_print_graph(fig, png)


def pie_plot(data: list, title=None):
    """
    Reusable pie plot for
    :param data: data list
    :param title: title
    :return:
    """
    labels = data[0]  # labels
    data_list = data[1]  # data list
    sum_all = sum(data_list)  # sum of the data list
    sizes = [i * 100.0 / sum_all for i in data_list]  # percentage for each data item
    fig, ax = plt.subplots()
    fig.suptitle(title, color='r')
    ax.pie(sizes, labels=labels, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    png = "%s%s___%s.png" % (GRAPH_PATH, re.sub(SPECIAL_CHARS, '_', title), datetime.now().strftime(
        '%Y_%m_%d_%H_%M_%S'))
    save_and_print_graph(fig, png)


def set_axis_labels__(axes, i, j, k, l, tuple_len):
    if tuple_len != 1:
        get_axes__(axes, i, j, tuple_len).set_ylabel(k[0])
    get_axes__(axes, i, j, tuple_len).set_xlabel(l[0])


def use_sea_born_cal__(use_sea_born, tuple_len):
    if tuple_len == 1:
        return True
    return use_sea_born


def get_axes__(axes, i, j, tuple_len):
    if tuple_len == 1:
        return axes
    return axes[i, j]
