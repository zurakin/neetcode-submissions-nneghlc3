class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = nums[0]
        smallest = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            possibilities = (n, n*largest, n*smallest)
            largest = max(possibilities)
            smallest = min(possibilities)
            res = max(res, largest)

        return res