class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        res = []
        def explorePerimiter(y, x, H, W):
            if H <= 0 or W <= 0:
                return
            res.append(matrix[y][x])
            directions = [(0, 1, W-1), (1, 0, H-1)]
            if H-1 > 0:
                directions.append((0, -1, W-1))
            if W-1 > 0:
                directions.append((-1, 0, H-2))
            for dy, dx, distance in directions:
                for _ in range(distance):
                    y += dy
                    x += dx
                    res.append(matrix[y][x])

        H = len(matrix)
        W = len(matrix[0])
        y, x, = 0, 0
        while H > 0 and W > 0:
            explorePerimiter(y, x, H, W)
            H -= 2
            W -= 2
            y += 1
            x += 1
        
        return res