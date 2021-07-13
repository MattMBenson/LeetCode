class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
       prev = None
       curr = head

       if (head == None):
           return head

       while True:
            next = curr.next
            curr.next = prev
            prev = curr

            if next == None:
                return curr

            curr = next