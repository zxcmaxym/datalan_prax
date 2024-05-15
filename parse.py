import csv
from collections import defaultdict

# Function to read CSV file and organize data into a dictionary of lists
def read_csv(file_path):
    data_dict = defaultdict(list)

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        headers = next(csv_reader)  # Read the header row
        region_index = headers.index('region_id')
        year_index = headers.index('year')
        crime_count_index = headers.index('crime_count')

        for row in csv_reader:
            region_id = row[region_index]
            year = int(row[year_index])
            crime_count = int(row[crime_count_index])
            data_dict[region_id].append({'year': year, 'crime_count': crime_count})

    return data_dict

# Function to write data to separate CSV files for each region
def write_csv(data_dict):
    for region_id, values in data_dict.items():
        file_name = f"{region_id}_data.csv"
        with open(file_name, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['year', 'crime_count'])
            for entry in values:
                csv_writer.writerow([entry['year'], entry['crime_count']])

# Example usage
file_path = './crime_data.csv'  # Replace with your CSV file path
data = read_csv(file_path)
write_csv(data)

