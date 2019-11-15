from texttable import Texttable


def print_summary(summary: list):
    """
    print summary of data set
    :param summary: summary
    :return:
    """
    t = Texttable()
    headers = []
    for i in summary:
        if len(headers) == 0:
            headers.append("Field")
            headers.extend(dict(i[1]).keys())
            t.header(headers)
        row = [i[0][0]]
        row.extend(list(dict(i[1]).values()))
        t.add_row(row)
    print(t.draw())


def print_file_read_summary(data_valid_read, data_skipped):
    """
    Print the read summary of data set
    :param data_valid_read: valid count
    :param data_skipped: skipped count
    :return:
    """
    t = Texttable()
    t.header(["", "Count"])
    t.add_row(["Valid Rows", data_valid_read])
    t.add_row(["Skipped Rows", data_skipped])
    t.add_row(["Total Reads", data_valid_read + data_skipped])
    print(t.draw())


def print_head(data, headers, count=10):
    """
    print head of data set
    :param data: data set
    :param headers: headers
    :param count: count, default to 10
    :return:
    """
    t = Texttable(max_width=0)
    t.header(headers)
    for i in data[:count]:
        t.add_row(list(i))
    print(t.draw())
