class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = 0
        while True:
            if current+nums[current] >= len(nums)-1:
                return True
            if nums[current] <= 0:
                return False
            nxt = current+1
            for i in range(1, nums[current]+1):
                option = current + i
                if nxt+nums[nxt] < option+nums[option]:
                    nxt = option
            current = nxt

            
            