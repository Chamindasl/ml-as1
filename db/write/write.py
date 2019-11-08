from db import connection, DATA_AB_NYC_DB
from os import path
import logging

logger = logging.getLogger(__name__)


def insert_all_data(all_data: dict):
    if not path.exists(DATA_AB_NYC_DB):
        insert_room_types(all_data["room_types"])
        insert_neighbourhood_groups(all_data["neighbourhood_groups"])
        insert_neighbourhoods(all_data["neighbourhoods"])
        insert_ab_data(all_data["ab_data"])
    else:
        logger.warning("Database file is already exist, data will not be inserted again")


def insert_room_types(room_types: list):
    insert_to_table(room_types, 'INSERT INTO room_types VALUES (?,?)')


def insert_neighbourhood_groups(neighbourhood_groups: list):
    insert_to_table(neighbourhood_groups, 'INSERT INTO neighbourhood_groups VALUES (?,?)')


def insert_neighbourhoods(neighbourhoods: list):
    insert_to_table(neighbourhoods, 'INSERT INTO neighbourhoods VALUES (?,?)')


def insert_ab_data(ab_data: list):
    insert_to_table(ab_data, 'INSERT INTO ab_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)')


def insert_to_table(room_types, insert_command):
    con = connection.connect()
    cur = con.cursor()
    cur.executemany(insert_command, room_types)
    con.commit()
    connection.close(con)
