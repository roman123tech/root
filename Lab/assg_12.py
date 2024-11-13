import numpy as np
import csv

def entropy(class_labels):
    value_counts = {}
    for label in class_labels:
        value_counts[label] = value_counts.get(label, 0) + 1
    
    total_count = len(class_labels)
    return -sum((count / total_count) * np.log2(count / total_count + 1e-10) for count in value_counts.values())

def information_gain(data, split_attribute_index, target_attribute_index):
    original_entropy = entropy([row[target_attribute_index] for row in data])
    values = {}
    for row in data:
        value = row[split_attribute_index]
        if value not in values:
            values[value] = []
        values[value].append(row[target_attribute_index])
    
    weighted_entropy = sum((len(value_data) / len(data)) * entropy(value_data) for value_data in values.values())
    return original_entropy - weighted_entropy

def gini_index(class_labels):
    value_counts = {}
    for label in class_labels:
        value_counts[label] = value_counts.get(label, 0) + 1
    
    total_count = len(class_labels)
    return 1 - sum((count / total_count) ** 2 for count in value_counts.values())

def gini_index_split(data, split_attribute_index, target_attribute_index):
    original_gini = gini_index([row[target_attribute_index] for row in data])
    values = {}
    for row in data:
        value = row[split_attribute_index]
        if value not in values:
            values[value] = []
        values[value].append(row[target_attribute_index])
    weighted_gini = sum((len(value_data) / len(data)) * gini_index(value_data) for value_data in values.values())
    return weighted_gini
def gini_for_unique_values(data, split_attribute_index, target_attribute_index):
    unique_values = set(row[split_attribute_index] for row in data)
    unique_ginis = {}
    for value in unique_values:
        value_data = [row[target_attribute_index] for row in data if row[split_attribute_index] == value]
        unique_ginis[value] = gini_index(value_data)
    return unique_ginis
def load_csv_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
    return header, data
csv_file_path = 'table1.csv'  
header, data = load_csv_data(csv_file_path)
target_attribute = header.index('Class')
results = []
best_gain = float('-inf')
best_gini = float('inf')
best_gain_attribute = None
best_gini_attribute = None
for attribute_index in range(len(header)):
    if attribute_index != target_attribute:
        ig = information_gain(data, attribute_index, target_attribute)
        gini_value = gini_index_split(data, attribute_index, target_attribute)
        unique_ginis = gini_for_unique_values(data, attribute_index, target_attribute)
        results.append({
            'Attribute': header[attribute_index],
            'Information Gain': ig,
            'Gini Index': gini_value,
            'Unique Values': list(set(row[attribute_index] for row in data)),
            'Unique Ginis': unique_ginis
        })
        if ig > best_gain:
            best_gain = ig
            best_gain_attribute = header[attribute_index]
        
        if gini_value < best_gini:
            best_gini = gini_value
            best_gini_attribute = header[attribute_index]

print(f"{'Attribute':<25} {'Information Gain':<20} {'Gini Index':<15} {'Unique Values':<30} {'Unique Ginis':<40}")
print("=" * 130)

for result in results:
    unique_values = ', '.join(result['Unique Values'])
    unique_ginis = ', '.join(f"{k}: {v:.4f}" for k, v in result['Unique Ginis'].items())
    print(f"{result['Attribute']:<25} {result['Information Gain']:<20.4f} {result['Gini Index']:<15.4f} {unique_values:<30} {unique_ginis:<40}")

print("=" * 130)
print(f"\nBest attribute for classification based on Information Gain: {best_gain_attribute} with gain of {best_gain:.4f}")
print(f"Best attribute for classification based on Gini Index: {best_gini_attribute} with Gini index of {best_gini:.4f}")
