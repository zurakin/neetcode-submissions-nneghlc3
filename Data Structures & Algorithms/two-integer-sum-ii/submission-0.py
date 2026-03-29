class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg = 0
        end = len(numbers) - 1
        while True:
            s = numbers[beg]+numbers[end]
            if s == target:
                return [beg+1, end+1]
            elif s < target:
                beg += 1
            else: 
                end -= 1
        