# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)[1]

    def height(self, node):
        if node is None:
            return 0, True
        leftHeight, leftBalanced = self.height(node.left)
        if not leftBalanced:
            return -1, False
        rightHeight, rightBalanced = self.height(node.right)
        if not rightBalanced:
            return -1, False
        return 1 + max(leftHeight, rightHeight), abs(leftHeight-rightHeight) <= 1
        