def mean(values):
    return sum(values) / len(values)

def correlation_coefficient(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    denominator_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    denominator = (denominator_x * denominator_y) ** 0.5
    
    return numerator / denominator

with open('marks.csv', 'r') as file:
    lines = file.readlines()
    ise = []
    ese = []
    for line in lines[1:]:
        values = line.strip().split(',')
        ise.append(float(values[0]))
        ese.append(float(values[1]))

correlation = correlation_coefficient(ise, ese)
print("Correlation Coefficient between ISE and ESE:", correlation)
