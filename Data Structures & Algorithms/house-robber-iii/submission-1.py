# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        mem = {}
        def dfs(node, parentWasRobbed):
            if node is None:
                return 0
            if (node, parentWasRobbed) in mem:
                return mem[(node, parentWasRobbed)]
            res = dfs(node.left, False) + dfs(node.right, False)

            if not parentWasRobbed:
                res = max(res, node.val + dfs(node.left, True) + dfs(node.right, True))
            
            mem[(node, parentWasRobbed)] = res
            return res        
        return dfs(root, False)