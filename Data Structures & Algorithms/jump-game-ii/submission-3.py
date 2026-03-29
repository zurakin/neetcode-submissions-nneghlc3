class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current = 0
        while current < len(nums)-1:
            jumps += 1
            if current+nums[current] >= len(nums)-1:
                    break
            nxt = current+1
            for i in range(1, nums[current]+1):
                if nxt+nums[nxt] <= current+i+nums[current+i]:
                    nxt = current+i
            current = nxt

        return jumps

