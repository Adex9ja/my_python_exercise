# import the Pandas library.
import pandas as pd
import matplotlib.pyplot as plt

# Read the downloaded csv file in the notebook using Pandas.
df = pd.read_csv('forestfires.csv')

# Show the first five row of the file, as shown in the figure below.
print(df.head())

# Check if the dataset has empty cells.
is_null = pd.isnull(df).sum()
print(is_null)

# Calculate the mean and median for all columns and notice the difference between the
# mean and medians. Calculate the variance and the standard deviation for all the columns
print(df.describe())

# Show a box plot for all FFMC, DMC, and DC columns.
df.boxplot(column=['FFMC', 'DMC', 'DC'])

# Show a correlation heatmap.
print(df.corr())