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
    return weighted_gini  # return weighted Gini index instead of reduction

def load_csv_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
    return header, data

csv_file_path = 'table1.csv'  # Change this to the path of your CSV file
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

        results.append({
            'Attribute': header[attribute_index],
            'Information Gain': ig,
            'Gini Index': gini_value,  # Store the Gini index instead of reduction
            'Unique Values': list(set(row[attribute_index] for row in data))
        })
        
        if ig > best_gain:
            best_gain = ig
            best_gain_attribute = header[attribute_index]
        
        if gini_value < best_gini:  # Check for minimum Gini index
            best_gini = gini_value
            best_gini_attribute = header[attribute_index]

for result in results:
    print(f"Attribute: {result['Attribute']}, Information Gain: {result['Information Gain']}, Gini Index: {result['Gini Index']}, Unique Values: {result['Unique Values']}")

print(f"\nBest attribute for classification based on Information Gain: {best_gain_attribute} with gain of {best_gain}")
print(f"Best attribute for classification based on Gini Index: {best_gini_attribute} with Gini index of {best_gini}")
