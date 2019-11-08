from db import connection


def create_room_types_table():
    create_table('''CREATE TABLE IF NOT EXISTS room_types
                 (id integer NOT NULL PRIMARY KEY, room_type text)''')


def create_neighbourhood_groups_table():
    create_table('''CREATE TABLE IF NOT EXISTS neighbourhood_groups
                 (id integer NOT NULL PRIMARY KEY, neighbourhood_group text)''')


def create_neighbourhoods_table():
    create_table('''CREATE TABLE IF NOT EXISTS neighbourhoods
                     (id integer NOT NULL PRIMARY KEY, neighbourhood text)''')


def create_ab_data_table():
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
                     )''')


def create_table(create_table_command):
    conn = connection.connect()
    cur = conn.cursor()
    cur.execute(create_table_command)
    conn.commit()
    connection.close(conn)


def create_all_tables():
    create_room_types_table()
    create_neighbourhood_groups_table()
    create_neighbourhoods_table()
    create_ab_data_table()
