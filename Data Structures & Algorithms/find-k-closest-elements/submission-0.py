class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [] # max heap
        for n in arr:
            heapq.heappush(heap, (-abs(x-n), -n))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted([-he[1] for he in heap])