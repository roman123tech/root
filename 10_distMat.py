import csv

def read_csv(filename):
    with open(filename, mode='r') as file:
        reader=csv.DictReader(file)
        rows=list(reader)
    return rows

def write_csv(output_file,matrix,header):
    with open(output_file,mode='w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(header)
        for row in matrix:
            writer.writerow(row)

def getCentroids(x,y):
    return sum(x)/len(x),sum(y)/len(y)

def euclidean(x1,y1,x2,y2):
    return round(((x2-x1)**2+(y2-y1)**2)**0.5,2)


filename='circles.csv'
rows=read_csv(filename)
# print(rows)
x=[float(row['x']) for row in rows]
y=[float(row['y']) for row in rows]

cx,cy=getCentroids(x,y)
print(f"Centroids are: ({cx:0.2f},{cy:0.2f})")
n=len(x)
distanceMatrix=[['']*n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        distanceMatrix[i][j]=euclidean(x[i],y[i],x[j],y[j])

header=[val+1 for val in range(n)]
# print(header)

print("Distance Matrix is ")

for i in range(n):
    print(f'{" ".join(str(val) for val in distanceMatrix[i])}')

output_file='mat.csv'
write_csv(output_file,distanceMatrix,header)