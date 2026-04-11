class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort()
        res = [0 for _ in range(len(queries))]
        heap = []
        currentInterval = 0
        for query, idx in queries:
            while currentInterval < len(intervals) and intervals[currentInterval][0] <= query:
                interval = intervals[currentInterval]
                heapq.heappush(heap, (interval[1]-interval[0]+1, interval[1]))
                currentInterval += 1
            while True:
                if not heap:
                    res[idx] = -1
                    break
                if heap[0][1] >= query:
                    res[idx] = heap[0][0]
                    break
                heapq.heappop(heap)
        return res

