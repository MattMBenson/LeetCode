class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        for i in range(0,len(haystack)):
            end = (len(needle)+i)
            splice = haystack[i:end]
            if splice == needle:
                return i
                
        return -1

test = Solution()
print(test.strStr("Happy","Happ"))
        