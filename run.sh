#!/bin/bash

#Run populationparser.py
python3 populationparser.py

# Run parse.py
python3 parse.py

# Run model.py
python3 model.py

# Run convertcsv.py
python3 convertcsv.py

# Run final conversion to crime per citizen
python3 final_gen.py

# remove aditional file in population/
rm population/_statistics.csv

# Finito
echo "Done"
