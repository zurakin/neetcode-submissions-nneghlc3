class Solution:
    def findMin(self, nums: List[int]) -> int:
        firstElement = nums[0]
        left = 0
        right = len(nums) - 1
        rotation = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < firstElement:
                rotation = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[rotation]
