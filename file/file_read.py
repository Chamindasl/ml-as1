from exceptions.file_exceptions import FileNotReadableError
from definitions import ROOT_DIR


def process_data_file(file=ROOT_DIR / "../data/AB_NYC_2019.csv"):
    """
    This method is used to read AirBnB New York 2019 data. Method is tightly coupled with data set.
    First line should be header.
    Row should contain 16 data items, if not row will be ignored
    File should be comma separated values (CSV)
    Method is capable to
        1. Read Headers
        2. Read Room Type, Neighbourhood Group, Neighbourhood and replace with their corresponding ids.
        3. Convert to correct format (eg. int, float)
        4. Assign 0 for missing Review per Month

    :param file: input file
    :raise FileNotReadableError: When file not found or not readable
    :return: dictionary which contains room_types, neighbourhood_groups, neighbourhoods, headers, data, skipped data
    """
    data_items = {
        "room_types": [],
        "neighbourhood_groups": [],
        "neighbourhoods": [],
        "ab_headers": [],
        "ab_data": [],
        "ab_skipped": []
    }
    try:
        with open(file, encoding="utf8") as data_file:
            read_header = False  # has header red
            for line in data_file:
                line = line.strip()
                comma_separated_line = line.split(",")
                if read_header:  # reading normal data row
                    if len(comma_separated_line) == 16:  # there should be exactly 16 data items
                        process_line__(comma_separated_line, data_items)  # process line
                    else:
                        data_items["ab_skipped"].append(comma_separated_line)  # skipped otherwise
                else:  # first row as a header
                    if not len(comma_separated_line) == 16:
                        raise FileNotReadableError
                    data_items["ab_headers"].append(comma_separated_line)
                    read_header = True
            return data_items
    except:
        raise FileNotReadableError


def add_keys_with_idx__(a_list: list, value):
    """
    Private utility method to add new item to list with new id and id or return existing id
    :param a_list: data list
    :param value: value
    :return: if value in list with id then return id else new id
    """
    for k, v in a_list:
        if v == value:  # if value found
            return k  # returned index
    else:
        list_len = len(a_list) + 1  # current len + 1 would be next index for new item
        a_list.append((list_len, value))  # append to list
        return list_len  # new index


def process_line__(one_line, data_items):
    """
    Process one row, convert cell value to correct type  and add to ab_data as a tuple
    """
    line_id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, \
        minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, \
        availability_365 = one_line  # read each item
    room_type_id = add_keys_with_idx__(data_items["room_types"], room_type)  # replace room type with its index
    # replace ng with idx
    neighbourhood_group_id = add_keys_with_idx__(data_items["neighbourhood_groups"], neighbourhood_group)
    neighbourhood_id = add_keys_with_idx__(data_items["neighbourhoods"], neighbourhood)  # replace n with ids
    reviews_per_month = float_or_0__(reviews_per_month)  # cleansing reviews_per_month
    data_items["ab_data"].append((
        name,
        host_id,
        room_type_id,
        neighbourhood_group_id,
        neighbourhood_id,
        float(latitude),
        float(longitude),
        int(price),
        int(minimum_nights),
        int(number_of_reviews),
        last_review,
        float(reviews_per_month),
        int(calculated_host_listings_count),
        int(availability_365)))


def float_or_0__(value):
    """
    Convert value to float and return or return 0
    :param value: value
    :return: float of value or 0
    """
    try:
        return float(value)
    except ValueError:
        return 0
