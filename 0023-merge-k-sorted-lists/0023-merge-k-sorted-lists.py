# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # (node value, index in lists)
        heap = []
        
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            heapq.heappush(heap, (lists[i].val, i))
           
        # There are no element in heap
        if not heap:
            return None
        
        val, i = heapq.heappop(heap)
        cur = head = ListNode(val)
        lists[i] = lists[i].next
        if lists[i] != None:
            heapq.heappush(heap, (lists[i].val, i))
        
        while any(lists):  # stop when all lists is None
            val, i = heapq.heappop(heap)
            lists[i] = lists[i].next
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i))
            cur.next = ListNode(val)
            cur = cur.next
            
        return head