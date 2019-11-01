from analytics.multi_scatter import plot
from const import F_ALL_FIELDS, F_PRICE, F_NUMBER_OF_REVIEWS, F_NUMERIC_FIELDS
from file.file_read import process_data_file
from db.init.init import create_all_tables
from db.write import write
from db.read import read
from utils.data import vertical_slice_all_data, summary
from utils.print import print_summary

ab_data_to_db = process_data_file()
#create_all_tables()
#write.insert_all_data(ab_data)
ab_data = read.read_ab_data()
vertical_slice_all_data = vertical_slice_all_data(ab_data)

print_summary(summary(ab_data, F_NUMERIC_FIELDS))
#plot(vertical_slice_all_data(ab_data), F_ALL_VARIABLES)

print_summary(summary(ab_data, [F_PRICE]))
plot(vertical_slice_all_data, [F_PRICE])