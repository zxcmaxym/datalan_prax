#!/bin/bash

#Run populationparser.py
python3 populationparser.py
rm population_in/_statistics.csv

#idek anymore man
python3 populationmodel.py

rm population_in/_statistics.csv
# Run parse.py
python3 parse.py

rm population_in/_statistics.csv
# Run model.py
python3 model.py

rm population_in/_statistics.csv
# Run convertcsv.py

rm population_in/_statistics.csv
# Run final conversion to crime per citizen
python3 final_gen.py
python3 convertcsv.py
rm population_in/_statistics.csv
# Run the server
python3 server.py
