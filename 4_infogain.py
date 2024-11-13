import csv
import math 

def read_csv(filename):
    with open(filename,mode='r') as file:
        reader=csv.DictReader(file)
        rows=list(reader)
    return rows

def getEntropy(labels):
    
    freq={}
    for label in labels:
        freq[label]=freq.get(label,0)+1
    
    ent=0.0
    total=len(labels)

    for count in freq.values():
        prob=count/total
        if prob>0:
            ent-=prob*math.log2(prob)
    
    return ent


def info_gain(targetClass,feature,rows,labels):
    base_ent=getEntropy(labels)
    subsets={}
    for row in rows:
        val=row[feature]

        if val not in subsets:
            subsets[val]=[]
        subsets[val].append(row[targetClass])
    weighted_entropy=sum(len(attr)/len(labels)*getEntropy(attr) for attr in subsets.values())
    gain=base_ent-weighted_entropy
    return base_ent,gain,subsets




file='datasheet.csv'
rows=read_csv(file)
headers=list(rows[0].keys())
features=headers[:-1]
targetClass=headers[-1]
labels=[row[targetClass] for row in rows]


print(f'Initial Entropy is {getEntropy(labels)}')
for feature in features:
    base_ent,gain,subsets=info_gain(targetClass,feature,rows,labels)
    print(feature, gain)
    for key,val in subsets.items():
        print(key,getEntropy(val))