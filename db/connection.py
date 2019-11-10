import sqlite3


def connect(db_file):
    """ Make connection to an SQLite database file
    :param db_file database file
    """
    conn = sqlite3.connect(db_file)
    return conn


def close(conn):
    """ Commit changes and close connection to the database
    :param conn connection to close
    """
    conn.close()
