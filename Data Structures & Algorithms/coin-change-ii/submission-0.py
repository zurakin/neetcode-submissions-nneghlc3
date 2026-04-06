class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = {}
        def changeRec(amount, start):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if (amount, start) in mem:
                return mem[(amount, start)]
            res = 0
            for i in range(start, len(coins)):
                res += changeRec(amount-coins[i], i)
            mem[(amount, start)] = res
            return res
        return changeRec(amount, 0)