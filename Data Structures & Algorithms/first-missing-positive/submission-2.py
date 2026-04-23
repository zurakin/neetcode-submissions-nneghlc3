class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def insert(n):
            if n <= 0 or n > len(nums) or nums[n-1] == n:
                return
            nxt = nums[n-1]
            nums[n-1] = n
            insert(nxt)
        for i in range(len(nums)):
            insert(nums[i])
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1