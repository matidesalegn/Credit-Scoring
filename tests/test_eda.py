import unittest
import pandas as pd
from src.eda import EDA

class TestEDA(unittest.TestCase):
    def setUp(self):
        data = {
            'CustomerId': [1, 2, 1, 2],
            'Amount': [100, 200, 300, 400],
            'TransactionStartTime': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04']
        }
        self.df = pd.DataFrame(data)
        self.eda = EDA(self.df)
    
    def test_overview(self):
        overview = self.eda.overview()
        self.assertIsInstance(overview, dict)
        self.assertIn("shape", overview)
        self.assertIn("columns", overview)
        self.assertIn("data_types", overview)

    def test_summary_statistics(self):
        summary_stats = self.eda.summary_statistics()
        self.assertIsInstance(summary_stats, pd.DataFrame)

    def test_check_missing_values(self):
        missing_values = self.eda.check_missing_values()
        self.assertIsInstance(missing_values, pd.Series)

if __name__ == '__main__':
    unittest.main()