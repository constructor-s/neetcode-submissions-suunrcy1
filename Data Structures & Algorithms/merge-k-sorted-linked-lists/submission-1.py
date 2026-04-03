# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import *

# ListNode.__lt__ = lambda self, other: self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists:
            lists[0].__class__.__lt__ = lambda self, other: self.val < other.val
        heads = []
        res = None
        res_tail = None

        for i in range(len(lists)):
            if lists[i]:
                node = lists[i]
                heappush(heads, node)

        while heads:
            node = heappop(heads)
            if node.next:
                heappush(heads, node.next)
            node.next = None
            if res is None:
                res = node
                res_tail = node
            else:
                res_tail.next = node
                res_tail = node

        return res
