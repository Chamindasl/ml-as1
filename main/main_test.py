from analytics.common.multi_graph import dist_plot, pie_plot, group_bar_plot, violin_plot
from analytics.common.multi_graph import scatter_plot
from const import F_PRICE, F_NUMERIC_FIELDS, F_ALL_FIELDS, F_ROOM_TYPE_ID, F_NEIGHBOURHOOD_GROUP_ID, F_NEIGHBOURHOOD_ID, \
    F_AVAILABILITY_365
from db.write import write
from db.init.init import create_all_tables
from db.read import read
from file.file_read import process_data_file
from utils.data import vertical_slice_all_data, summary, filter_by_index, group_count_list, group_by, \
    two_group_count_list, vertical_slice_data
from utils.print import print_summary

# ab_data_to_db = process_data_file()
# create_all_tables()
# write.insert_all_data(ab_data_to_db)
ab_data = read.read_ab_data()
b = group_by(ab_data, [F_ROOM_TYPE_ID[1]])
c = {i: vertical_slice_data(j, F_PRICE[1]) for i,j in b.items()}
vertical_slice_all_data_list = vertical_slice_all_data(ab_data)
violin_plot(c)