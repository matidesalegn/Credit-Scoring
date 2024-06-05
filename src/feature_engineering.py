# # src/feature_engineering.py
# import pandas as pd
# from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
# from src.logger import setup_logger

# class FeatureEngineering:
#     def __init__(self, data):
#         self.data = data
#         self.logger = setup_logger()

#     def create_aggregate_features(self):
#         self.logger.info("Creating aggregate features...")
#         self.data['TotalTransactionAmount'] = self.data.groupby('CustomerId')['Amount'].transform('sum')
#         self.data['AverageTransactionAmount'] = self.data.groupby('CustomerId')['Amount'].transform('mean')
#         self.data['TransactionCount'] = self.data.groupby('CustomerId')['TransactionId'].transform('count')
#         self.data['TransactionStdDev'] = self.data.groupby('CustomerId')['Amount'].transform('std')
#         return self.data

#     def extract_temporal_features(self):
#         self.logger.info("Extracting temporal features...")
#         self.data['TransactionStartTime'] = pd.to_datetime(self.data['TransactionStartTime'])
#         self.data['TransactionHour'] = self.data['TransactionStartTime'].dt.hour
#         self.data['TransactionDay'] = self.data['TransactionStartTime'].dt.day
#         self.data['TransactionMonth'] = self.data['TransactionStartTime'].dt.month
#         self.data['TransactionYear'] = self.data['TransactionStartTime'].dt.year
#         return self.data

#     def encode_categorical_variables(self):
#         self.logger.info("Encoding categorical variables...")
#         cat_cols = self.data.select_dtypes(include=['object']).columns
#         for col in cat_cols:
#             if self.data[col].nunique() < 10:
#                 self.data = pd.get_dummies(self.data, columns=[col], drop_first=True)
#             else:
#                 le = LabelEncoder()
#                 self.data[col] = le.fit_transform(self.data[col])
#         return self.data

#     def handle_missing_values(self):
#         self.logger.info("Handling missing values...")
#         self.data.fillna(self.data.mean(), inplace=True)
#         return self.data

#     def normalize_features(self):
#         self.logger.info("Normalizing features...")
#         scaler = StandardScaler()
#         numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
#         self.data[numeric_cols] = scaler.fit_transform(self.data[numeric_cols])
#         return self.data

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

class FeatureEngineering:
    def __init__(self, df):
        self.df = df

    def create_aggregate_features(self):
        self.df['Total_Transaction_Amount'] = self.df.groupby('CustomerId')['Amount'].transform('sum')
        self.df['Average_Transaction_Amount'] = self.df.groupby('CustomerId')['Amount'].transform('mean')
        self.df['Transaction_Count'] = self.df.groupby('CustomerId')['TransactionId'].transform('count')
        self.df['Std_Transaction_Amount'] = self.df.groupby('CustomerId')['Amount'].transform('std')

    def extract_temporal_features(self):
        self.df['TransactionStartTime'] = pd.to_datetime(self.df['TransactionStartTime'])
        self.df['Transaction_Hour'] = self.df['TransactionStartTime'].dt.hour
        self.df['Transaction_Day'] = self.df['TransactionStartTime'].dt.day
        self.df['Transaction_Month'] = self.df['TransactionStartTime'].dt.month
        self.df['Transaction_Year'] = self.df['TransactionStartTime'].dt.year

    def encode_categorical_variables(self):
        # One-Hot Encoding for nominal categorical variables
        nominal_features = self.df.select_dtypes(include=['object']).columns
        self.df = pd.get_dummies(self.df, columns=nominal_features, drop_first=True)
        
        # Label Encoding for ordinal categorical variables if any (example shown)
        # ordinal_features = ['ExampleOrdinalFeature']
        # for feature in ordinal_features:
        #     le = LabelEncoder()
        #     self.df[feature] = le.fit_transform(self.df[feature])

    def handle_missing_values(self, strategy='mean'):
        for column in self.df.columns:
            if self.df[column].isnull().sum() > 0:
                if self.df[column].dtype == 'object':
                    self.df[column].fillna(self.df[column].mode()[0], inplace=True)
                elif self.df[column].dtype in ['int64', 'float64']:
                    if strategy == 'mean':
                        self.df[column].fillna(self.df[column].mean(), inplace=True)
                    elif strategy == 'median':
                        self.df[column].fillna(self.df[column].median(), inplace=True)
                    elif strategy == 'mode':
                        self.df[column].fillna(self.df[column].mode()[0], inplace=True)
    
    def normalize_standardize_features(self, method='standardize'):
        numeric_columns = self.df.select_dtypes(include=['float64', 'int64']).columns
        if method == 'normalize':
            self.df[numeric_columns] = self.df[numeric_columns].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
        elif method == 'standardize':
            scaler = StandardScaler()
            self.df[numeric_columns] = scaler.fit_transform(self.df[numeric_columns])