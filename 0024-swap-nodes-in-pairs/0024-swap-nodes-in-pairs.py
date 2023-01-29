# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev, cur = head, head.next
        head = cur
        while cur is not None:
            adv = cur.next
            cur.next, prev.next = prev, adv
            if adv is None or adv.next is None:
                break
            else:
                prev.next = adv.next
            prev, cur = adv, adv.next
        
        return head
        
            