from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    mySet = set()
    for n in nums:
        mySet.add(n)
    print(len(mySet),len(nums))
    return len(mySet) != len(nums)

