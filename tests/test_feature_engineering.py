# tests/test_feature_engineering.py
import unittest
import pandas as pd
import numpy as np
from src.feature_engineering import FeatureEngineering

class TestFeatureEngineering(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'CustomerId': [1, 2, 1, 2, 3],
            'TransactionId': [101, 102, 103, 104, 105],
            'Amount': [50, 200, 150, 100, 250],
            'TransactionStartTime': pd.date_range(start='1/1/2022', periods=5, freq='D'),
            'Category': ['A', 'B', 'A', 'C', 'B']
        }
        self.df = pd.DataFrame(data)
        self.fe = FeatureEngineering(self.df)

    def test_create_aggregate_features(self):
        df = self.fe.create_aggregate_features()
        self.assertIn('TotalTransactionAmount', df.columns)
        self.assertIn('AverageTransactionAmount', df.columns)
        self.assertIn('TransactionCount', df.columns)
        self.assertIn('TransactionStdDev', df.columns)
        self.assertEqual(df.loc[df['CustomerId'] == 1, 'TotalTransactionAmount'].values[0], 200)

    def test_extract_temporal_features(self):
        df = self.fe.extract_temporal_features()
        self.assertIn('TransactionHour', df.columns)
        self.assertIn('TransactionDay', df.columns)
        self.assertIn('TransactionMonth', df.columns)
        self.assertIn('TransactionYear', df.columns)
        self.assertEqual(df['TransactionHour'].iloc[0], 0)  # assuming transactions occur at midnight

    def test_encode_categorical_variables(self):
        df = self.fe.encode_categorical_variables()
        self.assertNotIn('Category', df.columns)
        self.assertTrue(any('Category_' in col for col in df.columns))

    def test_handle_missing_values(self):
        df_with_missing = self.df.copy()
        df_with_missing.loc[0, 'Amount'] = np.nan
        fe_with_missing = FeatureEngineering(df_with_missing)
        df = fe_with_missing.handle_missing_values()
        self.assertFalse(df.isnull().any().any())

    def test_normalize_features(self):
        df = self.fe.normalize_features()
        self.assertTrue(np.allclose(df['Amount'].max(), 1))
        self.assertTrue(np.allclose(df['Amount'].min(), 0))

    def test_standardize_features(self):
        df = self.fe.standardize_features()
        self.assertTrue(np.allclose(df['Amount'].mean(), 0, atol=1e-6))
        self.assertTrue(np.allclose(df['Amount'].std(), 1, atol=1e-6))

if __name__ == '__main__':
    unittest.main()