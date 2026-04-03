# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        ptr1 = head # increment by 1
        ptr2 = head.next # increment by 2

        while ptr1 is not None and ptr2 is not None and ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if ptr2 is not None:
                ptr2 = ptr2.next

        if not ptr1 or not ptr2:
            return False
        else:
            return ptr1 == ptr2
