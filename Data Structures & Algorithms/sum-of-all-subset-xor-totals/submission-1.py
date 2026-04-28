class Solution:
    # Key observation: every bit that is set to 1 in at least 1 num 
    # will be equal to 1 in the XORs of subsets exactly half the time
    # That's 2**(n-1) 
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        # for every bit set to 1 in at least one num:
        #   res += 2**(bit) * 2**(n-1) 
        OR = 0
        for num in nums:
            OR |= num
        
        i = 0
        while OR > 0:
            bit = OR & 1
            OR >>= 1
            if bit:
                res += 2**i * 2**(n-1)
            i += 1

        return res