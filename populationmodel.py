import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Function to predict population count for 2030 and save the result
def predict_and_save(file_path):
    # Read the dataset
    population_data = pd.read_csv(file_path)
    
    # Extract years and population counts
    years = np.array(population_data['year']).reshape(-1, 1)
    population_counts = np.array(population_data['value'])
    
    # Fit linear regression model
    model = LinearRegression()
    model.fit(years, population_counts)
    
    # Predict population counts for years 2022 to 2040
    future_years = np.arange(2024, 2041).reshape(-1, 1)
    predicted_population_counts = model.predict(future_years)
    
    # Append predicted population counts to the dataset
    future_predictions = pd.DataFrame({
        'year': future_years.flatten(),
        'value': predicted_population_counts
    })
    updated_population_data = pd.concat([population_data, future_predictions], ignore_index=True)
    
    # Extract filename
    file_name = os.path.basename(file_path)
    
    # Create result file path
    result_file_path = os.path.join('population', file_name)
    
    # Save updated dataset to file
    updated_population_data.to_csv(result_file_path, index=False)
    print(f"Updated dataset saved to {result_file_path}")

# Iterate over files in the 'population_in/' directory
for file_name in os.listdir('population_in'):
    if file_name.endswith('.csv'):
        file_path = os.path.join('population_in', file_name)
        predict_and_save(file_path)

