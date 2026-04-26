# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        previous = None
        current = root
        while current:
            previous = current
            if val < current.val:
                current = current.left
            else:
                current = current.right
        if previous.val < val:
            previous.right = TreeNode(val)
        else:
            previous.left = TreeNode(val)
        return root