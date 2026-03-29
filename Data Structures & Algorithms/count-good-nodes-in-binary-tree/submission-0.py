# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = 0
        queue = [(root, float('-inf'))]
        while len(queue) > 0:
            qe, threshold = queue.pop()
            if qe is None:
                continue 
            if qe.val >= threshold:
                res += 1
                threshold = qe.val
            queue.extend([(qe.left, threshold), (qe.right, threshold)])
        return res
