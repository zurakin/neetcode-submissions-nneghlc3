class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveBills = 0
        tenBills = 0
        for bill in bills:
            if bill == 5:
                fiveBills += 1
                continue
            elif bill == 10:
                tenBills += 1
                
            change = bill-5 # either 0, 5, 15
            if change >= 10 and tenBills > 0:
                tenBills -= 1
                change -= 10
            while change >= 5 and fiveBills > 0:
                fiveBills -= 1
                change -= 5
            if change > 0:
                return False
        return True