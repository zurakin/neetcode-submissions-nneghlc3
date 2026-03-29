class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        pivot = nums[0]
        smaller = [n for n in nums[1:] if n < pivot]
        larger = [n for n in nums[1:] if n >= pivot]
        print(smaller, pivot, larger, k)
        if len(larger) == k-1:
            return pivot
        if len(larger) < k-1:
            return self.findKthLargest(smaller, k-len(larger)-1)
        return self.findKthLargest(larger, k)