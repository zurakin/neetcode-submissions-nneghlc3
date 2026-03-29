class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodeToComponent = {}
        for a, b in edges:
            if a in nodeToComponent and b in nodeToComponent and nodeToComponent[a] == nodeToComponent[b]:
                return [a, b]
            toMerge = []
            if a not in nodeToComponent:
                nodeToComponent[a] = set([a])
            if b not in nodeToComponent:
                nodeToComponent[b] = set([b])
            comp1 = nodeToComponent[a]
            comp2 = nodeToComponent[b]
            comp1.update(comp2)
            for node in comp2:
                nodeToComponent[node] = comp1
            
        return []