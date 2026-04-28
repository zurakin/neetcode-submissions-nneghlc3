class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        currentArr = []
        def backtrack(i):
            # print(i, currentArr)
            if len(currentArr) == k:
                res.append(currentArr[:])
                return
            if i == n+1:
                return
            currentArr.append(i)
            backtrack(i+1)
            currentArr.pop()
            backtrack(i+1)
        
        backtrack(1)
        return res
