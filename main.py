import logging
from os import path

from analytics.ab.price_graph import visualize_price
from analytics.common.multi_graph import dist_plot
from analytics.common.multi_graph import scatter_plot
from const import F_PRICE, F_NUMERIC_FIELDS, F_ALL_FIELDS, F_AVAILABILITY_365
from db import DATA_AB_NYC_DB
from db.init.init import create_all_tables
from db.read import read
from db.write import write
from file.file_read import process_data_file
from utils.data import vertical_slice_all_data, summary, filter_by_index
from utils.print import print_summary, print_file_read_summary

logger = logging.getLogger(__name__)


def set_logger():
    logging.getLogger(__name__).setLevel(logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger('').addHandler(console)


set_logger()


def create_tables_and_insert_data(data_to_db):
    if not path.exists(DATA_AB_NYC_DB):
        logger.info("Creating database tables")
        create_all_tables()
        logger.info("Inserting data")
        write.insert_all_data(data_to_db)
    else:
        logger.warning("Database file is already exist, data will not be inserted again")


"""
Data ingesting and processing
"""
logger.info("Reading data file")
ab_data_to_db = process_data_file()  # read file
logger.info("Summary of file read")
print_file_read_summary(len(ab_data_to_db["ab_data"]), len(ab_data_to_db["ab_skipped"]))  # print summary of read
create_tables_and_insert_data(ab_data_to_db)  # create db tables and insert data
ab_data = read.read_ab_data()  # read data from db
vertical_slice_all_data_list = vertical_slice_all_data(ab_data)  # vertical slice all data, separate column data

"""
Data Summary
"""
logger.info("Printing summary for all fields")
print_summary(summary(ab_data, F_NUMERIC_FIELDS))  # print the summary of each data field

# logger.info("Generating pair scatter plots. After Graph appeared please close to proceed")  # this could take minutes
# scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS, title="Pair Scatter Plot for All Variables")
# logger.info("Generating pair scatter plots. After Graph appeared please close to proceed")  # this could take minutes
# scatter_plot(vertical_slice_all_data_list, F_ALL_FIELDS, True, title="Pair Scatter Plot for All Variables")

"""
Analysing Price Data
"""
logger.info("Printing Price Summary")
price_summary_all_data = summary(ab_data, [F_PRICE])
print_summary(price_summary_all_data)
logger.info("Generating Price Distribution for All Data. After Graph appeared please close to proceed")
scatter_plot(vertical_slice_all_data_list, [F_PRICE], title="Price Distribution - All Data")

"""
Price > $1000 is very extreme case.
Analysing Price Data. Price <= $1000
"""
ab_data_p_lte_1000 = filter_by_index(ab_data, F_PRICE[1], '<=', 1000)  # filter data by price less than or eq 1000
# vertical slice data data, separate column data
vertical_slice_ab_data_p_lte_1000 = vertical_slice_all_data(ab_data_p_lte_1000)
price_summary_lte_1000 = summary(ab_data_p_lte_1000, [F_PRICE])
logger.info("Printing Price Summary for listing where Price is less than $1000")
print_summary(price_summary_lte_1000)
logger.info("Generating Price Distribution for price <= $1000. After Graph appeared please close to proceed")
scatter_plot(vertical_slice_ab_data_p_lte_1000, [F_PRICE], title="Price Distribution - Price less than $1000")

"""
Price > $500 is also extreme case.
Analysing Price Data. Price <= $500
"""
# filter data by price less than or eq $500
ab_data_p_lte_500 = filter_by_index(ab_data_p_lte_1000, F_PRICE[1], '<=', 500)
vertical_slice_ab_data_p_lte_500 = vertical_slice_all_data(ab_data_p_lte_500)
logger.info("Printing Price Summary for listing where Price is less than 500")
price_summary_lte_500 = summary(ab_data_p_lte_500, [F_PRICE])
print_summary(price_summary_lte_500)
logger.info("Generating Price Distribution for price <= $500. After Graph appeared please close to proceed")
scatter_plot(vertical_slice_ab_data_p_lte_500, [F_PRICE], title="Price Distribution - Price less than $500")

"""
Comparing Price distribution for 3 data sets, all, <= 1000, <= 500
"""
dist_plot(
    [
        vertical_slice_all_data_list,
        vertical_slice_ab_data_p_lte_1000,
        vertical_slice_ab_data_p_lte_500,
    ],
    ["All Data", "Price <= 1000", "Price <= 500"],
    [
        price_summary_all_data[0][1]["mean"],
        price_summary_lte_1000[0][1]["mean"],
        price_summary_lte_500[0][1]["mean"],
    ],
    F_PRICE, title="Price Distribution Comparision - All, < 1000, < 500"
)

# scatter_plot(vertical_slice_ab_data_p_lte_500, F_ALL_FIELDS, True)

"""
Visualizing Price Data where price <= 500
"""
visualize_price(ab_data_p_lte_500, logger, title="Price < 500")

"""
Analysing Price Price > 1000
"""
ab_data_p_gte_1000 = filter_by_index(ab_data, F_PRICE[1], '>', 1000)
vertical_slice_ab_data_p_gt_1000 = vertical_slice_all_data(ab_data_p_gte_1000)
price_summary_gte_1000 = summary(ab_data_p_gte_1000, [F_PRICE])
print_summary(price_summary_gte_1000)
scatter_plot(vertical_slice_ab_data_p_gt_1000, [F_PRICE], title="Price Distribution - Price greater than $1000")

"""
Analysing Price Price > 1000
"""
ab_data_p_gte_5000 = filter_by_index(ab_data_p_gte_1000, F_PRICE[1], '>=', 5000)
vertical_slice_ab_data_p_gt_5000 = vertical_slice_all_data(ab_data_p_gte_5000)
price_summary_gte_5000 = summary(ab_data_p_gte_5000, [F_PRICE])
print_summary(price_summary_gte_5000)
scatter_plot(vertical_slice_ab_data_p_gt_5000, [F_PRICE], title="Price Distribution - Price greater than $5000")

"""
Comparing Price distribution for 4 data sets, all, <= 500
"""
dist_plot(
    [
        vertical_slice_all_data_list,
        vertical_slice_ab_data_p_lte_500,
        vertical_slice_ab_data_p_gt_1000,
        vertical_slice_ab_data_p_gt_5000,
    ],
    ["All Data", "Price < 500", "Price > 1000", "Price > 5000"],
    [
        price_summary_all_data[0][1]["mean"],
        price_summary_lte_500[0][1]["mean"],
        price_summary_gte_1000[0][1]["mean"],
        price_summary_gte_5000[0][1]["mean"],
    ],
    F_PRICE, title="Price Distribution Comparision - All, < 500, > 1000, > 5000"
)

# scatter_plot(vertical_slice_ab_data_p_gt_1000, F_ALL_FIELDS, True)

"""
Analysing Price Price > 1000, Price > 5000 
"""
visualize_price(ab_data_p_gte_1000, logger, title="Price > 1000")
visualize_price(ab_data_p_gte_5000, logger, title="Price > 5000")

"""
Analysing Price data, Availability = 0, Availability > 0
"""
ab_data_p_gte_1000 = filter_by_index(ab_data, F_AVAILABILITY_365[1], '=', 0)
visualize_price(ab_data_p_gte_1000, logger, title="Availability = 0")

ab_data_p_gte_1000 = filter_by_index(ab_data, F_AVAILABILITY_365[1], '>', 0)
visualize_price(ab_data_p_gte_1000, logger, title="Availability > 0")
