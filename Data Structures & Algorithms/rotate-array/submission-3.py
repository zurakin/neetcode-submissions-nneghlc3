class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or k == 0:
            return
        shiftsPerCycle = n*k//math.gcd(n, k)
        jumpsPerCycle = shiftsPerCycle // k
        nbCycles = n // jumpsPerCycle
        for i in range(nbCycles):
            current = (i+k) % n
            buffer = nums[i]
            for _ in range(jumpsPerCycle):
                nxtBuffer = nums[current]
                nums[current] = buffer
                buffer = nxtBuffer
                current = (current+k) % n
