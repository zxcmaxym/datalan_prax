import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Function to predict crime count for 2030 and save the result
def predict_and_save(file_path):
    # Read the dataset
    crime_data = pd.read_csv(file_path)
    
    # Extract years and crime counts
    years = np.array(crime_data['year']).reshape(-1, 1)
    crime_counts = np.array(crime_data['crime_count'])
    
    # Fit linear regression model
    model = LinearRegression()
    model.fit(years, crime_counts)
    
    # Predict crime counts for years 2022 to 2040
    future_years = np.arange(2022, 2041).reshape(-1, 1)
    predicted_crime_counts = model.predict(future_years)
    
    # Append predicted crime counts to the dataset
    future_predictions = pd.DataFrame({
        'year': future_years.flatten(),
        'crime_count': predicted_crime_counts
    })
    updated_crime_data = pd.concat([crime_data, future_predictions], ignore_index=True)
    
    # Extract filename
    file_name = os.path.basename(file_path)
    
    # Create result file path
    result_file_path = os.path.join('results', file_name)
    
    # Save updated dataset to file
    updated_crime_data.to_csv(result_file_path, index=False)
    print(f"Updated dataset saved to {result_file_path}")

# Iterate over files in the 'datasets/' directory
for file_name in os.listdir('datasets'):
    if file_name.endswith('.csv'):
        file_path = os.path.join('datasets', file_name)
        predict_and_save(file_path)

