class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in unique:
                sequenceSize = 1
                current = n
                while current+1 in unique:
                    sequenceSize += 1 
                    current += 1
                longest = max(longest, sequenceSize)
        return longest

        