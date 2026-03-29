class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = [[] for _ in range(n)]
        visited = set()
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(start):
            visited.add(start)
            for n in neighbors[start]:
                if n not in visited:
                    dfs(n)

        counter = 0
        for i in range(n):
            if i in visited:
                continue
            counter += 1
            dfs(i)

        return counter
