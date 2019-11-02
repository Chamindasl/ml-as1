from const import *
from utils.data import sort_data
from utils.data import group_by
from analytics.common.multi_graph import dist_plot
from analytics.common.multi_graph import scatter_plot
from const import F_PRICE, F_NUMERIC_FIELDS
from db.read import read
from file.file_read import process_data_file
from utils.data import vertical_slice_all_data, summary, filter_by_index
from utils.print import print_summary


# ab_data_to_db = process_data_file()
# create_all_tables()
# write.insert_all_data(ab_data_to_db)
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
#catter_plot(vertical_slice_ab_data_p_lt3_1000, [F_PRICE])

ab_data_p_lte_500 = filter_by_index(ab_data_p_lte_1000, F_PRICE, '<=', 500)
vertical_slice_ab_data_p_lt3_500 = vertical_slice_all_data(ab_data_p_lte_500)
print_summary(summary(ab_data_p_lte_500, [F_PRICE]))
#scatter_plot(vertical_slice_ab_data_p_lt3_500, [F_PRICE])

dist_plot(
    [
        vertical_slice_all_data_list,
        vertical_slice_ab_data_p_lt3_1000,
        vertical_slice_ab_data_p_lt3_500,
    ],
    ["All Data", "Price <= 1000", "Price <= 500", "Price <= 300"],
    F_PRICE)


a = (group_by(ab_data_p_lte_500, [F_ROOM_TYPE_ID[1], F_NEIGHBOURHOOD_GROUP_ID[1]]))
print(a)
#scatter_plot(vertical_slice_ab_data_p_lt3_500, F_ALL_FIELDS, True)

# library & dataset

# use the function regplot to make a scatterplot

# sns.plt.show()

# Without regression fit:

# sns.plt.show()

data_file = process_data_file()
price_data = read.read_ab_data()

#scatter_plot(vertical_slice_all_data(price_data), F_ALL_FIELDS)

print(F_NUMBER_OF_REVIEWS)

sorted_by_reviews = sort_data(price_data,  F_PRICE[1])


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
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
