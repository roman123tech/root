import csv

def read_csv(filename):
    with open(filename,mode='r') as file:
        reader=csv.DictReader(file)
        rows=list(reader)
    return rows


filename='financial_risk_analysis.csv'
rows=read_csv(filename)
headers=list(rows[0].keys())

cnt=0
for val in headers:
    print(cnt,val)
    cnt+=1
column=headers[int(input("Enter the column number to apply binning: "))]

values=[float(row[column]) for row in rows]



numBins=int(input("Enter Number of bins to be formed: "))
ele_per_bin=(len(values)+numBins-1)//numBins #equivalent to ceil

values.sort()

bins=[values[i:i+ele_per_bin] for i in range(0,len(values),ele_per_bin)]
# print(bins)

for idx,bin in enumerate(bins):
    print(f'\nBin {idx}: {bin}')
    print("\nBin by mean")
    mean=sum(bin)/len(bin)
    
    bin_mean=",".join(str(mean) for i in range(len(bin)))
    print(f"[ {bin_mean} ]")
    
    print("\nBin by boundaries")
    minm=min(bin)
    maxm=max(bin)
    bin_bound=[str(maxm) if val-minm>=maxm-val else str(minm) for val in bin]
    print("["+",".join(bin_bound)+"]")

    print("\n Bin by Median")

    median=bin[len(bin)//2]
    bin_median=[str(median)]*len(bin)
    print(f'[ {",".join(bin_median)}]')




