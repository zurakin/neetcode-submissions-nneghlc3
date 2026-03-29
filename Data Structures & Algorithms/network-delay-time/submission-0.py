class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = [[] for _ in range(n)]
        for source, target, time in times:
            neighbors[source-1].append((time, target-1))

        visited = set()
        priorityQueue = [(0, k-1)]
        while len(priorityQueue) > 0:
            time, node = heapq.heappop(priorityQueue)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            for neighborTime, neighbor in neighbors[node]:
                heapq.heappush(priorityQueue, (time+neighborTime, neighbor))
        return -1