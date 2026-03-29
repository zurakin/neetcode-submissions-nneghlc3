class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = [set() for _ in range(n)]
        for a, b in edges:
            if a == b:
                return False
            neighbors[a].add(b)
            neighbors[b].add(a)
        visited = set()
        def dfs(start):
            visited.add(start)
            visitedNeighborsCount = 0
            for neighbor in neighbors[start]:
                if neighbor in visited:
                    visitedNeighborsCount += 1
                    if visitedNeighborsCount > 1:
                        return False
                    continue
                if not dfs(neighbor):
                    return False
            return True

        return dfs(0) and len(visited) == n

    def validTreeDirected(self, n: int, edges: List[List[int]]) -> bool:
        parentsCount = [0 for _ in range(n)]
        for a, b in edges:
            parentsCount[b] += 1
            if parentsCount[b] > 1:
                return False
        rootCount = parentsCount.count(0)
        return rootCount == 1

        