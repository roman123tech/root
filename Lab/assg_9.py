import numpy as np
import csv

def read_csv(file_name):
    entity1 = []
    entity2 = []
    
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            if not row[0].startswith('#'):
                entity1.append(float(row[0]))
                entity2.append(float(row[1]))
    
    return entity1, entity2

def calculate_correlation(entity1, entity2):
    correlation_matrix = np.corrcoef(entity1, entity2)
    correlation_coefficient = correlation_matrix[0, 1]
    
    if correlation_coefficient > 0:
        correlation_type = "Positive"
    elif correlation_coefficient < 0:
        correlation_type = "Negative"
    else:
        correlation_type = "No Correlation"
    
    return correlation_coefficient, correlation_type

csv_file = 'itemset.csv' 
entity1, entity2 = read_csv(csv_file)
correlation_coefficient, correlation_type = calculate_correlation(entity1, entity2)

print(f"Correlation Coefficient: {correlation_coefficient}")
print(f"Correlation Type: {correlation_type}")
