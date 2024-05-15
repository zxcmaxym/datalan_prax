import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

crime_data = pd.read_csv('SK010_data.csv')

years = np.array(crime_data['year']).reshape(-1, 1)
crime_counts = np.array(crime_data['crime_count'])

model = LinearRegression()

model.fit(years, crime_counts)

predicted_crime_2030 = model.predict([[2022]])

print("Predicted crime count for 2030:", int(predicted_crime_2030[0]))

