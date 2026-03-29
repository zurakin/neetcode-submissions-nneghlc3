# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortoise = head

        while hare is not None and tortoise is not None:
            tortoise = tortoise.next
            hare = hare.next
            if hare is None:
                return False
            hare = hare.next
            if hare == tortoise:
                return True

        return False
        