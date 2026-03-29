class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = (point[0]**2 + point[1]**2)
            pointToInsert = [-distance, point]
            if len(heap) >= k:
                furthest = heapq.heappop(heap)
                if abs(furthest[0]) < distance:
                    pointToInsert = furthest
            heapq.heappush(heap, pointToInsert)
        return [point[1] for point in heap]

