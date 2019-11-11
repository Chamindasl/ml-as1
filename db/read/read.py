from db import connection, DATA_AB_NYC_DB


def read_neighbourhood_groups_data(db_file=DATA_AB_NYC_DB):
    """
    Read all neighbourhood_groups data as list of tuples 
    :param db_file: db file
    :return: result
    :raise sqlite3.OperationalError when db_file is not the correct db file
    """""
    sql = 'SELECT ' \
          'ng.id,' \
          'ng.neighbourhood_group ' \
          'FROM neighbourhood_groups ng '

    return read_all_data(db_file, sql)


def read_room_types_data(db_file=DATA_AB_NYC_DB):
    """
    Read all room_type data as list of tuples 
    :param db_file: db file
    :return: result
    :raise sqlite3.OperationalError when db_file is not the correct db file
    """""
    sql = 'SELECT ' \
          'r.id,' \
          'r.room_type ' \
          'FROM room_types r '

    return read_all_data(db_file, sql)


def read_neighbourhoods_data(db_file=DATA_AB_NYC_DB):
    """
    Read all neighbourhood data as list of tuples 
    :param db_file: db file
    :return: result
    :raise sqlite3.OperationalError when db_file is not the correct db file
    """""
    sql = 'SELECT ' \
          'n.id,' \
          'n.neighbourhood ' \
          'FROM neighbourhoods n '

    return read_all_data(db_file, sql)


def read_ab_data(db_file=DATA_AB_NYC_DB):
    """
    Read all ab data by joining all tables as list of tuples 
    :param db_file: db file
    :return: result
    :raise sqlite3.OperationalError when db_file is not the correct db file
    """""
    sql = 'SELECT ' \
          'p.name,' \
          'p.host_id,' \
          'r.room_type,' \
          'ng.neighbourhood_group,' \
          'n.neighbourhood,' \
          'p.latitude,' \
          'p.longitude,' \
          'p.price,' \
          'p.minimum_nights,' \
          'p.number_of_reviews,' \
          'p.last_review,' \
          'p.reviews_per_month,' \
          'p.calculated_host_listings_count,' \
          'p.availability_365 ' \
          'FROM ab_data p ' \
          'INNER JOIN room_types r ' \
          'ON p.room_type_id = r.id ' \
          'INNER JOIN neighbourhood_groups ng ' \
          'ON p.neighbourhood_group_id = ng.id ' \
          'INNER JOIN neighbourhoods n ' \
          'ON p.neighbourhood_id = n.id '
    return read_all_data(db_file, sql)


def read_all_data(db_file, sql):
    """
    Utility method to read Read data as list of tuples 
    :param db_file: db file
    :param sql sql command
    :return: result
    :raise sqlite3.OperationalError when db_file is not the correct db file
    """""
    con = connection.connect(db_file)
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    connection.close(con)
    return result
