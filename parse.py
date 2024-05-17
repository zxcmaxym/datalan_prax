import csv
from collections import defaultdict
import os

# Labels dictionary
labels = {
    "SK0": "Slovenská republika",
    "SK01": "Bratislavský kraj",
    "SK02": "Západné Slovensko",
    "SK021": "Trnavský kraj",
    "SK022": "Trenčiansky kraj",
    "SK023": "Nitriansky kraj",
    "SK03": "Stredné Slovensko",
    "SK031": "Žilinský kraj",
    "SK032": "Banskobystrický kraj",
    "SK04": "Východné Slovensko",
    "SK041": "Prešovský kraj",
    "SK042": "Košický kraj"
}
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
            # Reverse the order of data
            data_dict[region_id].insert(0, {'year': year, 'crime_count': crime_count})

    return data_dict

def write_csv(data_dict, folder_name):
    for region_id, values in data_dict.items():
        label = labels.get(region_id, region_id)
        file_name = f"{folder_name}/{label.replace(' ', '_').replace('/', '_')}.csv"
        os.makedirs(folder_name, exist_ok=True)
        with open(file_name, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['year', 'crime_count'])
            for entry in values:
                csv_writer.writerow([entry['year'], entry['crime_count']])

def main():
    file_path = './crime_data.csv'
    folder_name = 'datasets'
    data = read_csv(file_path)
    write_csv(data, folder_name)

if __name__ == "__main__":
    main()
