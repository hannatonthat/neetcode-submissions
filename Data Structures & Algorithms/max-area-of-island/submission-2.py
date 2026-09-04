class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            res = 1
            for dr, dc in dirs:
                res += dfs(dr + r, dc + c)
            return res
                            
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res