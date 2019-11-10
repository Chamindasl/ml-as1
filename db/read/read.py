from db import connection, DATA_AB_NYC_DB


def read_ab_data(db_file=DATA_AB_NYC_DB):
    """
    Read all ab data by joining all tables as list of tuples 
    :param db_file: db file
    :return: result
    """""
    con = connection.connect(db_file)
    cur = con.cursor()
    cur.execute('SELECT '
                'p.name,'
                'p.host_id,'
                'r.room_type,'
                'ng.neighbourhood_group,'
                'n.neighbourhood,'
                'p.latitude,'
                'p.longitude,'
                'p.price,'
                'p.minimum_nights,'
                'p.number_of_reviews,'
                'p.last_review,'
                'p.reviews_per_month,'
                'p.calculated_host_listings_count,'
                'p.availability_365 '
                'FROM ab_data p '
                'INNER JOIN room_types r '
                'ON p.room_type_id = r.id '
                'INNER JOIN neighbourhood_groups ng '
                'ON p.neighbourhood_group_id = ng.id '
                'INNER JOIN neighbourhoods n '
                'ON p.neighbourhood_id = n.id ', )
    result = cur.fetchall()
    con.commit()
    connection.close(con)
    return result
