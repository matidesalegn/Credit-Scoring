import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.logger import setup_logger


class EDA:
    def __init__(self, df):
        self.df = df
        self.logger = setup_logger()


    def overview(self):
        overview = {
            "shape": self.df.shape,
            "columns": self.df.columns,
            "data_types": self.df.dtypes
        }
        return overview

    def summary_statistics(self):
        self.logger.info("Calculating summary statistics...")
        return self.df.describe()
    
    def data_types(self):
        self.logger.info("Checking data types...")
        return self.data.dtypes

    def plot_distribution(self, column):
        self.logger.info("Distribution Plot...")
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.show()
    
    # def plot_correlation_matrix(self):
    #     numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
    #     numeric_df = numeric_df.apply(pd.to_numeric, errors='coerce')  # Ensure all values are numeric
    #     plt.figure(figsize=(12, 8))
    #     sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    #     plt.title('Correlation Matrix')
    #     plt.show()

    def plot_correlation_matrix(self):
        self.logger.info("Calculating correlation matrix...")
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64'])
        correlation = numeric_cols.corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()

    def plot_categorical_distribution(self, column):
        self.logger.info("Categorical distribution...")
        plt.figure(figsize=(10, 6))
        sns.countplot(y=self.df[column])
        plt.title(f'Distribution of {column}')
        plt.show()
    
    def check_missing_values(self):
        self.logger.info("Checking missing values...")
        return self.df.isnull().sum()

    def detect_outliers(self, column):
        self.logger.info("Detect Outliers...")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.df[column])
        plt.title(f'Box Plot of {column}')
        plt.show()

    def visualize_distributions(self):
        self.logger.info("visualize distributions...")
        numeric_columns = self.df.select_dtypes(include=['float64', 'int64']).columns
        for column in numeric_columns:
            self.plot_distribution(column)
        
        categorical_columns = self.df.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            self.plot_categorical_distribution(column)

    def box_plots(self):
        self.logger.info("Creating box plots for outlier detection...")
        numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_cols:
            sns.boxplot(x=self.data[col])
            plt.title(f'Box plot of {col}')
            plt.show()
