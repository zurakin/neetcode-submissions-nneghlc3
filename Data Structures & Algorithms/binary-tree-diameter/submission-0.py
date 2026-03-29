# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.bestDiameter = 0
        self.maxDepth(root)
        return self.bestDiameter
        

    def maxDepth(self, root: Optional[TreeNod]) -> int:
        if root is None:
            return 0
        leftDepth = self.maxDepth(root.right)
        rightDepth = self.maxDepth(root.left)
        self.bestDiameter = max(self.bestDiameter, leftDepth+rightDepth)
        return 1 + max(leftDepth, rightDepth)    