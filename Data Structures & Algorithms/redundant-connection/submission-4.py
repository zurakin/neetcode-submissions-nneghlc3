class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]

    def union(self, i, j):
        parent1 = self.find(i)
        parent2 = self.find(j)
        self.parent[parent2] = parent1

    def find(self, i):
        current = i
        while self.parent[current] != current:
            current = self.parent[current]
        return current


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjointSet = DisjointSet(len(edges))

        for a, b in edges:
            if disjointSet.find(a) == disjointSet.find(b):
                return [a, b]
            disjointSet.union(a, b)


    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
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

    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        connectedComponents = []
        for a, b in edges:
            toMerge = []
            newConnectedComponents = []
            while len(connectedComponents) > 0:
                component = connectedComponents.pop()
                if a in component and b in component:
                    return [a, b]
                if a in component or b in component:
                    toMerge.append(component)
                else:
                    newConnectedComponents.append(component)
            connectedComponents = newConnectedComponents
            merged = set().union(*toMerge)
            merged.add(a)
            merged.add(b)
            connectedComponents.append(merged)
        return []