class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.heap = nums[max(0, len(nums)-k):]
        print(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            if val < self.heap[0]:
                return self.heap[0]
            heapq.heappop(self.heap)
        heapq.heappush(self.heap, val)
        print(self.heap)
        return self.heap[0]