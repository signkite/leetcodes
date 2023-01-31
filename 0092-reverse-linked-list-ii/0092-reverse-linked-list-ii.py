# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        val_list = []
        
        # 값을 뒤집을 부분의 시작 노드까지 rev를 옮김
        rev = head
        for _ in range(1, left):
            rev = rev.next
        rev_head = rev
        
        # 뒤집을 부분의 값을 val_list에 순차적으로 추가
        for _ in range(left, right + 1):
            val_list.append(rev.val)
            rev = rev.next
        
        # val_list의 순서를 뒤집은 후 노드에 순차적으로 반영
        val_list.reverse()
        rev = rev_head
        for i in range(right - left + 1):
            rev.val = val_list[i]
            rev = rev.next
        
        return head