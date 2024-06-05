# src/feature_engineering.py
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder, MinMaxScaler
from src.logger import setup_logger

class FeatureEngineering:
    def __init__(self, df):
        self.df = df
        self.logger = setup_logger()

    def create_aggregate_features(self):
        self.logger.info("Creating aggregate features...")
        self.df['TotalTransactionAmount'] = self.df.groupby('CustomerId')['Amount'].transform('sum')
        self.df['AverageTransactionAmount'] = self.df.groupby('CustomerId')['Amount'].transform('mean')
        self.df['TransactionCount'] = self.df.groupby('CustomerId')['TransactionId'].transform('count')
        self.df['TransactionStdDev'] = self.df.groupby('CustomerId')['Amount'].transform('std')
        return self.df

    def extract_temporal_features(self):
        self.logger.info("Extracting temporal features...")
        self.df['TransactionStartTime'] = pd.to_datetime(self.df['TransactionStartTime'])
        self.df['TransactionHour'] = self.df['TransactionStartTime'].dt.hour
        self.df['TransactionDay'] = self.df['TransactionStartTime'].dt.day
        self.df['TransactionMonth'] = self.df['TransactionStartTime'].dt.month
        self.df['TransactionYear'] = self.df['TransactionStartTime'].dt.year
        return self.df

    def encode_categorical_variables(self):
        self.logger.info("Encoding categorical variables...")
        cat_cols = self.df.select_dtypes(include=['object']).columns

        for col in cat_cols:
            if self.df[col].nunique() < 10:
                # One-Hot Encoding for columns with fewer unique categories
                ohe = OneHotEncoder(sparse_output=False, drop='first')
                ohe_df = pd.DataFrame(ohe.fit_transform(self.df[[col]]), columns=ohe.get_feature_names_out([col]))
                self.df = pd.concat([self.df, ohe_df], axis=1).drop(columns=[col])
            else:
                # Label Encoding for columns with many unique categories
                le = LabelEncoder()
                self.df[col] = le.fit_transform(self.df[col])
        return self.df

    def handle_missing_values(self):
        self.logger.info("Handling missing values...")
        # Impute missing values with mean for numerical features
        num_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        for col in num_cols:
            self.df[col].fillna(self.df[col].mean(), inplace=True)

        # Drop rows with missing categorical values
        cat_cols = self.df.select_dtypes(include=['object']).columns
        self.df.dropna(subset=cat_cols, inplace=True)
        return self.df

    def normalize_features(self):
        self.logger.info("Normalizing features...")
        scaler = MinMaxScaler()
        num_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        self.df[num_cols] = scaler.fit_transform(self.df[num_cols])
        return self.df

    def standardize_features(self):
        self.logger.info("Standardizing features...")
        scaler = StandardScaler()
        num_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        self.df[num_cols] = scaler.fit_transform(self.df[num_cols])
        return self.df
