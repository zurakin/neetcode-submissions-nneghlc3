# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        self.res = root.val
        self.maxPathSumRec(root)
        return self.res
    
    def maxPathSumRec(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftPath = self.maxPathSumRec(root.left)
        rightPath = self.maxPathSumRec(root.right)
        maxGivenRoot = root.val + max(0, leftPath) + max(0, rightPath)
        self.res = max(self.res, maxGivenRoot)
        return root.val + max(leftPath, rightPath, 0)
        