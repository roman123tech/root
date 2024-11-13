def minmax(data, new_min=0, new_max=1):
    min_val = min(data)
    max_val = max(data)
    minmax_normal = [((x - min_val) * (new_max - new_min) / (max_val - min_val)) + new_min for x in data]
    return minmax_normal
def zscore(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    zscore_normal = [(x - mean) / std_dev for x in data]
    return zscore_normal
def read_csv_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split(',') for line in lines[1:] if line.strip()]
    return data
def write_csv_data(file_path, normalized_data):
    with open(file_path, 'w') as file:
        for row in normalized_data:
            file.write(','.join(map(str, row)) + '\n')
def normalize_and_save(file_path, min_max_output, z_score_output):
    new_min = float(input("Enter the new minimum value for min-max normalization: "))
    new_max = float(input("Enter the new maximum value for min-max normalization: "))
    data = read_csv_data(file_path)
    trimmed_data = [row[:-1] for row in data if len(row) > 1] 
    if not trimmed_data:
        print("No valid data to normalize.")
        return
    try:
        numeric_data = [[float(value) for value in row] for row in trimmed_data]
    except ValueError as e:
        print(f"Error converting data to float: {e}")
        return
    num_columns = len(numeric_data[0]) if numeric_data else 0
    min_max_columns = [[] for _ in range(num_columns)]
    z_score_columns = [[] for _ in range(num_columns)]
    for col_index in range(num_columns):
        col_data = [row[col_index] for row in numeric_data if len(row) > col_index]
        min_max_columns[col_index] = minmax(col_data, new_min, new_max)
        z_score_columns[col_index] = zscore(col_data)
    min_max_normalized_data = [list(row) for row in zip(*min_max_columns)]
    z_score_normalized_data = [list(row) for row in zip(*z_score_columns)]
    write_csv_data(min_max_output, min_max_normalized_data)
    write_csv_data(z_score_output, z_score_normalized_data)
ipfile = "iris.csv"  
minmax_op = "min-maxop.csv"  
zscore_op = "z-score.csv"  
normalize_and_save(ipfile, minmax_op, zscore_op)
print(f"Min-max scaling saved to {minmax_op}")
print(f"Z-score normalization saved to {zscore_op}")
