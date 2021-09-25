import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        stack = []
        while curr != None:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        count = 0
        halfWayPoint = math.floor(len(stack) / 2)
        while curr != None and count <= halfWayPoint:
            comparator = stack.pop()
            if curr.val != comparator:
                return False
                
            count += 1
            curr = curr.next
        return True


testCase = Solution()
print(testCase.isPalindrome([5]))