# tests/test_data_loader.py
import unittest
from src.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.loader = DataLoader('data/raw/data.csv')

    def test_load_data(self):
        data = self.loader.load_data()
        self.assertIsNotNone(data)

    def test_check_data_types(self):
        data = self.loader.load_data()
        dtypes = self.loader.check_data_types(data)
        self.assertIsNotNone(dtypes)

    def test_check_missing_values(self):
        data = self.loader.load_data()
        missing_values = self.loader.check_missing_values(data)
        self.assertIsNotNone(missing_values)

if __name__ == '__main__':
    unittest.main()