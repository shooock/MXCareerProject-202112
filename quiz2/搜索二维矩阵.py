class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = len(matrix)
        row = len(matrix[0])
        l = 0
        r = line - 1
        while l <= r:
            mid = l + (r - l) // 2
            cur = matrix[0][mid]
            if cur == target:
                return True
            elif cur < target:
                temp = mid
                l = mid + 1
            else:
                r = mid - 1

        l = 1
        r = row - 1
        while l < r:
            mid = l + (r - l) // 2
            cur = matrix[mid][temp]
            if cur == target:
                return True
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1

        return False