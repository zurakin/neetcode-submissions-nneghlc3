"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        res = Node(-1, None, None)
        copies = {}
        current = head
        while current is not None:
            copies[current] = Node(current.val)
            current = current.next

        current = head
        while current is not None:
            copy = copies[current]
            if current.next is not None:
                copy.next = copies[current.next]
            if current.random is not None:
                copy.random = copies[current.random]
            current = current.next

        return copies[head]