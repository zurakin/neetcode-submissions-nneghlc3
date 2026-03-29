class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-weight for weight in stones]
        heapq.heapify(heap)
        while len(heap) > 0:
            if len(heap) == 1:
                return -heap[0]
            heaviest = -heapq.heappop(heap)
            secondHeaviest = -heapq.heappop(heap)
            resultingStoneWeight = abs(heaviest - secondHeaviest)
            if resultingStoneWeight > 0:
                heapq.heappush(heap, -resultingStoneWeight)
        return 0
