# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        queue = [(root, False)]
        while len(queue) > 0:
            node, leftAlreadyExplored = queue.pop()
            if leftAlreadyExplored:
                counter += 1
                if counter == k:
                    return node.val
                if node.right is not None:
                    queue.append((node.right, False))
            else:
                queue.append((node, True))
                if node.left is not None:
                    queue.append((node.left, False))
        return -1