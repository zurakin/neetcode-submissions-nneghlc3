# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         product = 1
#         zeroCounter = 0
#         for n in nums:
#             if n==0:
#                 zeroCounter += n==0
#             else:
#                 product *= n
#         if zeroCounter >= 2:
#             return [0] * len(nums)
#         if zeroCounter == 1:
#             return [0 if nums[i] != 0 else product for i in range(len(nums))]
#         return [product//nums[i] if nums[i] != 0 else product for i in range(len(nums))]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1]
        print(prefixes, suffixes, sep="\n")
        return [prefixes[i] * suffixes[i] for i in range(len(nums))]