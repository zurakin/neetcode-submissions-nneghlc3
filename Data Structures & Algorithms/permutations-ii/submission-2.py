class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i):
            if i == len(nums)-1:
                res.append(nums[:])
                return
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)

        return res