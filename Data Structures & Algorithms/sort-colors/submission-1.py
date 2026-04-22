class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        beg = 0 
        # while beg < len(nums) and nums[beg] == 0:
        #     beg += 1
        end = len(nums)-1
        # while end >= 0 and nums[end] == 2:
        #     end -= 1
        i = 0
        while beg <= i <= end:
            if nums[i] == 0:
                if i == beg:
                    i += 1
                    beg += 1
                else:
                    nums[i] = nums[beg]
                    nums[beg] = 0
                    beg += 1
                # while beg < len(nums) and nums[beg] == 0:
                #     beg += 1
            elif nums[i] == 2:
                nums[i] = nums[end]
                nums[end] = 2
                end -= 1
                # while end >= 0 and nums[end] == 2:
                #     end -= 1
            else:
                i += 1

