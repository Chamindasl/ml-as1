from db import connection
from db import DATA_AB_NYC_DB


def create_room_types_table(db_file):
    create_table('''CREATE TABLE IF NOT EXISTS room_types
                 (id integer NOT NULL PRIMARY KEY, room_type text)''', db_file)


def create_neighbourhood_groups_table(db_file):
    create_table('''CREATE TABLE IF NOT EXISTS neighbourhood_groups
                 (id integer NOT NULL PRIMARY KEY, neighbourhood_group text)''', db_file)


def create_neighbourhoods_table(db_file):
    create_table('''CREATE TABLE IF NOT EXISTS neighbourhoods
                     (id integer NOT NULL PRIMARY KEY, neighbourhood text)''', db_file)


def create_ab_data_table(db_file):
    create_table('''CREATE TABLE IF NOT EXISTS ab_data
                     (
                     name text,
                     host_id INTEGER NOT NULL,
                     room_type_id INTEGER NOT NULL,
                     neighbourhood_group_id INTEGER NOT NULL,
                     neighbourhood_id INTEGER NOT NULL,
                     latitude real,
                     longitude real,
                     price real, 
                     minimum_nights INTEGER, 
                     number_of_reviews INTEGER, 
                     last_review text, 
                     reviews_per_month INTEGER,
                     calculated_host_listings_count INTEGER, 
                     availability_365 INTEGER,
                     FOREIGN KEY (room_type_id) REFERENCES room_types (id)
                      ON DELETE CASCADE ON UPDATE NO ACTION,
                     FOREIGN KEY (neighbourhood_group_id) REFERENCES neighbourhood_groups (id)
                      ON DELETE CASCADE ON UPDATE NO ACTION,
                     FOREIGN KEY (neighbourhood_id) REFERENCES neighbourhoods (id)
                      ON DELETE CASCADE ON UPDATE NO ACTION
                     )''', db_file)


def create_table(create_table_command, db_file):
    conn = connection.connect(db_file)
    cur = conn.cursor()
    cur.execute(create_table_command)
    conn.commit()
    connection.close(conn)


def create_all_tables(db_file=DATA_AB_NYC_DB):
    create_room_types_table(db_file)
    create_neighbourhood_groups_table(db_file)
    create_neighbourhoods_table(db_file)
    create_ab_data_table(db_file)
