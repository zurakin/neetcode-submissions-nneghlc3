# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # assert left > 0
        anchor = ListNode(-1, head) # To handle corner cases
        leftNode = anchor
        leftMinus1Node = None
        for _ in range(left):
            leftMinus1Node = leftNode
            leftNode = leftNode.next

        prev = leftNode
        current = leftNode.next
        for _ in range(right-left):
            nextCurrent = current.next

            current.next = prev
            prev = current
            current = nextCurrent

        leftMinus1Node.next = prev
        leftNode.next = current

        return anchor.next

        
