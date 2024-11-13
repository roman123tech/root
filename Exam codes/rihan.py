import csv

# Function to calculate the Pearson correlation coefficient
def calculate_correlation(age, income):
    n = len(age)
    mean_x = sum(age) / n
    mean_y = sum(income) / n
    numerator = sum((age[i] - mean_x) * (income[i] - mean_y) for i in range(n))
    denominator = (sum((age[i] - mean_x) ** 2 for i in range(n)) * sum((income[i] - mean_y) ** 2 for i in range(n))) ** 0.5
    return numerator / denominator

# Function to calculate linear regression parameters (slope and intercept)
def calculate_linear_regression(age, income):
    n = len(age)
    sum_x = sum(age)
    sum_y = sum(income)
    sum_xy = sum(age[i] * income[i] for i in range(n))
    sum_x_squared = sum(age[i] ** 2 for i in range(n))
    
    # Slope (m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    
    # Intercept (b)
    b = (sum_y - m * sum_x) / n
    
    return m, b

# Function to read data from CSV
def read_data_from_csv(file_path):
    age = []
    income = []
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            age.append(float(row[0]))  # Assuming age is in the first column
            income.append(float(row[1]))  # Assuming income is in the second column
    
    return age, income

# Main program
file_path = 'your_file.csv'  # Change to your CSV file path
age, income = read_data_from_csv(file_path)

# Calculate Pearson correlation coefficient
correlation = calculate_correlation(age, income)

# Calculate linear regression
slope, intercept = calculate_linear_regression(age, income)

# Output the results
print(f"Correlation Coefficient: {correlation:.4f}")
print(f"Linear Regression Equation: y = {slope:.2f}x + {intercept:.2f}")

# Save results to a CSV file
output_data = [
    ["Correlation Coefficient", correlation],
    ["Slope", slope],
    ["Intercept", intercept],
    ["Linear Regression Equation", f"y = {slope:.2f}x + {intercept:.2f}"]
]

output_file = 'output_results.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(output_data)

print(f"Results saved to {output_file}")
