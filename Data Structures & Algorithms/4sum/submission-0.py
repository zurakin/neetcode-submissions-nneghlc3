class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []

        def search(startIndex, A, B, globalTarget):
            target = globalTarget - A - B
            i = startIndex
            j = N-1
            while i < j:
                s = nums[i] + nums[j]
                if s == target:
                    res.append([A, B, nums[i], nums[j]])
                    i += 1
                    while i < N and nums[i] == nums[i-1]:
                        i += 1
                    j -= 1
                    while j >= 0 and nums[j] == nums[j+1]:
                        j -= 1
                elif s < target:
                    i += 1
                else:
                    j -= 1
        prevI = None
        for i in range(N):
            if nums[i] == prevI:
                continue
            prevJ = None
            for j in range(i+1, N):
                if nums[j] == prevJ:
                    continue
                search(j+1, nums[i], nums[j], target)
                prevJ = nums[j]
            prevI = nums[i]
        return res
                