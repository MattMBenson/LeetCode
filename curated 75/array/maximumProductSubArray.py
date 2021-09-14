# naive approach
from typing import List
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProductFound = -sys.maxsize - 1
        n = len(nums)

        for i in range(0,n):
            localProduct = nums[i]
            for j in range(0,n):

                if i !=j:
                    localProduct *= nums[j]

                if localProduct > maxProductFound:
                    maxProductFound = localProduct
    
        return maxProductFound
    
test = Solution()
print(test.maxProduct([2,3,-2,4]))