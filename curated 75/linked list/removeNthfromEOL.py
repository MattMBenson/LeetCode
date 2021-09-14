from node import ListNode
def removeNthFromEnd(self, head:ListNode, n:int) -> ListNode:
    temp = None
    p = head
    count = 0

    while p != None:
        if count == n:
            temp = p.next
            
        
    