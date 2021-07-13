#not finished
class Solution(object):
    def lengthOfLastWord(self,s):
        space = " "
        idxLastSpace = 0
        #finds last space 
        for i in range(0,len(s)):
            if s[i] == space:
                idxLastSpace = i
        
        
        return len(s)-1-idxLastSpace    
