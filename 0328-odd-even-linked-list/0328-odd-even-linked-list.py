# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        odd_cur = head
        even_cur = head.next
        even_head = head.next
        cur = head.next.next
        cnt = 3
        while cur:
            if cnt % 2 == 0:
                even_cur.next = cur
                
                even_cur = cur
            else:
                odd_cur.next = cur
                odd_cur = cur
            cur = cur.next
            cnt += 1
            
        even_cur.next = None
        odd_cur.next = even_head
        return head