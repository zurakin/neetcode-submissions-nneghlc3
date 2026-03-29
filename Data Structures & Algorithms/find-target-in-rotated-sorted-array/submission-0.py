class Solution:
    def getRotation(self, nums):
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
        return rotation
    
    def get(self, nums, i, r):
        return nums[(i+r) % len(nums)]

    def search(self, nums: List[int], target: int) -> int:
        r = self.getRotation(nums)
        left = 0
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            midValue = self.get(nums, mid, r)
            if midValue == target:
                return (mid+r) % len(nums)
            if midValue < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1