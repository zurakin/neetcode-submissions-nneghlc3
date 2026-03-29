# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRec(root, float('-inf'), float('+inf'))
        

    def isValidBSTRec(self, node, inf, sup):
        if node is None:
            return True
        print(node.val, inf, sup)
        if node.val <= inf or node.val >= sup:
            return False
        return self.isValidBSTRec(node.left, inf, node.val) and self.isValidBSTRec(node.right, node.val, sup)
        