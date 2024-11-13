import csv
import math

def entropy(class_labels):
    label_count = {}
    for label in class_labels:
        if label in label_count:
            label_count[label] += 1
        else:
            label_count[label] = 1
    
    total_instances = len(class_labels)
    entropy_value = 0
    for count in label_count.values():
        probability = count / total_instances
        entropy_value -= probability * math.log2(probability)
    
    return entropy_value

def information_gain(data, target_attribute_index, attribute_index, total_entropy):
    attribute_values = [row[attribute_index] for row in data]
    
    attribute_value_counts = {}
    for value in attribute_values:
        if value in attribute_value_counts:
            attribute_value_counts[value] += 1
        else:
            attribute_value_counts[value] = 1
    
    weighted_entropy = 0
    for value, count in attribute_value_counts.items():
        subset = [row for row in data if row[attribute_index] == value]
        subset_labels = [row[target_attribute_index] for row in subset]
        subset_entropy = entropy(subset_labels)
        weighted_entropy += (count / len(data)) * subset_entropy
    
    gain = total_entropy - weighted_entropy
    return gain

def subset_information_gain(data, target_attribute_index, attribute_index):
    unique_values = set([row[attribute_index] for row in data])
    
    gains = {}
    for value in unique_values:
        subset_data = [row for row in data if row[attribute_index] == value]
        subset_entropy = entropy([row[target_attribute_index] for row in subset_data])
        
        gains[value] = subset_entropy
    
    return gains

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  
        data = [row for row in reader]  
    return header, data

if __name__ == "__main__":
    file_path = 'table1.csv'

    header, data = read_csv(file_path)
    
    target_column = 'Class'
    attributes = ['Outlook', 'Temperature', 'Humidity', 'Windy']

    if target_column not in header:
        print(f"Error: '{target_column}' not found in the CSV header.")
    else:
        target_index = header.index(target_column)

        target_labels = [row[target_index] for row in data]
        total_entropy = entropy(target_labels)  # Calculate total entropy once
        print(f"Total Entropy for target attribute '{target_column}': {total_entropy:.4f}")

        for attribute in attributes:
            if attribute not in header:
                print(f"Error: Attribute '{attribute}' not found in the CSV header.")
            else:
                attribute_index = header.index(attribute)
                gain = information_gain(data, target_index, attribute_index, total_entropy)
                print(f"\nInformation Gain for {attribute}: {gain:.4f}")

                subset_gains = subset_information_gain(data, target_index, attribute_index)
                for value, subset_gain in subset_gains.items():
                    print(f"Entropy for {attribute} = {value}: {subset_gain:.4f}")
