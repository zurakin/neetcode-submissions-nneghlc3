class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def ship(capacity):
            currentCapacity = capacity
            currentDay = 1
            for w in weights:
                if w <= currentCapacity:
                    currentCapacity -= w
                else:
                    currentCapacity = capacity - w
                    currentDay += 1
                    if currentDay > days: 
                        return False 
            return True 
        
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if ship(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
            