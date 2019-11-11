from os import path

from analytics.common.multi_graph import dist_plot, pie_plot, group_bar_plot, violin_plot
from analytics.common.multi_graph import scatter_plot
from const import F_PRICE, F_NUMERIC_FIELDS, F_ROOM_TYPE_ID, F_NEIGHBOURHOOD_GROUP_ID, F_ALL_FIELDS, F_AVAILABILITY_365
from db import DATA_AB_NYC_DB
from db.write import write
from db.init.init import create_all_tables
from db.read import read
from file.file_read import process_data_file
from utils.data import vertical_slice_all_data, summary, filter_by_index, group_count_list, group_by, \
    two_group_count_list, vertical_slice_data
from utils.print import print_summary, print_file_read_summary

import logging

logger = logging.getLogger(__name__)


def create_tables_and_insert_data(data_to_db):
    if not path.exists(DATA_AB_NYC_DB):
        create_all_tables()
        write.insert_all_data(data_to_db)
    else:
        logger.warning("Database file is already exist, data will not be inserted again")


def visualize_price(price_data, title=None):
    group_by_room_type = group_by(price_data, [F_ROOM_TYPE_ID[1]])
    group_count_list_by_room_type = group_count_list(group_by_room_type)
    group_by_neighbourhood_grp = group_by(price_data, [F_NEIGHBOURHOOD_GROUP_ID[1]])
    group_count_list_by_neighbourhood_grp_id = group_count_list(group_by_neighbourhood_grp)
    pie_plot(group_count_list_by_room_type, title="Room Listing by Room Type - " + title)
    pie_plot(group_count_list_by_neighbourhood_grp_id, title="Room Listing by Neighbourhood Group - " + title)
    group_count_list_by_room_type.insert(1, [""])
    group_bar_plot(group_count_list_by_room_type, title="Room Listing by Room Type - " + title)
    group_count_list_by_neighbourhood_grp_id.insert(1, [""])
    group_bar_plot(group_count_list_by_neighbourhood_grp_id, title="Room Listing by Neighbourhood Group Type - "
                                                                   + title)
    group_count_list_by_room_type_and_neighbourhood_grp_id = two_group_count_list(
        group_by(price_data,
                 [F_ROOM_TYPE_ID[1],
                  F_NEIGHBOURHOOD_GROUP_ID[1]]))
    group_bar_plot(group_count_list_by_room_type_and_neighbourhood_grp_id, title="Room Listing by Room Type "
                                                                                 "and Neighbourhood Group - " + title)
    group_count_list_by_neighbourhood_grp_id_and_room_type = two_group_count_list(
        group_by(price_data,
                 [F_NEIGHBOURHOOD_GROUP_ID[1],
                  F_ROOM_TYPE_ID[1]]))
    group_bar_plot(group_count_list_by_neighbourhood_grp_id_and_room_type,
                   title="Room Listing by Room Type and Neighbourhood Group - " + title)
    price_group_by_room_type = {k: vertical_slice_data(v, F_PRICE[1]) for k, v in
                                group_by_room_type.items()}
    violin_plot(price_group_by_room_type, "Price KDE by Room Type - " + title)
    price_group_by_neighbourhood_grp_id = {k: vertical_slice_data(v, F_PRICE[1])
                                           for k, v in group_by_neighbourhood_grp.items()}
    violin_plot(price_group_by_neighbourhood_grp_id, "Price KDE by Neighbourhood Group - " + title)


ab_data_to_db = process_data_file()
print_file_read_summary(len(ab_data_to_db["ab_data"]), len(ab_data_to_db["ab_skipped"]))
create_tables_and_insert_data(ab_data_to_db)
ab_data = read.read_ab_data()
vertical_slice_all_data_list = vertical_slice_all_data(ab_data)

print_summary(summary(ab_data, F_NUMERIC_FIELDS))
# scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS, title="Pair Scatter Plot for All Variables")
# scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS, True, title="Pair Scatter Plot for All Variables")

price_summary_all_data = summary(ab_data, [F_PRICE])
print_summary(price_summary_all_data)
scatter_plot(vertical_slice_all_data_list, [F_PRICE], title="Price Distribution - All Data")

ab_data_p_lte_1000 = filter_by_index(ab_data, F_PRICE[1], '<=', 1000)
vertical_slice_ab_data_p_lte_1000 = vertical_slice_all_data(ab_data_p_lte_1000)
price_summary_lte_1000 = summary(ab_data_p_lte_1000, [F_PRICE])
print_summary(price_summary_lte_1000)
scatter_plot(vertical_slice_ab_data_p_lte_1000, [F_PRICE], title="Price Distribution - Price less than $1000")

ab_data_p_lte_500 = filter_by_index(ab_data_p_lte_1000, F_PRICE[1], '<=', 500)
vertical_slice_ab_data_p_lte_500 = vertical_slice_all_data(ab_data_p_lte_500)
price_summary_lte_500 = summary(ab_data_p_lte_500, [F_PRICE])
print_summary(price_summary_lte_500)
scatter_plot(vertical_slice_ab_data_p_lte_500, [F_PRICE], title="Price Distribution - Price less than $500")

dist_plot(
    [
        vertical_slice_all_data_list,
        vertical_slice_ab_data_p_lte_1000,
        vertical_slice_ab_data_p_lte_500,
    ],
    ["All Data", "Price <= 1000", "Price <= 500"],
    [
        price_summary_all_data[0][1]["mean"],
        price_summary_lte_1000[0][1]["mean"],
        price_summary_lte_500[0][1]["mean"],
    ],
    F_PRICE, title="Price Distribution Comparision - All, < 1000, < 500"
)

# scatter_plot(vertical_slice_ab_data_p_lte_500, F_ALL_FIELDS, True)


visualize_price(ab_data_p_lte_500, title="Price < 500")

ab_data_p_gte_1000 = filter_by_index(ab_data, F_PRICE[1], '>', 1000)
vertical_slice_ab_data_p_gt_1000 = vertical_slice_all_data(ab_data_p_gte_1000)
price_summary_gte_1000 = summary(ab_data_p_gte_1000, [F_PRICE])
print_summary(price_summary_gte_1000)
scatter_plot(vertical_slice_ab_data_p_gt_1000, [F_PRICE], title="Price Distribution - Price greater than $1000")

ab_data_p_gte_5000 = filter_by_index(ab_data_p_gte_1000, F_PRICE[1], '>=', 5000)
vertical_slice_ab_data_p_gt_5000 = vertical_slice_all_data(ab_data_p_gte_5000)
price_summary_gte_5000 = summary(ab_data_p_gte_5000, [F_PRICE])
print_summary(price_summary_gte_5000)
scatter_plot(vertical_slice_ab_data_p_gt_5000, [F_PRICE], title="Price Distribution - Price greater than $5000")

dist_plot(
    [
        vertical_slice_all_data_list,
        vertical_slice_ab_data_p_lte_500,
        vertical_slice_ab_data_p_gt_1000,
        vertical_slice_ab_data_p_gt_5000,
    ],
    ["All Data", "Price < 1000", "Price > 1000", "Price > 5000"],
    [
        price_summary_all_data[0][1]["mean"],
        price_summary_lte_500[0][1]["mean"],
        price_summary_gte_1000[0][1]["mean"],
        price_summary_gte_5000[0][1]["mean"],
    ],
    F_PRICE, title="Price Distribution Comparision - All, < 500, > 1000, > 5000"
)

# scatter_plot(vertical_slice_ab_data_p_gt_1000, F_ALL_FIELDS, True)


visualize_price(ab_data_p_gte_1000, title="Price > 1000")
visualize_price(ab_data_p_gte_5000, title="Price > 5000")

ab_data_p_gte_1000 = filter_by_index(ab_data, F_AVAILABILITY_365[1], '=', 0)
visualize_price(ab_data_p_gte_1000, title="Availability = 0")

ab_data_p_gte_1000 = filter_by_index(ab_data, F_AVAILABILITY_365[1], '>', 0)
visualize_price(ab_data_p_gte_1000, title="Availability > 0")
