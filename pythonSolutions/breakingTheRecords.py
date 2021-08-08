from typing import List

def breakingRecords(scores:List)-> List:
    max_count = 0
    min_count = 0

    max_value = scores[0] 
    min_value = scores[0] 

    for n in range(1,len(scores)):
        num = scores[n]
        if num > max_value:
            max_value = num
            max_count += 1
        elif num < min_value:
            min_value = num
            min_count += 1
        
    return [max_count,min_count]

print(breakingRecords([12,24,10,24]))