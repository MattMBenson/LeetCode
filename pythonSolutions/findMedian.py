def findMedian(arr):
    new = sorted(arr)
    print(new)
    middle = len(new) / 2
    middle += 0.5
    return new[int(middle) - 1]


arr = [1,5,7,3,10]
print(findMedian(arr))
