# tests/test_eda.py
import unittest
import pandas as pd
from src.eda import EDA

class TestEDA(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'num_col1': [1, 2, 3, 4, 5],
            'num_col2': [5, 4, 3, 2, 1],
            'cat_col1': ['A', 'B', 'A', 'B', 'A'],
            'cat_col2': ['X', 'Y', 'X', 'Y', 'X'],
            'TransactionStartTime': pd.date_range(start='1/1/2022', periods=5)
        }
        df = pd.DataFrame(data)
        self.eda = EDA(df)

    def test_overview(self):
        overview = self.eda.overview()
        self.assertEqual(overview['shape'], (5, 5))
        self.assertTrue('num_col1' in overview['columns'])
        self.assertEqual(overview['data_types']['num_col1'], 'int64')

    def test_summary_statistics(self):
        summary = self.eda.summary_statistics()
        self.assertEqual(summary.loc['mean', 'num_col1'], 3.0)
        self.assertEqual(summary.loc['mean', 'num_col2'], 3.0)

    def test_check_missing_values(self):
        missing_values = self.eda.check_missing_values()
        self.assertEqual(missing_values.sum(), 0)

    def test_plot_distribution(self):
        # This test will check if the method runs without errors
        try:
            self.eda.plot_distribution('num_col1')
            self.eda.plot_distribution('num_col2')
        except Exception as e:
            self.fail(f"plot_distribution() raised {e} unexpectedly!")

    def test_plot_correlation_matrix(self):
        # This test will check if the method runs without errors
        try:
            self.eda.plot_correlation_matrix()
        except Exception as e:
            self.fail(f"plot_correlation_matrix() raised {e} unexpectedly!")

    def test_plot_categorical_distribution(self):
        # This test will check if the method runs without errors
        try:
            self.eda.plot_categorical_distribution('cat_col1')
            self.eda.plot_categorical_distribution('cat_col2')
        except Exception as e:
            self.fail(f"plot_categorical_distribution() raised {e} unexpectedly!")

    def test_detect_outliers(self):
        # This test will check if the method runs without errors
        try:
            self.eda.detect_outliers('num_col1')
            self.eda.detect_outliers('num_col2')
        except Exception as e:
            self.fail(f"detect_outliers() raised {e} unexpectedly!")

    def test_visualize_distributions(self):
        # This test will check if the method runs without errors
        try:
            self.eda.visualize_distributions()
        except Exception as e:
            self.fail(f"visualize_distributions() raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()