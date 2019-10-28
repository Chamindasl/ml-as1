from const import *
from file.file_read import process_data_file
from utils.data import slice_data
from utils.data import sort_data
import matplotlib.pyplot as plt

data_file = process_data_file()
price_data = data_file["price_data"]
print(F_NUMBER_OF_REVIEWS)

sorted_by_reviews = sort_data(price_data,  F_PRICE[1])

num_of_reviews = slice_data(sorted_by_reviews, F_NUMBER_OF_REVIEWS[1])
room_type_ids = slice_data(sorted_by_reviews, F_ROOM_TYPE_ID[1])
price = slice_data(sorted_by_reviews, F_PRICE[1])

print(max(price))
plt.hist(price, density=True, bins=50)
#plt.scatter(room_type_ids, price, alpha=0.1)
#plt.scatter( num_of_reviews, price, alpha=0.1)
#plt.ylim(1, 10)
#plt.xlim(1, 10)
plt.show()

print(num_of_reviews)
print(price)
# create_all_tables()
# write.insert_room_types(data_file["room_types"])
# write.insert_neighbourhood_groups(data_file["neighbourhood_groups"])
# write.insert_neighbourhoods(data_file["neighbourhoods"])
# write.insert_price_data(data_file["price_data"])

