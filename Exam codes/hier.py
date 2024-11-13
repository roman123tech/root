import csv
import numpy as np

def load_lower_triangular_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix_row = [float(x) for x in row]
            while len(matrix_row) < len(matrix) + 1:
                matrix_row.append(0.0)
            matrix.append(matrix_row)
    
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i].append(matrix[j][i])

    return np.array(matrix)

def update_distance_matrix(distance_matrix, cluster1, cluster2):
    new_distances = [
        min(distance_matrix[cluster1][k], distance_matrix[cluster2][k]) for k in range(len(distance_matrix))
    ]
    for k in range(len(distance_matrix)):
        distance_matrix[cluster1][k] = new_distances[k]
        distance_matrix[k][cluster1] = new_distances[k]
    
    distance_matrix = np.delete(distance_matrix, cluster2, axis=0)
    distance_matrix = np.delete(distance_matrix, cluster2, axis=1)
    return distance_matrix

def print_lower_triangular_matrix(matrix, labels):
    print("\n   " + "   ".join(labels))
    for i in range(len(matrix)):
        row = [" " if j > i else f"{matrix[i][j]:6.2f}" for j in range(len(matrix))]
        print(f"{labels[i]} " + " ".join(row))

def agglomerative_clustering_single_linkage(distance_matrix, labels):
    print("Initial Distance Matrix:")
    print_lower_triangular_matrix(distance_matrix, labels)
    
    clusters = labels.copy()
    while len(clusters) > 1:
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
        
        print(f"\nMerging clusters: {clusters[i]} and {clusters[j]} with distance {min_distance:.2f}")
        distance_matrix = update_distance_matrix(distance_matrix, i, j)
        clusters[i] = f"{clusters[i]}{clusters[j]}"
        clusters.pop(j)
        print("Updated Distance Matrix:")
        print_lower_triangular_matrix(distance_matrix, clusters)

if __name__ == "__main__":
    filename = 'hier.csv'  
    distance_matrix = load_lower_triangular_matrix(filename)
    if distance_matrix is None or len(distance_matrix) == 0:
        print("Error: Data could not be loaded or is empty.")
    else:
        labels = ['A', 'B', 'C', 'D', 'E']
        agglomerative_clustering_single_linkage(distance_matrix, labels)
