from typing import List 
import sys

def maxArea(nums: List[int]) -> int:
    maxNum = 0
    left = 0
    right = len(nums) - 1

    while left != right:
        # calculate with current values
        wall = min(nums[left], nums[right])
        foundArea = wall * (right - left)

        if foundArea > maxNum:
            maxNum = foundArea
        
        # move based on next values
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    
    return maxNum

nums = [1,2,4,3]
height = [1,8,6,2,5,4,9,3,7]
print(maxArea(height))
