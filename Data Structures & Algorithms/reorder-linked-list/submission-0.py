# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = self.length(head)
        N = (length + 1) // 2
        current = head
        for _ in range(N-1):
            current = current.next
        head2 = current.next
        current.next = None
        head2 = self.reverseList(head2)
        self.merge(head, head2)
        
    def merge(self, node1, node2):
        while node2 is not None:
            temp1 = node1.next
            temp2 = node2.next
            node1.next = node2
            node2.next = temp1
            node1 = temp1
            node2 = temp2


    def length(self, head: Optional[ListNode]) -> int:
        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next 
        return size

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current is not None:
            nextN = current.next
            current.next = previous 
            previous = current 
            current = nextN
        return previous
              