from analytics.common.multi_graph import dist_plot, group_bar_plot, pie_plot
from analytics.common.multi_graph import scatter_plot
from const import F_PRICE, F_NUMERIC_FIELDS, F_ALL_FIELDS, F_ROOM_TYPE_ID, F_NEIGHBOURHOOD_GROUP_ID
from db.write import write
from db.init.init import create_all_tables
from db.read import read
from file.file_read import process_data_file
from utils.data import vertical_slice_all_data, summary, filter_by_index, group_by, two_group_count_list, \
    group_count_list
from utils.print import print_summary

ab_data = read.read_ab_data()
# vertical_slice_all_data_list = vertical_slice_all_data(ab_data)
#
# print_summary(summary(ab_data, F_NUMERIC_FIELDS))
# # scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS)
# # scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS, True)
#
ab_data_p_lte_500 = filter_by_index(ab_data, F_PRICE, '<=', 500)
vertical_slice_ab_data_p_lt3_500 = vertical_slice_all_data(ab_data_p_lte_500)
print_summary(summary(ab_data_p_lte_500, [F_PRICE]))

from analytics.common.multi_graph import group_bar_plot
from utils.data import two_group_count_list

count_list = two_group_count_list(group_by(ab_data_p_lte_500, [F_ROOM_TYPE_ID[1], F_NEIGHBOURHOOD_GROUP_ID[1]]))
print(count_list)
group_bar_plot(count_list)

count_list = group_count_list(group_by(ab_data_p_lte_500, [F_ROOM_TYPE_ID[1]]))
pie_plot(count_list)
count_list.insert(1, [""])
group_bar_plot(count_list)
