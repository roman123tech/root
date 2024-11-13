import csv
import numpy as np

def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = [list(map(float, row)) for row in reader]
    return np.array(data)

def calculate_distance_matrix(data):
    num_points = len(data)
    distance_matrix = [[0.0] * num_points for _ in range(num_points)]
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = np.linalg.norm(data[i] - data[j])
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    return distance_matrix

def update_distance_matrix(distance_matrix, cluster1, cluster2):
    new_distances = [
        min(distance_matrix[cluster1][k], distance_matrix[cluster2][k]) for k in range(len(distance_matrix))
    ]
    for k in range(len(distance_matrix)):
        distance_matrix[cluster1][k] = new_distances[k]
        distance_matrix[k][cluster1] = new_distances[k]
    
    distance_matrix.pop(cluster2)
    for row in distance_matrix:
        row.pop(cluster2)

def print_distance_matrix(matrix, labels):
    print("\n" + "   ".join([" "] + labels))
    for i, row in enumerate(matrix):
        print(f"{labels[i]} " + " ".join(f"{dist:6.2f}" for dist in row))

def agglomerative_clustering_single_linkage(data, labels):
    distance_matrix = calculate_distance_matrix(data)
    print("Initial Distance Matrix:")
    print_distance_matrix(distance_matrix, labels)
    
    clusters = labels.copy()
    while len(clusters) > 1:
        print("\nCurrent Distance Matrix:")
        print_distance_matrix(distance_matrix, clusters)
        
        min_distance = float('inf')
        i, j = -1, -1
        for x in range(len(distance_matrix)):
            for y in range(x + 1, len(distance_matrix)):
                if distance_matrix[x][y] < min_distance:
                    min_distance = distance_matrix[x][y]
                    i, j = x, y
        if i == -1 or j == -1:
            print("Error: No valid clusters found.")
            return
        print(f"Merging clusters: {clusters[i]} and {clusters[j]}")
        update_distance_matrix(distance_matrix, i, j)
        
        clusters[i] = f"{clusters[i]}{clusters[j]}"
        clusters.pop(j)
if __name__ == "__main__":
    filename = 'hier.csv'  
    data = load_data(filename)
    if data is None or len(data) == 0:
        print("Error: Data could not be loaded or is empty.")
    else:
        labels = ['A', 'B', 'C', 'D'] 
        agglomerative_clustering_single_linkage(data, labels)
