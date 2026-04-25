class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k += 1
        seen = set()
        for i in range(min(k, len(nums))):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
    
        for i in range(k, len(nums)):
            seen.remove(nums[i-k])
            if nums[i] in seen:
                return True
            seen.add(nums[i])

        return False
