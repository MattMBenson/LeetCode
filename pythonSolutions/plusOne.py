from typing import List

def plusOne(digits: List[int]) -> List[int]:
    myList = list(reversed(digits))
    myList[0] += 1
    cur_num = myList[0]
    i = 0
    while (cur_num == 10):
        if (i + 1 < len(myList)):
            myList[i] = 0
            myList[i + 1] += 1
        else:
            myList[i] = 0
            myList.append(1)
        i += 1
        cur_num = myList[i]
    return list(reversed(myList))
    
    
digits = [4,3,2,1]
d = [9,9,9,9]
#test = [0]
print(plusOne(d))