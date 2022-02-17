class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            nonlocal res
            cnt = 1
            grid[r][c] = -1
            for (nr,nc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= nr < row and 0<= nc < col and grid[nr][nc] == 1:
                    cnt += dfs(nr,nc)
            res = max(res,cnt)
            return cnt
        res =0
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dfs(r,c)
        return res