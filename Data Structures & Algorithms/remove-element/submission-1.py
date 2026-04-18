class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums)-1
        i = 0
        while i <= end:
            if nums[end] == val:
                end -= 1
                continue
            if nums[i] == val:
                tmp = nums[end]
                nums[end] = nums[i]
                nums[i] = tmp
                end -= 1
                i += 1
            else:
                i += 1
        return end+1
