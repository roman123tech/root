def read_csv(filename):
    with open(filename, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]
    return data[1:]
data = read_csv('bin.csv')
data_values = [float(row[1]) for row in data]
num_bins = int(input("Enter the number of bins: "))
bin_size, remainder = divmod(len(data_values), num_bins)
bins = []
start = 0
for i in range(num_bins):
    extra = 1 if i < remainder else 0
    bins.append(data_values[start:start + bin_size + extra])
    start += bin_size + extra

print("Sorted data for Age:", sorted(data_values))

print("\nPartition into bins:")
for i, bin in enumerate(bins):
    print(f"Bin {i + 1}: {', '.join(map(str, bin))}")

smooth_by_mean = []
for bin in bins:
    mean_val = round(sum(bin) / len(bin)) if bin else 0
    smooth_by_mean.extend([mean_val] * len(bin))

print("\nSmoothing by bin means:")
for i in range(len(bins)):
    print(f"Bin {i + 1}: {', '.join([str(smooth_by_mean[j]) for j in range(sum(len(b) for b in bins[:i]), sum(len(b) for b in bins[:i+1]))])}")

smooth_by_median = []
for bin in bins:
    sorted_bin = sorted(bin)
    median_val = sorted_bin[len(sorted_bin) // 2] if sorted_bin else 0
    smooth_by_median.extend([median_val] * len(bin))
print("\nSmoothing by bin medians:")
for i in range(len(bins)):
    print(f"Bin {i + 1}: {', '.join([str(smooth_by_median[j]) for j in range(sum(len(b) for b in bins[:i]), sum(len(b) for b in bins[:i+1]))])}")
smooth_by_boundary = []
for bin in bins:
    if bin:
        min_val, max_val = min(bin), max(bin)
        smooth_bin = [min_val if abs(val - min_val) < abs(val - max_val) else max_val for val in bin]
        smooth_by_boundary.extend(smooth_bin)
print("\nSmoothing by bin boundaries:")
for i in range(len(bins)):
    print(f"Bin {i + 1}: {', '.join([str(smooth_by_boundary[j]) for j in range(sum(len(b) for b in bins[:i]), sum(len(b) for b in bins[:i+1]))])}")