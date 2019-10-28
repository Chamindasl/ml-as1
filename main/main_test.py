from file.file_read import process_data_file
from db.init.init import create_all_tables
from db.write import write
from utils.data import slice_data
from const import *
data_file = process_data_file()
price_data = data_file["price_data"]
print(F_NUMBER_OF_REVIEWS)


num_of_reviews = slice_data(price_data, F_NUMBER_OF_REVIEWS[1])
#price = slice_data(price_data, F_PRICE[1])
print(num_of_reviews)
# create_all_tables()
# write.insert_room_types(data_file["room_types"])
# write.insert_neighbourhood_groups(data_file["neighbourhood_groups"])
# write.insert_neighbourhoods(data_file["neighbourhoods"])
# write.insert_price_data(data_file["price_data"])

