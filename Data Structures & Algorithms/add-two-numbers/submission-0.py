# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1, None)
        current = res
        residue = 0
        while l1 is not None or l2 is not None or residue != 0:
            s = residue
            residue = 0
            if l1 is not None:
                s += l1.val
                l1 = l1.next
            if l2 is not None:
                s += l2.val
                l2 = l2.next
            if s >= 10:
                residue = 1
                s -= 10
            current.next = ListNode(s, None)
            current = current.next
        return res.next