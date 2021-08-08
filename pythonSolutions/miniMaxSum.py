def miniMaxSum(arr):
    sort = sorted(arr)
    print(sum(sort[:4]),sum(sort[1:]))


arr = [1,3,5,7,9]
miniMaxSum([1,3,5,7,9])