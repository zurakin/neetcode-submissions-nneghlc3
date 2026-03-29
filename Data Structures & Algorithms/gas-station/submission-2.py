class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        deltaArr = [gas[i]-cost[i] for i in range(len(gas))]
        if sum(deltaArr) < 0:
            return -1
        
        print(deltaArr)
        
        res = 0
        s = deltaArr[0]
        for i in range(1, len(deltaArr)):
            if s < 0:
                s = deltaArr[i]
                res = i
            else:
                s += deltaArr[i]
        return res

