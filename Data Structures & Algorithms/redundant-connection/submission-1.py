class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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
            print(connectedComponents)
        return []