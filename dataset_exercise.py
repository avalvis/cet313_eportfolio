import pandas as pd

# Load the dataset
file_path = 'players.csv'  # Replace with your file path
players_df = pd.read_csv(file_path)

# Shape of the dataset
print("Shape of the dataset:", players_df.shape)

# First 30 rows of the dataset
print("\nFirst 30 rows of the dataset:")
print(players_df.head(30))

# Description of the dataset
print("\nDescription of the dataset:")
print(players_df.describe())

import matplotlib.pyplot as plt

# Selecting key variables for histograms
variables_for_histogram = ['now_cost', 'points_per_game', 'goals_scored']

# Creating histograms
fig, axes = plt.subplots(nrows=1, ncols=len(variables_for_histogram), figsize=(15, 5))
fig.suptitle('Histograms of Selected Variables')

for i, var in enumerate(variables_for_histogram):
    axes[i].hist(players_df[var].dropna(), bins=20, color='skyblue', edgecolor='black')
    axes[i].set_title(var.replace('_', ' ').capitalize())
    axes[i].set_xlabel(var)
    axes[i].set_ylabel('Frequency')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()