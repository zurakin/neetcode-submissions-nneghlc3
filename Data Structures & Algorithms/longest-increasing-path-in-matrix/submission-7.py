from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

        neighbors = [[[] for _ in range(COLS)] for _ in range(ROWS)]
        predecessors = [[0] * COLS for _ in range(ROWS)]

        for y in range(ROWS):
            for x in range(COLS):
                for dy, dx in DIRS:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < ROWS and 0 <= nx < COLS and matrix[ny][nx] > matrix[y][x]:
                        neighbors[y][x].append((ny, nx))
                        predecessors[ny][nx] += 1

        queue = deque((y, x) for y in range(ROWS) for x in range(COLS) if predecessors[y][x] == 0)

        path_length = 0
        while queue:
            path_length += 1
            for _ in range(len(queue)):
                y, x = queue.popleft()
                for ny, nx in neighbors[y][x]:
                    predecessors[ny][nx] -= 1
                    if predecessors[ny][nx] == 0:
                        queue.append((ny, nx))

        return path_length