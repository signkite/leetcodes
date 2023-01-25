# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        temp_list = []
        node = head
        while node is not None:
            temp_list.append(node.val)
            node = node.next
        
        rev_list = temp_list.copy()
        rev_list.reverse()
        if temp_list == rev_list:
            return True
        else:
            return False
        
            