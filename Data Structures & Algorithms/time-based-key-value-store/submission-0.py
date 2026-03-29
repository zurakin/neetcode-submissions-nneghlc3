class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = [(timestamp, value)]
        else:
            self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        values = self.m[key]
        left = 0
        right = len(values) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            midTimestamp = values[mid][0]
            if midTimestamp <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res
        
