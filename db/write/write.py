from db import connection, DATA_AB_NYC_DB
from os import path
import logging

logger = logging.getLogger(__name__)


def insert_all_data(all_data: dict, db_file=DATA_AB_NYC_DB):
    """
    Insert data into given db file if db file is not exist
    :param all_data: all data as dictionary
    :param db_file: db file
    :return: return True if insertion successful
    """
    if not path.exists(db_file):
        insert_room_types(all_data["room_types"], db_file)
        insert_neighbourhood_groups(all_data["neighbourhood_groups"], db_file)
        insert_neighbourhoods(all_data["neighbourhoods"], db_file)
        insert_ab_data(all_data["ab_data"], db_file)
        return True
    else:
        logger.warning("Database file is already exist, data will not be inserted again")
        return False


def insert_room_types(room_types: list, db_file):
    """
    Insert room type data
    :param room_types: room types as list of tuples
    :param db_file: database file
    :return:
    """
    insert_to_table(room_types, 'INSERT INTO room_types VALUES (?,?)', db_file)


def insert_neighbourhood_groups(neighbourhood_groups: list, db_file):
    """
    Insert neighbourhood groups type data
    :param neighbourhood_groups: neighbourhood groups as list of tuples
    :param db_file: database file
    :return:
    """
    insert_to_table(neighbourhood_groups, 'INSERT INTO neighbourhood_groups VALUES (?,?)', db_file)


def insert_neighbourhoods(neighbourhoods: list, db_file):
    """
    Insert neighbourhood  type data
    :param neighbourhoods: neighbourhood as list of tuples
    :param db_file: database file
    :return:
    """
    insert_to_table(neighbourhoods, 'INSERT INTO neighbourhoods VALUES (?,?)', db_file)


def insert_ab_data(ab_data: list, db_file):
    """
    Insert main airbnb data
    :param ab_data: airbnb data as list of tuples
    :param db_file: database file
    :return:
    """
    insert_to_table(ab_data, 'INSERT INTO ab_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', db_file)


def insert_to_table(data_list, insert_command, db_file):
    """
    Insert data into a given table
    :param data_list: data as list of tuples
    :param insert_command: insert command
    :param db_file: database file
    :return:
    """
    con = connection.connect(db_file)
    cur = con.cursor()
    cur.executemany(insert_command, data_list)
    con.commit()
    connection.close(con)
