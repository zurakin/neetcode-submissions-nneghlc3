"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clones = {}
        visited = set()
        queue = [node]
        while len(queue) > 0:
            current = queue.pop(0)
            if current in visited:
                continue
            if current not in clones:
                clones[current] = Node(current.val)
            visited.add(current)
            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
                clones[current].neighbors.append(clones[neighbor])
        return clones[node]