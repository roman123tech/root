import numpy as np
import csv

def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = 0
    denominator = 0
    for i in range(n):
        numerator += (x[i] - x_mean) * (y[i] - y_mean)
        denominator += (x[i] - x_mean) ** 2
    w1 = numerator / denominator
    w0 = y_mean - w1 * x_mean
    
    return w0, w1

def linear_regression_from_csv(csv_file):
    x = []
    y = []
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
    
    return linear_regression(x, y)

csv_file = 'reg.csv'
w0, w1 = linear_regression_from_csv(csv_file)
print(f"Intercept (w0): {w0}")
print(f"Slope (w1): {w1}")
