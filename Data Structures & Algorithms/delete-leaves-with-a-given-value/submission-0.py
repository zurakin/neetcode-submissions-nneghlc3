# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if node is None:
                return True
            
            if dfs(node.left):
                node.left = None

            if dfs(node.right):
                node.right = None

            if node.left is None and node.right is None:
                return node.val == target

        if dfs(root):
            return None
        return root