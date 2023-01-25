# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        answer_node = answer_head = ListNode()
        node1 = list1
        node2 = list2
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                answer_node.next = node1
                node1 = node1.next
            else:
                answer_node.next = node2
                node2 = node2.next
            print('*', answer_node.val)
            answer_node = answer_node.next
        
        if node2 is not None:
            while node2 is not None:
                answer_node.next = node2
                answer_node = answer_node.next
                node2 = node2.next
        elif node1 is not None:
            while node1 is not None:
                answer_node.next = node1
                answer_node = answer_node.next
                node1 = node1.next
        return answer_head.next