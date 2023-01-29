# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # corner case
        if head is None or head.next is None:
            return head
        
        rev = None
        next_node = head
        while next_node.next is not None:
            rev, next_node, rev.next = next_node, next_node.next, rev
        rev, rev.next = next_node, rev
        
        return rev
        
            
        
            