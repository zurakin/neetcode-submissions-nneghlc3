class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = nums[0]
        smallest = nums[0]
        res = nums[0]
        for n in nums[1:]:
            possibilities = (n, n*largest, n*smallest)
            largest = max(possibilities)
            smallest = min(possibilities)
            res = max(res, largest)

        return res