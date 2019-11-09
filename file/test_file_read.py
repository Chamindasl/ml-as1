from unittest import TestCase

from exceptions.file_exceptions import FileNotReadableError
from file.file_read import process_data_file

HEADERS = [['id',
            'name',
            'host_id',
            'host_name',
            'neighbourhood_group',
            'neighbourhood',
            'latitude',
            'longitude',
            'room_type',
            'price',
            'minimum_nights',
            'number_of_reviews',
            'last_review',
            'reviews_per_month',
            'calculated_host_listings_count',
            'availability_365']]


class TestData(TestCase):

    def test_process_data_file_10_lines(self):
        data = process_data_file("../data/tmp/AB_NYC_10_lines.csv")
        self.assertEqual([(1, 'Private room'), (2, 'Entire home/apt')], data["room_types"])
        self.assertEqual([(1, 'Brooklyn'), (2, 'Manhattan')], data["neighbourhood_groups"])
        self.assertEqual(10, len(data["neighbourhoods"]))
        self.assertEqual(HEADERS, data["ab_headers"])
        self.assertEqual(10, len(data["ab_data"]))
        self.assertEqual(0, len(data["ab_skipped"]))

    def test_process_data_file_10_lines_2_skip(self):
        data = process_data_file("../data/tmp/AB_NYC_10_lines_2_skip.csv")
        self.assertEqual([(1, 'Private room'), (2, 'Entire home/apt')], data["room_types"])
        self.assertEqual([(1, 'Brooklyn'), (2, 'Manhattan')], data["neighbourhood_groups"])
        self.assertEqual(8, len(data["neighbourhoods"]))
        self.assertEqual(HEADERS, data["ab_headers"])
        self.assertEqual(8, len(data["ab_data"]))
        self.assertEqual(('Clean & quiet apt home by the park',
                          '2787',
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
                          365), data["ab_data"][0])
        self.assertEqual(2, len(data["ab_skipped"]))
        self.assertEqual("5203", data["ab_skipped"][0][0])
        self.assertEqual("5238", data["ab_skipped"][1][0])
        self.assertEqual(15, len(data["ab_skipped"][0]))
        self.assertEqual(17, len(data["ab_skipped"][1]))

    def test_process_data_file_file_not_exist(self):
        self.assertRaises(FileNotReadableError, process_data_file, "../data/tmp/A.csv")
        self.assertRaises(FileNotReadableError, process_data_file, "../data/tmp/AB_NYC_invalid_data.csv")

    def test_process_data_file_main_fle(self):
        data = process_data_file()
        self.assertEqual([(1, 'Private room'), (2, 'Entire home/apt'), (3, 'Shared room')], data["room_types"])
        self.assertEqual([(1, 'Brooklyn'),
                          (2, 'Manhattan'),
                          (3, 'Queens'),
                          (4, 'Staten Island'),
                          (5, 'Bronx')], data["neighbourhood_groups"])
        self.assertEqual(218, len(data["neighbourhoods"]))
        self.assertEqual(HEADERS, data["ab_headers"])
        self.assertEqual(41707, len(data["ab_data"]))
        self.assertEqual(7373, len(data["ab_skipped"]))
