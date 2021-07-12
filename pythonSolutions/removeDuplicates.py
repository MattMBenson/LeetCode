class Solution(object):
    def removeDuplicates(self, nums):
        hashMap = {}
        i = 0 #count/key 
        k = 0 #amt of nums removed
        for value in nums:
            if not (value in hashMap.values()):
                hashMap[i] = value
                i+=1
            else:
                k+=1

        for x in range(0,i):
            nums(i) = hashMap[i]
        return k
        
