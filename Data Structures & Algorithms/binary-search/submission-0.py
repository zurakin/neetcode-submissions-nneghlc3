class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            current = (right+left) // 2
            print(nums[left], nums[right], nums[current])
            currentNum = nums[current]
            if currentNum == target:
                return current
            if currentNum < target:
                left = current + 1
            else:
                right = current -1
        return -1
