import sqlite3
from unittest import TestCase

from coverage.files import os

from db.connection import connect
from db.init.init import create_all_tables
from db.read.read import read_ab_data, read_room_types_data, read_neighbourhoods_data, read_neighbourhood_groups_data
from db.write.write import insert_room_types, insert_neighbourhood_groups, insert_neighbourhoods, insert_ab_data
from definitions import ROOT_DIR
from exceptions.db_exceptions import InvalidData

relative_path = ""
# uncomment following line when running single test from ide
# relative_path = "../"

db_ = ROOT_DIR / relative_path / "data/tmp/tmp.ab.nyc.db"


def delete_db():
    try:
        os.remove(db_)
    except FileNotFoundError:
        pass


class TestInitWriteRead(TestCase):

    def setUp(self):
        # removing temp db file
        delete_db()
        connect(db_)
        create_all_tables(db_)

    def test_init(self):
        # initial read should fail as tables not exist
        delete_db()
        connect(db_)
        self.assertRaises(sqlite3.OperationalError, read_room_types_data, db_)
        self.assertRaises(sqlite3.OperationalError, read_neighbourhood_groups_data, db_)
        self.assertRaises(sqlite3.OperationalError, read_neighbourhoods_data, db_)
        self.assertRaises(sqlite3.OperationalError, read_ab_data, db_)
        # creating tables
        create_all_tables(db_)
        # after creating tables, read should return 0 items
        self.assertEqual(0, len(read_room_types_data(db_)))
        self.assertEqual(0, len(read_neighbourhood_groups_data(db_)))
        self.assertEqual(0, len(read_neighbourhoods_data(db_)))
        self.assertEqual(0, len(read_ab_data(db_)))

    def test_write_read_room_types(self):
        # before insert
        data = read_room_types_data(db_)
        self.assertEqual(0, len(data))

        # insert 1 room type
        insert_room_types([(1, "rt 1")], db_)
        data = read_room_types_data(db_)
        self.assertEqual(1, len(data))
        self.assertEqual(1, data[0][0])
        self.assertEqual("rt 1", data[0][1])

        # insert multiple room types
        insert_room_types([(2, "rt 2"), (3, "rt 3")], db_)
        data = read_room_types_data(db_)
        self.assertEqual(3, len(data))

        # duplicate id test
        self.assertRaises(InvalidData, insert_room_types, [(1, "rt 1")], db_)

        # invalid data
        self.assertRaises(InvalidData, insert_room_types, [(1,)], db_)
        self.assertRaises(InvalidData, insert_room_types, [(1, "rt 1", "abc")], db_)
        self.assertRaises(InvalidData, insert_room_types, [[1, "rt 1", "abc"]], db_)

    def test_write_read_neighbourhood_groups(self):
        # before insert
        data = read_neighbourhood_groups_data(db_)
        self.assertEqual(0, len(data))

        # insert 1 room type
        insert_neighbourhood_groups([(1, "ng 1")], db_)
        data = read_neighbourhood_groups_data(db_)
        self.assertEqual(1, len(data))
        self.assertEqual(1, data[0][0])
        self.assertEqual("ng 1", data[0][1])

        # insert multiple room types
        insert_neighbourhood_groups([(2, "ng 2"), (3, "ng 3")], db_)
        data = read_neighbourhood_groups_data(db_)
        self.assertEqual(3, len(data))

        # duplicate id test
        self.assertRaises(InvalidData, insert_neighbourhood_groups, [(1, "ng 1")], db_)

    def test_write_read_neighbourhoods(self):
        # before insert
        data = read_neighbourhoods_data(db_)
        self.assertEqual(0, len(data))

        # insert 1 room type
        insert_neighbourhoods([(1, "n 1")], db_)
        data = read_neighbourhoods_data(db_)
        self.assertEqual(1, len(data))
        self.assertEqual(1, data[0][0])
        self.assertEqual("n 1", data[0][1])

        # insert multiple room types
        insert_neighbourhoods([(2, "n 2"), (3, "n 3")], db_)
        data = read_neighbourhoods_data(db_)
        self.assertEqual(3, len(data))

        # duplicate id test
        self.assertRaises(InvalidData, insert_neighbourhoods, [(1, "n 1")], db_)

    def test_write_read_ab_data(self):
        # before insert
        data = read_ab_data(db_)
        self.assertEqual(0, len(data))
        insert_room_types([(1, "Private room")], db_)
        insert_neighbourhood_groups([(1, "Brooklyn")], db_)
        insert_neighbourhoods([(1, "Kensington")], db_)
        # insert 1 room type
        data_1 = ('Clean & quiet apt home by the park',
                  2787,
                  1,  # id of Private room
                  1,  # id of Brooklyn
                  1,  # id of Kensington
                  40.64749,
                  -73.97237,
                  149,
                  1,
                  9,
                  '2018-10-19',
                  0.21,
                  6,
                  365)
        insert_ab_data([data_1], db_)
        data = read_ab_data(db_)
        self.assertEqual(1, len(data))
        self.assertEqual("Clean & quiet apt home by the park", data[0][0])
        self.assertEqual("Private room", data[0][2])
        self.assertEqual("Brooklyn", data[0][3])
        self.assertEqual("Kensington", data[0][4])

        # insert multiple room types
        insert_ab_data([data_1, data_1], db_)
        data = read_ab_data(db_)
        self.assertEqual(3, len(data))

    def tearDown(self):
        # removing temp db file
        delete_db()
