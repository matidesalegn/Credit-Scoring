# src/data_loader.py
import pandas as pd
from src.logger import setup_logger

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = setup_logger()

    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            self.logger.info(f"Data loaded successfully from {self.file_path}")
            return data
        except Exception as e:
            self.logger.error(f"Error loading data: {e}")
            raise

    def check_data_types(self, data):
        self.logger.info("Checking data types...")
        return data.dtypes

    def check_missing_values(self, data):
        self.logger.info("Checking missing values...")
        return data.isnull().sum()