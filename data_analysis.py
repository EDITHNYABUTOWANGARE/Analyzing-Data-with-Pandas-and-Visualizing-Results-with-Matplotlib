# data_analysis.py

import pandas as pd

def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    df = pd.read_csv(url, names=column_names)
    return df

def basic_statistics(df):
    return df.describe()

def group_by_species(df):
    return df.groupby('species').mean()

def check_missing_values(df):
    return df.isnull().sum()

if __name__ == "__main__":
    df = load_data()
    print("Dataset Overview:")
    print(df.head())
    print("\nBasic Statistics:")
    print(basic_statistics(df))
    print("\nGrouped by Species:")
    print(group_by_species(df))
    print("\nMissing Values:")
    print(check_missing_values(df))
