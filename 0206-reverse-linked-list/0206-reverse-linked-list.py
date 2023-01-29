# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node = None, head
        
        while node is not None:
            node.next, prev, node = prev, node, node.next
        
        return prev
            
        
        