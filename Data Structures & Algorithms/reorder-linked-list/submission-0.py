# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        prev = s
        cur = prev.next
        prev.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        tail = prev
        while head:
            temp1 = head.next
            head.next = tail
            temp2 = tail.next
            tail.next = temp1
            head = temp1
            tail = temp2