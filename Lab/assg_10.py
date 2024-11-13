import numpy as np
import string

points = np.loadtxt("mat.csv", delimiter=",")
num_points = len(points)
distance_matrix = np.zeros((num_points, num_points))

for i in range(num_points):
    for j in range(i, num_points):
        dist = np.sqrt(np.sum((points[i] - points[j]) ** 2))
        distance_matrix[i, j] = dist
        distance_matrix[j, i] = dist

centroid = np.mean(points, axis=0)

lower_triangular = np.tril(distance_matrix)
for i in range(num_points):
    for j in range(i + 1, num_points):
        lower_triangular[i, j] = np.nan

labels = list(string.ascii_uppercase[:num_points])

print("Lower Triangular Distance Matrix:\n")
print("     " + "  ".join(f"{label:>8}" for label in labels))
for i, row in enumerate(lower_triangular):
    row_str = " ".join(f"{value:>8.2f}" if not np.isnan(value) else "        " for value in row)
    print(f"{labels[i]:<3} {row_str}")

print("\nCentroid of the cluster:")
print(f"Coordinates: {centroid}")
