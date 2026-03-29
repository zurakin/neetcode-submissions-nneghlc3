# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(-1, head)
        left = res
        start = head
        previous = head
        current = head.next
        while current is not None:
            tempCurrent = current
            for _ in range(k-2):
                tempCurrent = tempCurrent.next
                if tempCurrent is None:
                    return res.next

            for _ in range(k-1):
                next = current.next
                current.next = previous
                previous = current
                current = next

            left.next = previous
            start.next = current

            left = start
            start = current
            previous = current
            if current is None:
                return res.next
            current = current.next
            
        return res.next
            