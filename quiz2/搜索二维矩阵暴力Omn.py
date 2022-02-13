class Solution:
    def searchMatrix(self, matrix, target):
        line = len(matrix) - 1
        row = len(matrix[0]) - 1
        i = j = 0
        while True:
            if matrix[i][j] == target:
                return True
            elif i < line and matrix[i + 1][j] <= target:
                i += 1
            elif j < row and matrix[i][j + 1] <= target:
                j += 1
            else:
                return False