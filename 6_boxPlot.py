import csv

def read_csv(filename):
    with open(filename,mode='r') as file:
        reader=csv.DictReader(file)
        rows=list(reader)
    return rows

def getQuartiles(values):
    n=len(values)
    req1=(n-1)/4
    req2=((n-1)*3)/4
    q1=-1
    q2=-1
    if req1.is_integer():
        q1=values[int(req1)]
    else:
        q1=(values[int(req1)]+values[int(req1)+1])/2

    if req2.is_integer():
        q2=values[int(req2)]
    else:
        q2=(values[int(req2)]+values[int(req2)+1])/2

    return q1,q2

def getMedian(values):
    n=len(values)
    if n%2!=0:
        return values(n/2)
    else:
        l=n//2
        r=l-1
        return (values[l]+values[r])/2

def getFNS(column,rows):
    values=[int(row[column]) for row in rows]
    values.sort()
    # print(values)
    minm=min(values)
    maxm=max(values)
    median=getMedian(values)
    q1,q3=getQuartiles(values)
    print(f'minm: {minm} maxm: {maxm} q1: {q1} q3: {q3} median: {median}')
    



filename='financial_risk_analysis.csv'
rows=read_csv(filename)
# print(rows)
headers=list(rows[0].keys())
# print(headers)

print("Select a column to get 5 number summary for: ")
for idx,val in enumerate(headers):
    print(idx,val)

column=headers[int(input("Enter column number: "))]
# print(column)
getFNS(column,rows)

