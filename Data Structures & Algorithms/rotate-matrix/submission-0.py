class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        # i, j -> j, N-1-i
        
        def getNext(i, j):
            return j, N-1-i

        def rotate(i, j):
            tmp = matrix[i][j]
            for _ in range(4):
                nextI, nextJ = getNext(i, j)
                tmp, matrix[nextI][nextJ] = matrix[nextI][nextJ], tmp
                i, j = nextI, nextJ

        for r in range(N//2):
            for c in range(r, N-r-1):
                rotate(r, c)


            