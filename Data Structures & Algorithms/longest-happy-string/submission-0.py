class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = []
        if a > 0:
            heapq.heappush(chars, (-a, 'a'))
        if b > 0:
            heapq.heappush(chars, (-b, 'b'))
        if c > 0:
            heapq.heappush(chars, (-c, 'c'))

        s = ""
        while chars:
            usesLeft, charToUse = heapq.heappop(chars)
            if len(s) >= 2 and s[-1] == s[-2] and s[-1] == charToUse:
                if len(chars) == 0:
                    return s
                usesLeftAlt, charToUseAlt = heapq.heappop(chars)
                s += charToUseAlt
                usesLeftAlt += 1
                if usesLeftAlt < 0:
                    heapq.heappush(chars, (usesLeftAlt, charToUseAlt))
            else:
                s += charToUse
                usesLeft += 1
            if usesLeft < 0:
                heapq.heappush(chars, (usesLeft, charToUse))
        return s

            