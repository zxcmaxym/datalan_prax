import os
import csv

def parse_data(filename):
    regions = {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip header
        
        for row in reader:
            region = row[0]
            if region not in regions:
                regions[region] = []
            data = row[2:]  # Extract yearly statistics
            regions[region].extend(data)
    
    return regions

def save_data(regions, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for region, data in regions.items():
        with open(os.path.join(directory, f"{region.strip()}_statistics.csv"), 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["year", "value"])  # Write the header
            for year, value in zip(range(2001, 2024), data):
                writer.writerow([year, value])

if __name__ == "__main__":
    filename = "Population.csv"
    output_directory = "population"
    regions_data = parse_data(filename)
    save_data(regions_data, output_directory)

