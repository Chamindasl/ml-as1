room_types = []
neighbourhood_groups = []
neighbourhoods = []
price_data = []


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
    id, name, host_id, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price, \
        minimum_nights, number_of_reviews, last_review, reviews_per_month, calculated_host_listings_count, \
        availability_365 = one_line
    room_type_id = add_keys_with_idx(room_types, room_type)
    neighbourhood_group_id = add_keys_with_idx(neighbourhood_groups, neighbourhood_group)
    neighbourhood_id = add_keys_with_idx(neighbourhoods, neighbourhood)
    price_data.append((
                      name,
                      host_id,
                      room_type_id,
                      neighbourhood_group_id,
                      neighbourhood_id,
                      latitude,
                      longitude,
                      price,
                      minimum_nights,
                      number_of_reviews,
                      last_review,
                      reviews_per_month,
                      calculated_host_listings_count,
                      availability_365))


def build_dto():
    return {
        "room_types": room_types,
        "neighbourhood_groups": neighbourhood_groups,
        "neighbourhoods": neighbourhoods,
        "price_data": price_data
    }
