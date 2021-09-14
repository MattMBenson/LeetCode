from node import ListNode

def mergeTwoLists(self, a:ListNode, b: ListNode) -> ListNode:
    tempA = None
    tempB = None

    while True:
        if a.val >= b.val:
            