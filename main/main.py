from analytics.multi_graph import dist_plot
from analytics.multi_graph import scatter_plot
from const import F_PRICE, F_NUMERIC_FIELDS
from db.write import write
from db.init.init import create_all_tables
from db.read import read
from file.file_read import process_data_file
from utils.data import vertical_slice_all_data, summary, filter_by_index
from utils.print import print_summary

ab_data_to_db = process_data_file()
create_all_tables()
write.insert_all_data(ab_data_to_db)
ab_data = read.read_ab_data()
vertical_slice_all_data_list = vertical_slice_all_data(ab_data)

print_summary(summary(ab_data, F_NUMERIC_FIELDS))
# plot(vertical_slice_all_data_list(ab_data), F_ALL_VARIABLES)

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
