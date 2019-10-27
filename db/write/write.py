from db import connection


def insert_room_types(room_types: list):
    insert_to_table(room_types, 'INSERT INTO room_types VALUES (?,?)')


def insert_neighbourhood_groups(neighbourhood_groups: list):
    insert_to_table(neighbourhood_groups, 'INSERT INTO neighbourhood_groups VALUES (?,?)')


def insert_neighbourhoods(neighbourhoods: list):
    insert_to_table(neighbourhoods, 'INSERT INTO neighbourhoods VALUES (?,?)')


def insert_price_data(price_data: list):
    insert_to_table(price_data, 'INSERT INTO price_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)')


def insert_to_table(room_types, insert_command):
    con = connection.connect()
    cur = con.cursor();
    cur.executemany(insert_command, room_types)
    con.commit()
    connection.close(con)
