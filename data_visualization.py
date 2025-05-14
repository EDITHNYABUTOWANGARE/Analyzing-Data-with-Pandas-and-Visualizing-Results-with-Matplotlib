# data_visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
from data_analysis import load_data

def plot_line_chart(df):
    plt.plot(df['sepal_length'])
    plt.title('Trend of Sepal Length')
    plt.xlabel('Index')
    plt.ylabel('Sepal Length')
    plt.show()

def plot_bar_chart(df):
    df.groupby('species')['petal_length'].mean().plot(kind='bar')
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length')
    plt.show()

def plot_histogram(df):
    df['sepal_length'].plot(kind='hist', bins=20, edgecolor='black')
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Frequency')
    plt.show()

def plot_scatter(df):
    plt.scatter(df['sepal_length'], df['petal_length'])
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Length')
    plt.show()

def plot_seaborn_boxplot(df):
    sns.set(style="whitegrid")
    sns.boxplot(x='species', y='petal_length', data=df)
    plt.title('Petal Length Distribution by Species')
    plt.show()

if __name__ == "__main__":
    df = load_data()
    plot_line_chart(df)
    plot_bar_chart(df)
    plot_histogram(df)
    plot_scatter(df)
    plot_seaborn_boxplot(df)
