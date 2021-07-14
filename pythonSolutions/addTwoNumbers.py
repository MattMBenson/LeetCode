#med difficulty, passed intial test but failed subsequent test horrible lol
#unfinished https://leetcode.com/problems/add-two-numbers/submissions/
class ListNode:     
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(0)
        tmpNode = head
        prevTmp = None
        while True:
            carry = 0
            #reached end of list
            if l1 == None and l2 == None:
                if tmpNode.val == 0: #no end carry
                    prevTmp.next = None #clear the potential carry node waiting
                return head

            if l1 == None and l2 != None:
                sum = 0 + l2.val
            elif l1 != None and l2 == None:
                sum = l1.val + 0
            else:
                sum = l1.val + l2.val

            if sum >= 10:
                carry = sum % 10
                if sum % 10 == 0:
                    carry = 1
                sum = 0
            #add to current node with val sum
            #add new node.next with val carry
            tmpNode.val += sum
            tmpNode.next = ListNode(carry)
            prevTmp = tmpNode
            tmpNode = tmpNode.next

            #advance pointers
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            

            
            