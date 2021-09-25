# naive approach
from typing import List
import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxFound = -sys.maxsize - 1
        for i in range(0, len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                curr *= nums[j]
                if curr > maxFound:
                    maxFound = curr
        return maxFound



sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))
