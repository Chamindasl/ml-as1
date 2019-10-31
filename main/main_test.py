from const import *
from file.file_read import process_data_file
from utils.data import vertical_slice_data
from utils.data import vertical_slice_all_data
from utils.data import sort_data
from utils.data import group_by
from utils.data import summary
from db.read import read
from analytics.multi_scatter import plot

import matplotlib.pyplot as plt

# library & dataset

# use the function regplot to make a scatterplot

# sns.plt.show()

# Without regression fit:

# sns.plt.show()

data_file = process_data_file()
price_data = read.read_price_data()

plot(vertical_slice_all_data(price_data), F_ALL_VARIABLES)

print(F_NUMBER_OF_REVIEWS)

sorted_by_reviews = sort_data(price_data,  F_PRICE[1])



#plot(vertical_slice_all_data(sorted_by_reviews))
#
# num_of_reviews = vertical_slice_data(sorted_by_reviews, F_NUMBER_OF_REVIEWS[1])
# room_type_ids = vertical_slice_data(sorted_by_reviews, F_ROOM_TYPE_ID[1])
# price = vertical_slice_data(sorted_by_reviews, F_PRICE[1])
# print("hi")
# a= [t for t in price_data if t[7]>1100 and t[7]<1200]
# print("ok")
# #print(a)
# print(max(price))
# sorted_by_reviews = sort_data(a,  F_PRICE[1])
# #price = vertical_slice_data(sorted_by_reviews, F_PRICE[1])
# #plt.hist(price, density=True, bins=50)
#
# print(summary(a, [F_PRICE, F_NUMBER_OF_REVIEWS]))
# print(summary(a, [F_PRICE, F_NUMBER_OF_REVIEWS]))
# print(sorted_by_reviews)
#
# print(group_by(sorted_by_reviews, F_NEIGHBOURHOOD_GROUP_ID[1]))
#
# #print(summary(a, [F_PRICE, F_NUMBER_OF_REVIEWS]))
# plt.scatter(room_type_ids, price, alpha=0.1)
# #plt.scatter( num_of_reviews, price, alpha=0.1)
# # plt.ylim(1, 10)
# # plt.xlim(1, 10)
# plt.show()
#
# print(price)
# # create_all_tables()
# # write.insert_room_types(data_file["room_types"])
# # write.insert_neighbourhood_groups(data_file["neighbourhood_groups"])
# # write.insert_neighbourhoods(data_file["neighbourhoods"])
# # write.insert_price_data(data_file["price_data"])
#
