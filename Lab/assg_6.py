import csv

def read_csv_data(file_name: str):
    data_list = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader, None)
        for row in reader:
            try:
                if row[0].strip():
                    score = float(row[0])
                    data_list.append(score)
            except ValueError:
                print(f"Warning: Skipping row with non-numeric data: {row}")
    return data_list, headers

def calculate_statistics(scores):
    data_sorted = sorted(scores)
    n = len(data_sorted)

    minimum = data_sorted[0]
    maximum = data_sorted[-1]

    median = (data_sorted[n // 2 - 1] + data_sorted[n // 2]) / 2 if n % 2 == 0 else data_sorted[n // 2]

    q1 = data_sorted[n // 4]
    q3 = data_sorted[(3 * n) // 4]

    iqr = q3 - q1

    return minimum, q1, median, q3, maximum, iqr

def process_csv(file_name: str):
    data_list, headers = read_csv_data(file_name)

    if not data_list:
        print("Error: No valid data found in the CSV file.")
        return {}

    minimum, q1, median, q3, maximum, iqr = calculate_statistics(data_list)
    
    results = {
        "Minimum": minimum,
        "Q1": q1,
        "Median": median,
        "Q3": q3,
        "Maximum": maximum,
        "IQR": iqr
    }

    return results

file_name = 'boxplot.csv'
statistics = process_csv(file_name)

print("\nStatistics for All Scores:")
for stat_name, value in statistics.items():
    print(f"{stat_name}: {value:.2f}")
