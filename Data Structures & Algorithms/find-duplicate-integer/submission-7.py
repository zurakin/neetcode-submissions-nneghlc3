class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                fast = 0
                break
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:
                return fast
        