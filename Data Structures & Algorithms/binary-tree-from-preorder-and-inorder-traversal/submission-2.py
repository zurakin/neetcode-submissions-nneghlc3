# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i, n in enumerate(inorder):
            index[n] = i
        return self.buildTreeRec(preorder, index)

    def buildTreeRec(self, preorder, index):
        if len(preorder) == 0:
            return None
        left = []
        right = []
        for v in preorder[1:]:
            if index[v] < index[preorder[0]]:
                left.append(v)
            else:
                right.append(v)
        return TreeNode(preorder[0], self.buildTreeRec(left, index), self.buildTreeRec(right, index))