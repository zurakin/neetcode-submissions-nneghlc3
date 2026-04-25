class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        pos = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[pos] = nums[i]
                seen.add(nums[i])
                pos += 1
        return pos