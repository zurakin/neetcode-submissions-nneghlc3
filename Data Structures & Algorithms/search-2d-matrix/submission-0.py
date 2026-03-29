class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        left = 0 
        right = len(matrix) * len(matrix[0]) - 1
    
        while left <= right:
            middle = (left + right) // 2
            middleValue = get(matrix, middle)
            if middleValue == target:
                return True
            if middleValue < target:
                left = middle + 1
            else: 
                right = middle - 1
        return False
        
def get(m, i):
    h = len(m)
    w = len(m[0])

    r = i // w
    c = i % w

    return m[r][c]