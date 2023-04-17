# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        nodeSet = set()
        
        while headA is not None:
            nodeSet.add(headA)
            headA = headA.next
        
        while headB is not None:
            if headB in nodeSet:
                return headB
            headB = headB.next
        
        return None

# Beats 93.26% Runtime, 150ms
# Beats 16.44% Memory, 30.1mb