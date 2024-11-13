import csv

def read_csv(filename):
    with open(filename,mode='r') as file:
        reader=csv.DictReader(file)
        rows=list(reader)
    return rows

def findCorrelation(x,y):
    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    sum_xy=sum((x[i]-x_mean)*(y[i]-y_mean) for  i in range(len(x)))
    sum_xx=sum((x[i]-x_mean)**2 for i in range(len(x)))
    sum_yy=sum((y[i]-y_mean)**2 for i in range(len(y)))
    return sum_xy/(sum_xx*sum_yy)**0.5

file='correlation_data.csv'
rows=read_csv(file)
headers=list(rows[0].keys())
x=[float(row[headers[0]]) for row in rows]
y=[float(row[headers[1]]) for row in rows]
coeff=findCorrelation(x,y)
print(f'Correlation between {headers[0]} and {headers[1]} if {coeff:0.4f}')


