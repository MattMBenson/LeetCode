import sys
def maxSubArray(nums) -> int:
    maxSub = - sys.maxsize - 1
    localMax = 0
    n = len(nums)

    for i in range (0, n):
        # start new array
        if nums[i] > localMax + nums[i]:
            localMax = nums[i]

        # add to localMax
        else:
            localMax += nums[i]

        if localMax > maxSub:
            maxSub = localMax
        
    return maxSub

LIST = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(LIST))