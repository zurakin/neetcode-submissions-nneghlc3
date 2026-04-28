class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        currentXor = 0
        def backtrack(i):
            nonlocal currentXor, res
            if i == len(nums):
                res += currentXor
                return
            currentXor ^= nums[i]
            backtrack(i+1)
            currentXor ^= nums[i]
            backtrack(i+1)

        backtrack(0)
        return res
