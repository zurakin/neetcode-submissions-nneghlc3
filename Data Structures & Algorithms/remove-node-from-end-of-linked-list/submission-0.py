# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = self.length(head)
        target = N - n
        temp = ListNode(-1, head)
        current = temp
        for _ in range(target):
            current = current.next
        if current.next is not None:
            current.next = current.next.next
        return temp.next



    def length(self, head: Optional[ListNode]) -> int:
        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next 
        return size
