import csv
from itertools import chain, combinations

def readFile(filename):
    with open(filename, 'r') as file:
        robj = csv.reader(file)
        data = [row for row in robj]
    
    transactions = []
    
    for row in data[1:]:
        transaction = set(item for item in row[1:] if item)
        transactions.append(transaction)
    
    return transactions

def getAllItemsets(transactions):
    unique_items = set(item for transaction in transactions for item in transaction)
    all_itemsets = list(chain.from_iterable(combinations(unique_items, r) for r in range(1, len(unique_items) + 1)))
    
    print(f"Number of possible itemsets: {len(all_itemsets)}")
    return all_itemsets

def writeItemsetsToFile(filename, itemsets):
    with open(filename, 'w', newline='') as file:
        wobj = csv.writer(file)
        wobj.writerow(['Itemset'])
        for itemset in itemsets:
            wobj.writerow([', '.join(itemset)])

if __name__ == '__main__':
    ip = 'ip.csv'
    op = 'frequent_itemsets.csv'
    
    transactions = readFile(ip)
    all_itemsets = getAllItemsets(transactions)
    writeItemsetsToFile(op, all_itemsets)
