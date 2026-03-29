# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = [p]
        queue2 = [q]

        while len(queue1) > 0 and len(queue2) > 0:
            n1 = queue1.pop() 
            n2 = queue2.pop()

            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False 
            queue1.extend([n1.left, n1.right])
            queue2.extend([n2.left, n2.right])

        return len(queue1) == len(queue2) # both should be 0