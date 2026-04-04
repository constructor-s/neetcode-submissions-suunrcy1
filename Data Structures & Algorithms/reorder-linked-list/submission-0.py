# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        head.prev = None
        front = head
        back = head
        while back.next:
            back.next.prev = back
            back = back.next
        
        while front != back:
            front_next = front.next
            front.next = back
            back.next = front_next
            front = front_next
            if front == back:
                back.next = None
                break
            back = back.prev
            back.next = None
            
        