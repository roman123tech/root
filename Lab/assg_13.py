import csv
from collections import defaultdict

def load_data(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data.append(row)
    return data, headers

def separate_features_labels(dataset):
    features = []
    labels = []
    for row in dataset:
        features.append(row[:-1])
        labels.append(row[-1])
    return features, labels

def encode_features(features):
    encoded_features = []
    feature_encoders = []
    
    for col in range(len(features[0])):
        col_values = [row[col] for row in features]
        if all(isinstance(x, str) for x in col_values):
            unique_values = set(col_values)
            encoder = {value: idx for idx, value in enumerate(unique_values)}
            feature_encoders.append(encoder)
            encoded_col = [encoder[value] for value in col_values]
            encoded_features.append(encoded_col)
        else:
            encoded_features.append([float(value) for value in col_values])
            feature_encoders.append(None)

    return list(map(list, zip(*encoded_features))), feature_encoders

def calculate_prior(labels):
    total_count = len(labels)
    label_count = {}
    for label in labels:
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    prior = {label: count / total_count for label, count in label_count.items()}
    return prior
def calculate_conditional_probabilities(features, labels):
    conditional_probabilities = defaultdict(lambda: defaultdict(list))
    label_count = {}
    for i in range(len(features)):
        label = labels[i]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
        for j in range(len(features[i])):
            conditional_probabilities[label][j].append(float(features[i][j]))
    for label in conditional_probabilities:
        for j in conditional_probabilities[label]:
            mean = sum(conditional_probabilities[label][j]) / label_count[label]
            variance = sum((x - mean) ** 2 for x in conditional_probabilities[label][j]) / label_count[label]
            conditional_probabilities[label][j] = (mean, variance)
    return conditional_probabilities
def calculate_class_probability(sample, prior, conditional_probabilities):
    total_prob = {}
    for label in prior:
        prob = prior[label]
        for j in range(len(sample)):
            mean, variance = conditional_probabilities[label][j]
            if variance == 0:
                continue
            prob *= (1 / ((2 * 3.14159 * variance) ** 0.5)) * \
                     (2.71828 ** (-((sample[j] - mean) ** 2) / (2 * variance)))
        total_prob[label] = prob
    return total_prob
def predict(sample, prior, conditional_probabilities):
    probabilities = calculate_class_probability(sample, prior, conditional_probabilities)
    return max(probabilities, key=probabilities.get)
def main():
    filename = 'table1.csv'
    dataset, headers = load_data(filename)
    features, labels = separate_features_labels(dataset)
    encoded_features, feature_encoders = encode_features(features)
    prior = calculate_prior(labels)
    conditional_probabilities = calculate_conditional_probabilities(encoded_features, labels)
    input_data = []
    for i, header in enumerate(headers[:-1]):
        options = ', '.join([str(opt) for opt in feature_encoders[i].keys()]) if feature_encoders[i] else "any number"
        value = input(f"Enter value for '{header}' [{options}]: ")
        input_data.append(value)
    
    encoded_sample = [feature_encoders[i].get(value, value) if feature_encoders[i] else float(value) 
                      for i, value in enumerate(input_data)]

    predicted_class = predict(encoded_sample, prior, conditional_probabilities)
    print("Sample features:", input_data)
    print("Predicted class:", predicted_class)
    probabilities = calculate_class_probability(encoded_sample, prior, conditional_probabilities)
    print("Class probabilities:")
    for label, probability in probabilities.items():
        print(f"Class {label}: {probability}")

if __name__ == "__main__":
    main()
