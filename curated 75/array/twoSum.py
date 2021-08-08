from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dic = dict()
    ans = []

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dic:
            ans.append(dic[diff])
            ans.append(i)
        else:
            dic[nums[i]] = i
    return ans

nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))

