# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                serialized.append('N')
            else:
                serialized.append(str(node.val))
                queue.extend([node.left, node.right])
        return ",".join(serialized)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        firstToken = tokens.pop(0)
        if firstToken == 'N':
            return None
        head = TreeNode(int(firstToken))
        queue = [head]
        while len(queue) > 0:
            node = queue.pop(0)
            leftToken = tokens.pop(0)
            rightToken = tokens.pop(0)
            if leftToken != 'N':
                node.left = TreeNode(int(leftToken))
                queue.append(node.left)
            if rightToken != 'N':
                node.right = TreeNode(int(rightToken))
                queue.append(node.right)
        return head

        
