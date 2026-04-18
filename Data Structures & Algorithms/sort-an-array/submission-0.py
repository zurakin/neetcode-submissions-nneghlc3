class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        arr1 = self.sortArray(nums[:mid])
        arr2 = self.sortArray(nums[mid:])

        res = [0 for _ in range(len(nums))]
        i = 0
        j = 0
        while i + j < len(nums):
            if i >= len(arr1):
                res[i+j] = arr2[j]
                j += 1
            elif j >= len(arr2):
                res[i+j] = arr1[i]
                i += 1
            else:
                if arr1[i] < arr2[j]:
                    res[i+j] = arr1[i]
                    i += 1
                else:
                    res[i+j] = arr2[j]
                    j += 1
        return res
