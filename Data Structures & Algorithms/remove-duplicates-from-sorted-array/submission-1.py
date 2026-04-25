class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        previousVal = float("-inf")
        for i in range(len(nums)):
            if nums[i] > previousVal:
                nums[pos] = nums[i]
                previousVal = nums[i]
                pos += 1
        return pos