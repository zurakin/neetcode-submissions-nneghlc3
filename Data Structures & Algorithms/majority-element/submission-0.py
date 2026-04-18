class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        counter = 0
        for n in nums:
            if counter == 0:
                majority = n
                counter = 1
                continue
            if n == majority:
                counter += 1
            else:
                counter -= 1
        return majority
