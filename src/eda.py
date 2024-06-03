import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class EDA:
    def __init__(self, df):
        self.df = df

    def overview(self):
        overview = {
            "shape": self.df.shape,
            "columns": self.df.columns,
            "data_types": self.df.dtypes
        }
        return overview

    def summary_statistics(self):
        return self.df.describe()

    def plot_distribution(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.show()
    
    def plot_correlation_matrix(self):
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])
        plt.figure(figsize=(12, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()

    def plot_categorical_distribution(self, column):
        plt.figure(figsize=(10, 6))
        sns.countplot(y=self.df[column])
        plt.title(f'Distribution of {column}')
        plt.show()
    
    def check_missing_values(self):
        return self.df.isnull().sum()

    def detect_outliers(self, column):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.df[column])
        plt.title(f'Box Plot of {column}')
        plt.show()
