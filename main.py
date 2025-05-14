# main.py

from data_analysis import load_data, basic_statistics, group_by_species, check_missing_values
from data_visualization import plot_line_chart, plot_bar_chart, plot_histogram, plot_scatter, plot_seaborn_boxplot

# Load data
df = load_data()

# Perform analysis
print("Dataset Overview:")
print(df.head())
print("\nBasic Statistics:")
print(basic_statistics(df))
print("\nGrouped by Species:")
print(group_by_species(df))
print("\nMissing Values:")
print(check_missing_values(df))

# Visualize data
plot_line_chart(df)
plot_bar_chart(df)
plot_histogram(df)
plot_scatter(df)
plot_seaborn_boxplot(df)
