class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCounter = 0
        for n in nums:
            if n==0:
                zeroCounter += n==0
            else:
                product *= n
        if zeroCounter >= 2:
            return [0] * len(nums)
        if zeroCounter == 1:
            return [0 if nums[i] != 0 else product for i in range(len(nums))]
        return [product//nums[i] if nums[i] != 0 else product for i in range(len(nums))]