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

def candidateSet(prevFreqItem, k):
    candidates = set()
    prevFreqItem = list(prevFreqItem)
    
    for i in range(len(prevFreqItem)):
        for j in range(i + 1, len(prevFreqItem)):
            newFreqSet = prevFreqItem[i].union(prevFreqItem[j])
            if len(newFreqSet) == k:
                candidates.add(frozenset(newFreqSet))
    
    return candidates

def support(transactions, candidates, minsup, total):
    itemSup = {}
    
    for transaction in transactions:
        for candidate in candidates:
            if candidate.issubset(transaction):
                itemSup[candidate] = itemSup.get(candidate, 0) + 1

    freqItem = {
        itemset: support / total
        for itemset, support in itemSup.items()
        if support / total >= minsup
    }
    
    return freqItem, itemSup

def apriori(transactions, minsup):
    total = len(transactions)
    k = 1
    candidates = [frozenset([item]) for item in set(item for transaction in transactions for item in transaction)]
    freqItemSet = []
    itemSupportDict = {}

    while candidates:
        freqItem, itemSup = support(transactions, candidates, minsup, total)
        
        if not freqItem:
            break
        
        freqItemSet.append(freqItem)
        itemSupportDict.update(itemSup)
        candidates = candidateSet(freqItem.keys(), k + 1)
        k += 1
    
    return freqItemSet, itemSupportDict

def writeFile(filename, freqItemSet):
    with open(filename, 'w', newline='') as file:
        wobj = csv.writer(file)
        wobj.writerow(['Itemset', 'Support'])
        
        for k_itemsets in freqItemSet:
            for itemset, support in k_itemsets.items():
                wobj.writerow([', '.join(itemset), support])

def getSubsets(itemset):
    return chain.from_iterable(combinations(itemset, r) for r in range(1, len(itemset)))

def generateAssociationRules(freqItemSet, itemSupportDict, minconf):
    rules = []
    
    for k_itemsets in freqItemSet:
        for itemset in k_itemsets.keys():
            subsets = list(getSubsets(itemset))
            
            for subset in subsets:
                A = frozenset(subset)
                B = itemset - A
                
                if B:
                    support_AB = itemSupportDict[itemset]
                    support_A = itemSupportDict[A]
                    confidence = support_AB / support_A
                    
                    if confidence >= minconf:
                        rules.append((A, B, confidence))
    
    return rules

def writeRules(filename, rules):
    with open(filename, 'w', newline='') as file:
        wobj = csv.writer(file)
        wobj.writerow(['Antecedent', 'Consequent', 'Confidence'])
        
        for A, B, confidence in rules:
            wobj.writerow([', '.join(A), ', '.join(B), confidence])

if __name__ == '__main__':
    ip = 'ip.csv'
    op = 'freqItem.csv'
    rule_op = 'assocRules.csv'

    minsup = float(input("Enter minimum support (as a decimal, e.g., 0.5): "))
    minconf = float(input("Enter minimum confidence (as a decimal, e.g., 0.6): "))

    transactions = readFile(ip)
    freqItemSet, itemSupportDict = apriori(transactions, minsup)
    writeFile(op, freqItemSet)
    
    rules = generateAssociationRules(freqItemSet, itemSupportDict, minconf)
    writeRules(rule_op, rules)
