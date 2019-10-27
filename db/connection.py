import sqlite3
from db import DATA_AB_NYC_DB


def connect():
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(DATA_AB_NYC_DB)
    return conn


def close(conn):
    """ Commit changes and close connection to the database """
    conn.close()
