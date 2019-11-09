__room_types = []
__neighbourhood_groups = []
__neighbourhoods = []
__ab_data = []
__ab_headers = []
__ab_skipped = []


def process_data_file(file="../data/AB_NYC_2019.csv"):
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
    :return: dictionary which contains room_types, neighbourhood_groups, neighbourhoods, headers, data, skipped data
    """
    with open(file, encoding="utf8") as data_file:
        read_header = False
        for line in data_file:
            line = line.strip()
            comma_separated_line = line.split(",")
            if read_header:
                if len(comma_separated_line) == 16:
                    process_line__(comma_separated_line)
                else:
                    __ab_skipped.append(comma_separated_line)

        return build_dto__()


def add_keys_with_idx__(a_list: list, value):
    """
    Private utility method to add new item to list with new id and id or return existing id
    :param a_list: data list
    :param value: value
    :return: if value in list with id then return id else new id
    """
    for k, v in a_list:
        if v == value:
            return k
    else:
        list_len = len(a_list) + 1
        a_list.append((list_len, value))
        return list_len


def process_line__(one_line):
    """
    Process one row, convert cell value to correct type  and add to ab_data as a tuple
    """
    line_id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, \
        minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, \
        availability_365 = one_line
    room_type_id = add_keys_with_idx__(__room_types, room_type)
    neighbourhood_group_id = add_keys_with_idx__(__neighbourhood_groups, neighbourhood_group)
    neighbourhood_id = add_keys_with_idx__(__neighbourhoods, neighbourhood)
    reviews_per_month = float_or_0__(reviews_per_month)
    __ab_data.append((
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


def build_dto__():
    """
    Build the final dto dictionary which has room_types, neighbourhood_groups, ab_headers, ab_data, ab_skipped
    :return:
    """
    return {
        "room_types": __room_types,
        "neighbourhood_groups": __neighbourhood_groups,
        "neighbourhoods": __neighbourhoods,
        "ab_headers": __ab_headers,
        "ab_data": __ab_data,
        "ab_skipped": __ab_skipped,
    }
