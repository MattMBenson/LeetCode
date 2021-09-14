class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def reverseList(self, head: ListNode) -> ListNode:
    curr = head
    prev = None
    nextN = None

    while curr is not None:
        nextN = curr.next
        curr.next = prev
        prev = curr
        curr = nextN
    
    return prev
