from analytics.common.multi_graph import dist_plot, pie_plot, group_bar_plot, violin_plot
from analytics.common.multi_graph import scatter_plot
from const import F_PRICE, F_NUMERIC_FIELDS, F_ALL_FIELDS, F_ROOM_TYPE_ID, F_NEIGHBOURHOOD_GROUP_ID
from db.write import write
from db.init.init import create_all_tables
from db.read import read
from file.file_read import process_data_file
from utils.data import vertical_slice_all_data, summary, filter_by_index, group_count_list, group_by, \
    two_group_count_list, vertical_slice_data
from utils.print import print_summary

ab_data_to_db = process_data_file()
create_all_tables()
write.insert_all_data(ab_data_to_db)
ab_data = read.read_ab_data()
vertical_slice_all_data_list = vertical_slice_all_data(ab_data)

print_summary(summary(ab_data, F_NUMERIC_FIELDS))
scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS)
scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS, True)

price_summary_all_data = summary(ab_data, [F_PRICE])
print_summary(price_summary_all_data)
scatter_plot(vertical_slice_all_data_list, [F_PRICE])

ab_data_p_lte_1000 = filter_by_index(ab_data, F_PRICE, '<=', 1000)
vertical_slice_ab_data_p_lte_1000 = vertical_slice_all_data(ab_data_p_lte_1000)
price_summary_lte_1000 = summary(ab_data_p_lte_1000, [F_PRICE])
print_summary(price_summary_lte_1000)
scatter_plot(vertical_slice_ab_data_p_lte_1000, [F_PRICE])

ab_data_p_lte_500 = filter_by_index(ab_data_p_lte_1000, F_PRICE, '<=', 500)
vertical_slice_ab_data_p_lte_500 = vertical_slice_all_data(ab_data_p_lte_500)
price_summary_lte_500 = summary(ab_data_p_lte_500, [F_PRICE])
print_summary(price_summary_lte_500)
scatter_plot(vertical_slice_ab_data_p_lte_500, [F_PRICE])

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
    F_PRICE)

# scatter_plot(vertical_slice_ab_data_p_lte_500, F_ALL_FIELDS, True)

group_by_room_type_lt_1000 = group_by(ab_data_p_lte_500, [F_ROOM_TYPE_ID[1]])
group_count_list_by_room_type_lt_1000 = group_count_list(group_by_room_type_lt_1000)
group_by_neighbourhood_grp_lt_1000 = group_by(ab_data_p_lte_500, [F_NEIGHBOURHOOD_GROUP_ID[1]])
group_count_list_by_neighbourhood_grp_id_lt_1000 = group_count_list(group_by_neighbourhood_grp_lt_1000)

pie_plot(group_count_list_by_room_type_lt_1000)
pie_plot(group_count_list_by_neighbourhood_grp_id_lt_1000)

group_count_list_by_room_type_lt_1000.insert(1, [""])
group_bar_plot(group_count_list_by_room_type_lt_1000)

group_count_list_by_neighbourhood_grp_id_lt_1000.insert(1, [""])
group_bar_plot(group_count_list_by_neighbourhood_grp_id_lt_1000)

group_count_list_by_room_type_and_neighbourhood_grp_id_lt_1000 = two_group_count_list \
    (group_by(ab_data_p_lte_500,
              [F_ROOM_TYPE_ID[1],
               F_NEIGHBOURHOOD_GROUP_ID[1]]))
group_bar_plot(group_count_list_by_room_type_and_neighbourhood_grp_id_lt_1000)

group_count_list_by_neighbourhood_grp_id_and_room_type_lt_1000 = two_group_count_list(
    group_by(ab_data_p_lte_500,
             [F_NEIGHBOURHOOD_GROUP_ID[1],
              F_ROOM_TYPE_ID[1]]))

price_group_by_room_type_lt_1000 = {k: vertical_slice_data(v, F_PRICE[1]) for k, v in
                                    group_by_room_type_lt_1000.items()}
violin_plot(price_group_by_room_type_lt_1000)

price_group_by_neighbourhood_grp_id_lt_1000 = {k: vertical_slice_data(v, F_PRICE[1]) for k, v in
                                               group_by_neighbourhood_grp_lt_1000.items()}
violin_plot(price_group_by_neighbourhood_grp_id_lt_1000)

''''''
ab_data_p_gte_1000 = filter_by_index(ab_data, F_PRICE, '>', 1000)
vertical_slice_ab_data_p_gt_1000 = vertical_slice_all_data(ab_data_p_gte_1000)
price_summary_gte_1000 = summary(ab_data_p_gte_1000, [F_PRICE])
print_summary(price_summary_gte_1000)
scatter_plot(vertical_slice_ab_data_p_gt_1000, [F_PRICE])

ab_data_p_gte_5000 = filter_by_index(ab_data_p_gte_1000, F_PRICE, '>=', 5000)
vertical_slice_ab_data_p_gt_5000 = vertical_slice_all_data(ab_data_p_gte_5000)
price_summary_gte_5000 = summary(ab_data_p_gte_5000, [F_PRICE])
print_summary(price_summary_gte_5000)
scatter_plot(vertical_slice_ab_data_p_gt_5000, [F_PRICE])

dist_plot(
    [
        vertical_slice_all_data_list,
        vertical_slice_ab_data_p_lte_1000,
        vertical_slice_ab_data_p_gt_1000,
        vertical_slice_ab_data_p_gt_5000,
    ],
    ["All Data", "Price < 1000", "Price > 1000", "Price > 5000"],
    [
        price_summary_all_data[0][1]["mean"],
        price_summary_lte_1000[0][1]["mean"],
        price_summary_gte_1000[0][1]["mean"],
        price_summary_gte_5000[0][1]["mean"],
    ],
    F_PRICE)

# scatter_plot(vertical_slice_ab_data_p_gt_1000, F_ALL_FIELDS, True)

group_by_room_type_gt_1000 = group_by(ab_data_p_gte_1000, [F_ROOM_TYPE_ID[1]])
group_count_list_by_room_type_gt_1000 = group_count_list(group_by_room_type_gt_1000)
group_by_neighbourhood_grp_gt_1000 = group_by(ab_data_p_gte_1000, [F_NEIGHBOURHOOD_GROUP_ID[1]])
group_count_list_by_neighbourhood_grp_id_gt_1000 = group_count_list(group_by_neighbourhood_grp_gt_1000)

pie_plot(group_count_list_by_room_type_gt_1000)
pie_plot(group_count_list_by_neighbourhood_grp_id_gt_1000)

group_count_list_by_room_type_gt_1000.insert(1, [""])
group_bar_plot(group_count_list_by_room_type_gt_1000)

group_count_list_by_neighbourhood_grp_id_gt_1000.insert(1, [""])
group_bar_plot(group_count_list_by_neighbourhood_grp_id_gt_1000)

group_count_list_by_room_type_and_neighbourhood_grp_id_gt_1000 = two_group_count_list(
    group_by(ab_data_p_gte_1000,
             [F_ROOM_TYPE_ID[1],
              F_NEIGHBOURHOOD_GROUP_ID[1]]))
group_bar_plot(group_count_list_by_room_type_and_neighbourhood_grp_id_gt_1000)

group_count_list_by_neighbourhood_grp_id_and_room_type_gt_1000 = two_group_count_list(
    group_by(ab_data_p_gte_1000,
             [F_NEIGHBOURHOOD_GROUP_ID[1],
              F_ROOM_TYPE_ID[1]]))

price_group_by_room_type_gt_1000 = {k: vertical_slice_data(v, F_PRICE[1]) for k, v in
                                    group_by_room_type_gt_1000.items()}
violin_plot(price_group_by_room_type_gt_1000)

price_group_by_neighbourhood_grp_id_gt_1000 = {k: vertical_slice_data(v, F_PRICE[1])
                                               for k, v in group_by_neighbourhood_grp_gt_1000.items()}
violin_plot(price_group_by_neighbourhood_grp_id_gt_1000)
