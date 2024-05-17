import pandas as pd
import os
import json

# Directory containing CSV files
csv_directory = "output/"

# Directory to store JSON files
json_directory = "json_output/"

os.makedirs(json_directory, exist_ok=True)

# Iterate through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        # Read the CSV file into a pandas DataFrame
        filepath = os.path.join(csv_directory, filename)
        df = pd.read_csv(filepath)

        # Convert DataFrame to JSON
        json_data = df.to_json(orient='records')

        # Write JSON data to a file
        json_filename = os.path.splitext(filename)[0] + ".json"
        json_filepath = os.path.join(json_directory, json_filename)
        with open(json_filepath, 'w') as json_file:
            json_file.write(json_data)

        print(f"Converted {filename} to {json_filename}")

print("Conversion completed!")

