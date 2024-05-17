import pandas as pd
import os

# Define directories
population_dir = 'population'
datasets_dir = 'datasets'
output_dir = 'output'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# List of regions
regions = [
    'Banskobystrický_kraj', 'Bratislavský_kraj', 'Košický_kraj',
    'Nitriansky_kraj', 'Prešovský_kraj', 'Trenčiansky_kraj',
    'Trnavský_kraj', 'Žilinský_kraj'
]

# Process each region
for region in regions:
    # Construct file paths
    population_file = os.path.join(population_dir, f'{region}_statistics.csv')
    datasets_file = os.path.join(datasets_dir, f'{region}.csv')
    output_file = os.path.join(output_dir, f'{region}_crime_per_citizen.csv')

    # Read population and crime data
    population_df = pd.read_csv(population_file, sep=',')
    datasets_df = pd.read_csv(datasets_file, sep=',')

    # Merge dataframes on the year column
    merged_df = pd.merge(population_df, datasets_df, on='year')

    # Calculate crime per citizen
    merged_df['crime_per_citizen'] = merged_df['crime_count'] / merged_df['value']

    # Select only the necessary columns
    result_df = merged_df[['year', 'crime_per_citizen']]

    # Save the result to a new CSV file
    result_df.to_csv(output_file, sep=';', index=False)

    print(f'Created {output_file}')

