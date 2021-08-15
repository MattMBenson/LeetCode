# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 2n Solution
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    count = 0
    curr = head
    stack = []

    while curr is not None:
        count += 1
        if left <= count <= right:
            stack.append(curr.val)
        curr = curr.next

    count = 0
    curr = head
    while curr is not None:
        count += 1
        if left <= count <= right:
            curr.val = stack.pop()
        curr = curr.next


