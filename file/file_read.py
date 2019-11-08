room_types = []
neighbourhood_groups = []
neighbourhoods = []
ab_data = []


def process_data_file(file="../data/AB_NYC_2019.csv"):
    with open(file, encoding="utf8") as data_file:
        next(data_file)
        for line in data_file:
            line = line.strip()
            comma_separated_line = line.split(",")
            if len(comma_separated_line) == 16:
                process_line(comma_separated_line)
        return build_dto()


def add_keys_with_idx(a_list: list, value):
    for k, v in a_list:
        if v == value:
            return k
    else:
        list_len = len(a_list) + 1
        a_list.append((list_len, value))
        return list_len


def process_line(one_line):
    line_id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, \
        minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, \
        availability_365 = one_line
    room_type_id = add_keys_with_idx(room_types, room_type)
    neighbourhood_group_id = add_keys_with_idx(neighbourhood_groups, neighbourhood_group)
    neighbourhood_id = add_keys_with_idx(neighbourhoods, neighbourhood)
    reviews_per_month = cleanse_reviews_per_month(reviews_per_month)
    ab_data.append((
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


def cleanse_reviews_per_month(reviews_per_month):
    try:
        return float(reviews_per_month)
    except ValueError:
        return 0


def build_dto():
    return {
        "room_types": room_types,
        "neighbourhood_groups": neighbourhood_groups,
        "neighbourhoods": neighbourhoods,
        "ab_data": ab_data
    }
