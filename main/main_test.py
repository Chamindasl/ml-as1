from analytics.common.multi_graph import violin_plot
from const import F_PRICE, F_ROOM_TYPE_ID
from db.read import read
from utils.data import vertical_slice_all_data, group_by, \
    vertical_slice_data

# ab_data_to_db = process_data_file()
# create_all_tables()
# write.insert_all_data(ab_data_to_db)
ab_data = read.read_ab_data()
b = group_by(ab_data, [F_ROOM_TYPE_ID[1]])
c = {i: vertical_slice_data(j, F_PRICE[1]) for i, j in b.items()}
vertical_slice_all_data_list = vertical_slice_all_data(ab_data)
violin_plot(c)
