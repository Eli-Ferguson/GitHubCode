# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        
        if not head :
            return None
        if not head.next :
            return None
        if not head.next.next :
            head.next = None
            return head

        mid, end = head, head.next.next

        while True :
            
            if end.next and end.next.next :
                end = end.next.next
                mid = mid.next
            elif end.next :
                mid = mid.next
                mid.next = mid.next.next
                break
            else :
                mid.next = mid.next.next
                break
        
        return head

# Beats 95.63% Runtime, 1674ms
# Beats 24.17% Memory, 62.9mb