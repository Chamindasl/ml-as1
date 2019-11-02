from analytics.common.multi_graph import dist_plot, pie_plot, group_bar_plot
from analytics.common.multi_graph import scatter_plot
from const import F_PRICE, F_NUMERIC_FIELDS, F_ALL_FIELDS, F_ROOM_TYPE_ID, F_NEIGHBOURHOOD_GROUP_ID, F_NEIGHBOURHOOD_ID
from db.write import write
from db.init.init import create_all_tables
from db.read import read
from file.file_read import process_data_file
from utils.data import vertical_slice_all_data, summary, filter_by_index, group_count_list, group_by, \
    two_group_count_list
from utils.print import print_summary

ab_data_to_db = process_data_file()
create_all_tables()
write.insert_all_data(ab_data_to_db)
ab_data = read.read_ab_data()
vertical_slice_all_data_list = vertical_slice_all_data(ab_data)

print_summary(summary(ab_data, F_NUMERIC_FIELDS))
# scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS)
# scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS, True)

print_summary(summary(ab_data, [F_PRICE]))
scatter_plot(vertical_slice_all_data_list, [F_PRICE])

ab_data_p_lte_1000 = filter_by_index(ab_data, F_PRICE, '<=', 1000)
vertical_slice_ab_data_p_lt3_1000 = vertical_slice_all_data(ab_data_p_lte_1000)
print_summary(summary(ab_data_p_lte_1000, [F_PRICE]))
scatter_plot(vertical_slice_ab_data_p_lt3_1000, [F_PRICE])

ab_data_p_lte_500 = filter_by_index(ab_data_p_lte_1000, F_PRICE, '<=', 500)
vertical_slice_ab_data_p_lt3_500 = vertical_slice_all_data(ab_data_p_lte_500)
print_summary(summary(ab_data_p_lte_500, [F_PRICE]))
scatter_plot(vertical_slice_ab_data_p_lt3_500, [F_PRICE])

dist_plot(
    [
        vertical_slice_all_data_list,
        vertical_slice_ab_data_p_lt3_1000,
        vertical_slice_ab_data_p_lt3_500,
    ],
    ["All Data", "Price <= 1000", "Price <= 500", "Price <= 300"],
    F_PRICE)

# scatter_plot(vertical_slice_ab_data_p_lt3_500, F_ALL_FIELDS, True)

group_count_list_by_room_type = group_count_list(group_by(ab_data_p_lte_500, [F_ROOM_TYPE_ID[1]]))
group_count_list_by_neighbourhood_grp_id = group_count_list(group_by(ab_data_p_lte_500, [F_NEIGHBOURHOOD_GROUP_ID[1]]))

pie_plot(group_count_list_by_room_type)
pie_plot(group_count_list_by_neighbourhood_grp_id)

group_count_list_by_room_type.insert(1, [""])
group_bar_plot(group_count_list_by_room_type)

group_count_list_by_neighbourhood_grp_id.insert(1, [""])
group_bar_plot(group_count_list_by_neighbourhood_grp_id)

group_count_list_by_room_type_and_neighbourhood_frp_id = two_group_count_list(group_by(ab_data_p_lte_500,
                                                                                       [F_ROOM_TYPE_ID[1],
                                                                                        F_NEIGHBOURHOOD_GROUP_ID[1]]))

group_bar_plot(group_count_list_by_room_type_and_neighbourhood_frp_id)
