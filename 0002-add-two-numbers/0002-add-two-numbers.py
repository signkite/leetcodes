# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# linked list to integer
# 3 -> 2 -> 1: ListNode to 123: int
def list2num(num_list):
    n_sum = 0
    digit = 0
    while num_list is not None:
        n_sum += num_list.val * (10**digit)
        digit += 1
        num_list = num_list.next
    return n_sum
    

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = list2num(l1)
        num2 = list2num(l2)
        
        # sum to linked list
        n_sum = num1 + num2
        n_sum = str(n_sum)
        
        node = None
        for c in n_sum:
            node = ListNode(int(c), node)
        
        return node
        