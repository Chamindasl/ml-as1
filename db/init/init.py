from db import connection
from db import DATA_AB_NYC_DB


def create_room_types_table(db_file):
    """
    Create room types table

    +-----------+---------+----------------+-----+
    |  Column   |  Type   |  Description   | Key |
    +-----------+---------+----------------+-----+
    | id        | Integer | Id of the room | PK  |
    | room_type | text    | Room Type Text |     |
    +-----------+---------+----------------+-----+

    :param db_file: database file name
    :return: None
    """
    create_table('''CREATE TABLE IF NOT EXISTS room_types
                 (id integer NOT NULL PRIMARY KEY, room_type text)''', db_file)


def create_neighbourhood_groups_table(db_file):
    """
    Create neighbourhood groups table

    +----------------------+---------+--------------------------------+-----+
    |        Column        |  Type   |          Description           | Key |
    +----------------------+---------+--------------------------------+-----+
    | id                   | Integer | Id of the Neighbourhood group  | PK  |
    | neighbourhood_groups | text    | Neighbourhood Text             |     |
    +----------------------+---------+--------------------------------+-----+
    :param db_file: database file name
    :return: None
    """
    create_table('''CREATE TABLE IF NOT EXISTS neighbourhood_groups
                 (id integer NOT NULL PRIMARY KEY, neighbourhood_group text)''', db_file)


def create_neighbourhoods_table(db_file):
    """
    Create neighborhoods table

    +----------------+---------+-------------------------+-----+
    |     Column     |  Type   |       Description       | Key |
    +----------------+---------+-------------------------+-----+
    | id             | Integer | Id of the Neighborhoods |  PK |
    | neighborhoods  | text    | Neighborhoods  Text     |     |
    +----------------+---------+-------------------------+-----+

    :param db_file: database file name
    :return:
    """
    create_table('''CREATE TABLE IF NOT EXISTS neighbourhoods
                     (id integer NOT NULL PRIMARY KEY, neighbourhood text)''', db_file)


def create_ab_data_table(db_file):
    """
    Create main airbnb table as ab_data
    +--------------------------------+---------+--------------------------------+---------------------------+
    |             Column             |  Type   |           Description          |            Key            |
    +--------------------------------+---------+--------------------------------+---------------------------+
    | name                           | text    | Name of the room               |                           |
    | host_id                        | integer | Host Id                        |                           |
    | room_type_id                   | integer | Room type Id                   | FK to room_type           |
    | neighbourhood_group_id         | integer | Neighbourhood Group id         | FK to neighbourhood_group |
    | neighbourhood_id               | integer | Neighbourhood id               | FK to neighbourhood       |
    | latitude                       | real    | Latitude of the room           |                           |
    | longitude                      | real    | Longitude of the room          |                           |
    | price                          | real    | Price                          |                           |
    | minimum_nights                 | integer | Minimum Nights                 |                           |
    | number_of_reviews              | integer | Number of Reviews              |                           |
    | last_review                    | text    | Last Review                    |                           |
    | reviews_per_month              | integer | Reviews per Month              |                           |
    | calculated_host_listings_count | integer | Calculated Host Listings Count |                           |
    | availability_365               | integer | Availability                   |                           |
    +--------------------------------+---------+--------------------------------+---------------------------+


    :param db_file:
    :return:
    """
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
    """
    Utility method to create db tables
    :param create_table_command: command to create table
    :param db_file: database file
    :return: None
    """
    conn = connection.connect(db_file)
    cur = conn.cursor()
    cur.execute(create_table_command)
    conn.commit()
    connection.close(conn)


def create_all_tables(db_file=DATA_AB_NYC_DB):
    """
    Creates all 4 tables, room_types, neighbourhood_groups, neighbourhoods and ab_data
    :param db_file: database file
    :return: None
    """
    create_room_types_table(db_file)
    create_neighbourhood_groups_table(db_file)
    create_neighbourhoods_table(db_file)
    create_ab_data_table(db_file)
