class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            beg = i+1
            end = len(nums)-1
            while beg < end:
                s = nums[i] + nums[beg] + nums[end]
                if s == 0:
                    res.append([nums[i], nums[beg], nums[end]])
                    end -= 1
                    while end >= 0 and nums[end] == nums[end+1]:
                        end -= 1
                    beg += 1
                    while beg < len(nums) and nums[beg] == nums[beg-1]:
                        beg += 1
                elif s > 0:
                    end -= 1
                    while end >= 0 and nums[end] == nums[end+1]:
                        end -= 1
                else: 
                    beg += 1
                    while beg < len(nums) and nums[beg] == nums[beg-1]:
                        beg += 1
        return res