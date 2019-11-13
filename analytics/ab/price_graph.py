import logging

from analytics.common.multi_graph import pie_plot, group_bar_plot, violin_plot
from const import F_PRICE, F_ROOM_TYPE_ID, F_NEIGHBOURHOOD_GROUP_ID
from utils.data import group_count_list, group_by, \
    two_group_count_list, vertical_slice_data


def visualize_price(price_data, logger, title=None):
    """
    Reusable graph generator for Price Data. Following 8 graphs will be generated.
    1. Pie Chart by Room Type
    2. Pie Chart by Neighbourhood_Group
    3. Count Bar Chart by Room Type
    4. Count Bar Chart by Neighbourhood_Group
    5. Count Bar Chart Group by Room Type for Neighbourhood_Group
    6. Count Bar Chart Group by Neighbourhood_Group for Room Type
    7. Violin (KDE) Chart by Room Type
    8. Violin (KDE) Chart by Neighbourhood_Group

    :param price_data: price data
    :param title: main title for graph
    :param logger: main logger
    :return:
    """
    # grouping data by room type
    group_by_room_type = group_by(price_data, [F_ROOM_TYPE_ID[1]])
    # get the count for each group
    group_count_list_by_room_type = group_count_list(group_by_room_type)
    # grouping data by neighbourhood_grp
    group_by_neighbourhood_grp = group_by(price_data, [F_NEIGHBOURHOOD_GROUP_ID[1]])
    # get the count for each group
    group_count_list_by_neighbourhood_grp_id = group_count_list(group_by_neighbourhood_grp)
    logger.info("Generating Pie Plot [Room Listing by Room Type - %s]."
                " After Graph appeared please close to proceed",
                title)
    pie_plot(group_count_list_by_room_type, title="Room Listing by Room Type - " + title)
    logger.info("Generating Pie Plot [Room Listing by Neighbourhood Group -  %s]."
                " After Graph appeared please close to proceed",
                title)
    pie_plot(group_count_list_by_neighbourhood_grp_id, title="Room Listing by Neighbourhood Group - " + title)
    group_count_list_by_room_type.insert(1, [""])  # fake group
    logger.info("Generating Count Bar Chart [Room Listing by Room Type -   %s]."
                " After Graph appeared please close to proceed",
                title)
    group_bar_plot(group_count_list_by_room_type, title="Room Listing by Room Type - " + title)
    group_count_list_by_neighbourhood_grp_id.insert(1, [""])
    logger.info("Generating Count Bar Chart [Room Listing by Neighbourhood Group Type -   %s]."
                " After Graph appeared please close to proceed",
                title)
    group_bar_plot(group_count_list_by_neighbourhood_grp_id, title="Room Listing by Neighbourhood Group Type - "
                                                                   + title)
    group_count_list_by_room_type_and_neighbourhood_grp_id = two_group_count_list(
        group_by(price_data,
                 [F_ROOM_TYPE_ID[1],
                  F_NEIGHBOURHOOD_GROUP_ID[1]]))
    logger.info("Generating Count Bar Chart [Room Listing by Room Type "
                "and Neighbourhood Group -   %s]."
                " After Graph appeared please close to proceed",
                title)
    group_bar_plot(group_count_list_by_room_type_and_neighbourhood_grp_id, title="Room Listing by Room Type "
                                                                                 "and Neighbourhood Group - " + title)
    group_count_list_by_neighbourhood_grp_id_and_room_type = two_group_count_list(
        group_by(price_data,
                 [F_NEIGHBOURHOOD_GROUP_ID[1],
                  F_ROOM_TYPE_ID[1]]))
    logger.info("Generating Count Bar Chart [Room Listing by Neighbourhood Group "
                "and Room Type -   %s]."
                " After Graph appeared please close to proceed",
                title)
    group_bar_plot(group_count_list_by_neighbourhood_grp_id_and_room_type,
                   title="Room Listing by Neighbourhood Group and Room Type - " + title)
    price_group_by_room_type = {k: vertical_slice_data(v, F_PRICE[1]) for k, v in
                                group_by_room_type.items()}
    logger.info("Generating Violin Chart [Price KDE by Room Type -  %s]."
                " After Graph appeared please close to proceed",
                title)
    violin_plot(price_group_by_room_type, "Price KDE by Room Type - " + title)
    price_group_by_neighbourhood_grp_id = {k: vertical_slice_data(v, F_PRICE[1])
                                           for k, v in group_by_neighbourhood_grp.items()}
    logger.info("Generating Violin Chart [Price KDE by Neighbourhood Group -  %s]."
                " After Graph appeared please close to proceed",
                title)
    violin_plot(price_group_by_neighbourhood_grp_id, "Price KDE by Neighbourhood Group - " + title)
