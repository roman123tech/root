import csv

def read_csv(filename):
    with open(filename) as file:
        reader=csv.DictReader(file)
        rows=list(reader)
    return rows


def getCoeff(a,b):
    n=len(a)
    a_mean=sum(a)/n
    b_mean=sum(b)/n
    numerator=sum((a[i]-a_mean)*(b[i]-b_mean) for i in range(n))
    denominator=sum((a[i]-a_mean)**2 for i in range(n))
    m=numerator/denominator
    c=b_mean-m*a_mean
    return m,c

filename='real_estate.csv'
rows=read_csv(filename)
# print(rows)

headers=list(rows[0].keys())
a=[float(row[headers[0]]) for row in rows]
b=[float(row[headers[1]]) for row in rows]
m,c=getCoeff(a,b)
print(f"y={m:0.3f}x+{c:0.3f}")
