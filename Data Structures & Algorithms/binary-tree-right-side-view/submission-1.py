# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [root] if root is not None else []
        while len(queue) > 0:
            res.append(queue[-1].val)
            newQueue = []
            for n in queue:
                if n.left is not None:
                    newQueue.append(n.left)
                if n.right is not None:
                    newQueue.append(n.right)
            queue = newQueue
        return res