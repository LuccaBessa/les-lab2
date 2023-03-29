import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('./data/repos.csv')

# Convert the createdAt column to datetime format
df['createdAt'] = pd.to_datetime(df['createdAt'])

# Calculate the repo age in days
df['repoAge'] = (pd.Timestamp.now() - df['createdAt']).dt.days / 365.25

# Define the columns to use for the scatterplots
metric_columns = ['CBO', 'DIT', 'LCOM']
scatter_columns = ['repoAge', 'stargazerCount', 'releases', 'LOC'] + metric_columns

# Generate the scatterplot graphs
for i in range(len(scatter_columns) - 1):
    for j in range(i+1, len(scatter_columns)):
        plt.scatter(df[scatter_columns[i]], df[scatter_columns[j]])
        plt.xlabel(scatter_columns[i])
        plt.ylabel(scatter_columns[j])
        plt.title(f'{scatter_columns[i]} vs {scatter_columns[j]}')
        filename = f'{scatter_columns[i]}_vs_{scatter_columns[j]}.png'
        plt.savefig(filename)
        plt.clf()  # clear the plot for the next iteration
