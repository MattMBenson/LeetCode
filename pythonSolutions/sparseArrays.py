from typing import List

def matchingStrings(strings:List, queries:List)-> List:
    hashMap = dict()
    # str : amount
    results = []
    
    for s in strings:
        if s not in hashMap:
            hashMap[s] = 1
        else:
            hashMap[s] = hashMap.get(s) + 1
    
    for s in queries:
        if s in hashMap:
            results.append(hashMap.get(s))
        else:
            results.append(0)
    
    print(results)

a = ['ab','ab','abc']
b = ['ab','abc','bc']

matchingStrings(a,b)

