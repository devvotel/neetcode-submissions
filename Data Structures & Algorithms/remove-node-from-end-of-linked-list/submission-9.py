class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        length = 0
        cur = head
        while cur:
            length +=1 
            cur = cur.next
        print(length)

        target_node = length - n
        cur = head
        for i in range(target_node-1):
            cur = cur.next
        
        if target_node == 0:
            head = head.next

        else:
            cur.next = cur.next.next

        return head