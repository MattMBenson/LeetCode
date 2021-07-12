class Solution(object):
    def removeDuplicates(self, nums):
        hashMap = {}
        i = 0 #count/key 
        k = 0 #amt of nums removed
        # i + k = len(nums)
        # k value to be returned
        for value in nums:
            if not (value in hashMap.values()):
                hashMap[i] = value
                i+=1
            else:
                k+=1

        for x in range(0,len(nums)):
            if x > i-1:
                nums[x] = None
            else: 
                nums[x] = hashMap[x]
        return k

test = Solution()
nums = [1,1,2]
print(test.removeDuplicates(nums))
print(nums)
        
