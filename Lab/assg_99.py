import csv
import numpy as np

land_price = []
house_price = []

file_path = 'itemset.csv'
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    
    next(csv_reader)

    for row in csv_reader:
        land_price.append(float(row[0]))
        house_price.append(float(row[1]))

correlation = np.corrcoef(land_price, house_price)[0, 1]

print(f"Correlation between Land Price and House Price: {correlation}")