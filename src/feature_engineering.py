# src/feature_engineering.py
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from src.logger import setup_logger

class FeatureEngineering:
    def __init__(self, data):
        self.data = data
        self.logger = setup_logger()

    def create_aggregate_features(self):
        self.logger.info("Creating aggregate features...")
        self.data['TotalTransactionAmount'] = self.data.groupby('CustomerId')['Amount'].transform('sum')
        self.data['AverageTransactionAmount'] = self.data.groupby('CustomerId')['Amount'].transform('mean')
        self.data['TransactionCount'] = self.data.groupby('CustomerId')['TransactionId'].transform('count')
        self.data['TransactionStdDev'] = self.data.groupby('CustomerId')['Amount'].transform('std')
        return self.data

    def extract_temporal_features(self):
        self.logger.info("Extracting temporal features...")
        self.data['TransactionStartTime'] = pd.to_datetime(self.data['TransactionStartTime'])
        self.data['TransactionHour'] = self.data['TransactionStartTime'].dt.hour
        self.data['TransactionDay'] = self.data['TransactionStartTime'].dt.day
        self.data['TransactionMonth'] = self.data['TransactionStartTime'].dt.month
        self.data['TransactionYear'] = self.data['TransactionStartTime'].dt.year
        return self.data

    def encode_categorical_variables(self):
        self.logger.info("Encoding categorical variables...")
        cat_cols = self.data.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if self.data[col].nunique() < 10:
                self.data = pd.get_dummies(self.data, columns=[col], drop_first=True)
            else:
                le = LabelEncoder()
                self.data[col] = le.fit_transform(self.data[col])
        return self.data

    def handle_missing_values(self):
        self.logger.info("Handling missing values...")
        self.data.fillna(self.data.mean(), inplace=True)
        return self.data

    def normalize_features(self):
        self.logger.info("Normalizing features...")
        scaler = StandardScaler()
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
        return self.data