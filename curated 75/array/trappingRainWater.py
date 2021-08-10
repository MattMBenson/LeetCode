from typing import List

def trap(nums: List[int]) -> int:
    maxHeight = max(nums)
    totalWater = 0

    for i in range(0,maxHeight):
        foundWall = False
        foundSecondWall = False
        waterOnLayer = 0
        possibleWater = 0
        for j in range(0,len(nums)):
            #block = 0 or 1. Space or wall
            block = nums[j] - i
            if not foundWall and block > 0:
                foundWall = True

            elif not foundSecondWall and block > 0:
                foundSecondWall = True

            elif foundWall and block == 0:
                possibleWater += 1

            if foundSecondWall:
                waterOnLayer += possibleWater
                possibleWater = 0
            
        totalWater += waterOnLayer

    return totalWater


temp = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(temp))